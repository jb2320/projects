import ctypes
import os
import time

drive = "D:\\"
folder = "Users"
folder2 = "User"
folder3 = "Desktop"
folder4 = "cDesktop"
folder5 = "pics"
image = "wallpaper.jpg"
DIR = os.path.join(drive, folder,folder2,folder3,folder4,folder5)
SPI_SETDESKWALLPAPER = 20
while True:
    for filename in os.listdir(DIR):
        image_path = os.path.join(DIR, filename)
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
        time.sleep(3)