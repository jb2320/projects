from PIL import Image
import os
import json
from bs4 import BeautifulSoup
import urllib2

query = raw_input("Query Image\n")
query = query.split()
query = '+'.join(query)
image_name = "wallpaper"
url = "https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
soup = BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

IMAGES = []
for a in soup.find_all("div", {"class":"rg_meta"}):
    link, Type = json.loads(a.text)["ou"], json.loads(a.text)["ity"]
    IMAGES.append((link,Type))
rimg = []
drive = "D:\\"
folder = "Users"
folder2 = "User"
folder3 = "Desktop"
folder4 = "cDesktop"
folder5 = "pics"
DIR = os.path.join(drive,folder,folder2,folder3,folder4,folder5)
for i, (img, Types) in enumerate(IMAGES):
    requ = urllib2.Request(img, headers={'User-Agent':header})
    try:
        raw_img = urllib2.urlopen(requ).read()
        rimg.append(urllib2.urlopen(requ).read())
    except:
        pass
    cntr = len([i for i in os.listdir(DIR) if image_name in i]) + 1
    if len(Types) == 0:
        f = open(os.path.join(DIR, str(cntr)+image_name+".jpg"), 'wb')
        f.write(raw_img)
        f.close()
        try:
            resiz = Image.open(os.path.join(DIR, str(cntr)+image_name+".jpg"))
            new_img = resiz.resize((1920,1080), Image.BILINEAR)
            new_img.save(os.path.join(DIR, str(cntr)+image_name+".jpg"))
        except:
            os.remove(os.path.join(DIR, str(cntr)+image_name+".jpg"))

    else:

        f = open(os.path.join(DIR, str(cntr)+image_name + "." + Types), 'wb')
        f.write(raw_img)
        f.close()
        try:
            resiz = Image.open(os.path.join(DIR, str(cntr)+image_name + "." + Types))
            new_img = resiz.resize((1920, 1080), Image.BILINEAR)
            new_img.save(os.path.join(DIR, str(cntr)+image_name + "." + Types))
        except:
            os.remove(os.path.join(DIR, str(cntr)+image_name + "." + Types))




#for i in rimg:


print("There are a total of %d images" % len(IMAGES))



