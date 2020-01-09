from tkinter import *
from math import*
#from numpy import*
root=Tk()#idk
width=800
height=800
canvas=Canvas(root,width=width,height=height)
canvas.grid()
Yaxis=canvas.create_line(800/2, 0, 800/2, 800, fill ="red")
Xaxis1=canvas.create_line(0, 800/2, 800/2, 800/2, fill ="blue")#xaxis1 is negative x axis
Xaxis2=canvas.create_line(800/2, 800/2, 800, 800/2, fill ="blue")
Zaxis1=canvas.create_line(800/2, 800/2, 800/2, 800/2, fill ="green")#zaxis1 is positive z axis
Zaxis2=canvas.create_line(800/2, 800/2, 800/2, 800/2, fill ="green")


def convertToAxis(range):
    #creates grid to place numbers
    I=[]
    i=-range/2
    while(i<range/2):
        I.append(i)
        i+=.025
    return(I)

def buildGraph(grid,function,width,height,ran,scaleFacX,scaleFacY,zDist,zSlope):
    #converts back to GUI grid and graphs
    X=[]
    Y=[]
    for s in grid:
        func=-(s**2)
        
        ###This needs fixing###
        if(zDist>50):
            
            if(zSlope>1.3):
                Y.append(func*height/ran*scaleFacX/scaleFacY+height/2.)
                X.append(s*width/ran+width/2.)
            elif(zSlope<0.7):
                Y.append(func*height/ran+height/2.)
                X.append(s*width/ran*scaleFacY/scaleFacX+width/2.)
            elif(0.7<zSlope<1.3):
                Y.append(func*height/ran+height/2.)
                X.append(s*width/ran+width/2.)
        else:
            Y.append(func*height/ran+height/2.)
            X.append(s*width/ran+width/2.)
        ##Idea: have the graph vary with the length of z axis and vary it base on the slope of z axis
        r=abs(scaleFacX-scaleFacY)
        
##        Y.append(func*height/ran+height/2.)
##        X.append(s*width/ran+width/2.)
        ###
    for p in range(len(X)-1,-1,-1):
        #canvas.create_oval(X[p]+scaleFacX,Y[p]+scaleFacY,X[p]+scaleFacX,Y[p]+scaleFacY)
        canvas.create_oval(X[p],Y[p],X[p],Y[p])

def createAxis(X1,X2,Y1,Y2,firstNum,ran):
    #Makes an axis depending on parameters
    if(X1!=X2):
        o=int(firstNum)
        slope=(Y1-Y2)/(X1-X2)
        Xdist=(X1-X2)
        Ydist=(Y1-Y2)
        i=X1
        j=Y1
        while(o<=ran+firstNum):#find slope of line and make perpindicular to line
            y=j
            if(abs(slope*2)<10 and abs(slope/2)>.1):#creates perpindicular axis lines
                number=canvas.create_line(int(i)-(slope*2), y+2*(-1/slope), int(i)+2*(slope), y-2*(-1/slope))
            elif(abs(slope*2)>10):#initial y axis
                number=canvas.create_line(int(i)-10, y, int(i)+10, y)
            elif(abs(slope/2)<.1):#initial x axis
                number=canvas.create_line(int(i), y+10, int(i), y-10)
            
            num=str(o)
            lbel6=canvas.create_text(int(i),y-20,text=num)
            i-=Xdist/ran
            j-=Ydist/ran
            o+=1
        
        

def leftMotion(event):
    if(0<=event.y<800 and 0<=event.x<800):#need to account for y being over 400 while x being less also need to account for 
        canvas.delete("all")
        Yaxis2=canvas.create_line(800/2, 800/2, 800/2-event.y/2, 800-event.y/2, fill ="red")
        Xaxis1=canvas.create_line(event.x/2, 800/2+event.x/2, 800/2, 800/2, fill ="blue")#FIRST Y COMPONENT OF X DOESNT WORK PROPERLY
        Xaxis2=canvas.create_line(800/2, 800/2, 800-event.x/2, 800/2-event.x/2, fill ="blue")
        Yaxis1=canvas.create_line(800/2+event.y/2, event.y/2, 800/2, 800/2, fill ="red")#FIRST X POINT OF Y DOESNT WORK PROPERLY
        createAxis(event.x/2,400,800/2+event.x/2,400,-5,5)#X1LEFT
        createAxis(400,800-event.x/2,400,800/2-event.x/2,0,5)#X2RIGHT
        createAxis(400,800/2+event.y/2,400,event.y/2,0,5)#Y1TOP
        createAxis(800/2-event.y/2,400,800-event.y/2,400,-5,5)#Y2BOT
        P=convertToAxis(20)#controls range of numbers
        rangeArray=[-1,-1.7,-5,1,1.7,5,10000]
        if(event.y+event.x<800):
            Zaxis2=canvas.create_line(800/2-event.x/2, 800/2-event.y/2, 800/2, 800/2, fill ="green")#zaxis1 is positive z axis
            Zaxis1=canvas.create_line(800/2, 800/2, 800/2+event.x/2, 800/2+event.y/2, fill ="green")
            createAxis(400,800/2+event.x/2,400,800/2+event.y/2,0,5)#Z2
            createAxis(800/2-event.x/2,400,800/2-event.y/2,400,-5,5)#Z1
            slopeZ2=(event.y/2)/(event.x/2)
            d=2*sqrt((event.x/2)**2+(event.y**2))
            for z in rangeArray:
                buildGraph(P,"f(x)=x^2",800-event.x/z,800-event.y/z,20,event.x/2,event.y/2,d,slopeZ2)
##            buildGraph(P,"f(x)=x^2",800-event.x,800-event.y,20,event.x/2,event.y/2)

        else:
            y=800-event.y
            x=800-event.x
            
            Zaxis1=canvas.create_line(event.y/2, event.x/2, 800/2, 800/2, fill ="green")#zaxis1 is positive z axis
            Zaxis2=canvas.create_line(800/2, 800/2, 800/2+y/2, 800/2+x/2, fill ="green")
            
            
            createAxis(400,800/2+y/2,400,800/2+x/2,0,5)#Z2
            createAxis(event.y/2,400,event.x/2,400,-5,5)#Z1
            for z in rangeArray:
                buildGraph(P,"f(x)=x^2",event.x/z+800,event.y/z+800,20,400-event.y/2,400-event.x/2)
            
canvas.bind("<B1-Motion>",leftMotion)


root.mainloop()#keeps window open
