#Team ID: 3920
#Author List: Shivansh Rao, Manish Aggarwal, Deepank Grover, Prabhakar Nawale
#Filename: section1.py.
#Theme: Navigate A Terrain Set-1.
#Functions: sine(), cosine(), readImage(), findNeighbours(), colourCell(), buildGraph(), findStartPoint(), findPath(), main().
#Global Variables: NONE
from __future__ import division
import numpy as np
import cv2
import math
import time

##  Returns sine of an angle.
#Function Name: sine()
#Input: angle-Value of angle in degrees.
#Output: sine of the angle value input.
#Logic: This function coverts the angle in degrees to radians and outputs the corresponding sine value.
#Example: sine(30)
def sine(angle):
    return math.sin(math.radians(angle))

##  Returns cosine of an angle
#Function Name: cosine()
#Input: angle-Value of angle in degrees.
#Output: cosine of the angle value input.
#Logic: This function coverts the angle in degrees to radians and outputs the corresponding cosine value.
#Example: cosine(30)
def cosine(angle):
    return math.cos(math.radians(angle))

##  Reads an image from the specified filepath and converts it to Grayscale. Then applies binary thresholding
##  to the image.
#Function Name: readImage()
#Input: filePath.
#Output: Returns the image corresponding to the input filepath.
#Logic: Reads an image from the specified filepath and converts it to Grayscale. Then applies binary thresholding to the image.
#Example: readImage("image_00.jpg")
def readImage(filePath):
    mazeImg = cv2.imread(filePath)
    grayImg = cv2.cvtColor(mazeImg, cv2.COLOR_BGR2GRAY)
    ret,binaryImage = cv2.threshold(grayImg,127,255,cv2.THRESH_BINARY)
    return binaryImage

##  This function accepts the img, level and cell number of a particular cell and the size of the maze as input
##  arguments and returns the list of cells which are traversable from the specified cell.
#Function Name: findNeighbours()
#Input: image, parameter 1(level), parameter 2(cellnum), parameter3(size)-these parameters are called from the main function.
#Output: returns the accessible neighbours.
#Logic: analyses all the neighbouring cells of a cell and returns the accessible cells for the cell coordinates specified in parameters.
#Example: findNeighbours(img, 1, 6, 1)
def findNeighbours(img, level, cellnum, size):
    neighbours = []

    arr0=[]
    arrd=[]
    arru1=[]
    arru2=[]
    arrr=[]
    arrl=[]
    aa=0;
    arrur=[]
    arrul=[]
    x=level
    
    y=cellnum

    if (size==1):


        if(level==0 and cellnum==0):
            theta0=360/6
            for y1 in xrange(1,7):
                px=img[220+40*cosine(90-(y1*theta0) + theta0/2),220+40*sine(90-(y1*theta0) + theta0/2)]
                if px==0 or px==1 or px==2:
                    aa=1;
                elif px==255 or px==254 or px==253:
                    aa=1;
                    arr0.append([x+1,y1])
                    neighbours=arr0;
                    

        if(x==1):
        
            c=int(math.pow(2,x-1))          
            theta=360/(6*c)
            px1=img[220+40*x*cosine(90-(y*theta) + theta/2),220+40*x*sine(90-(y*theta) + theta/2)]
            if px1==0 or px1==1 or px1==2:
                aa=1;
            elif px1==255 or px1==254 or px1==253:
                aa=1;
                arrd.append([0,0])
                
            d=int(math.pow(2,x))
            theta1=360/(6*d)
            px2=img[220+40*(x+1)*cosine(90-(2*y*theta1)+theta1/2),220+40*(x+1)*sine(90-(2*y*theta1)+theta1/2)]
            if px2==0 or px2==1 or px2==2:
                aa=1;
            elif px2==255 or px2==254 or px2==253:
                aa=1;
                arru1.append([x+1,2*y])
                
                

            px3=img[220+40*(x+1)*cosine(90-(2*y*theta1)+3*(theta1/2)),220+40*(x+1)*sine(90-(2*y*theta1)+3*(theta1/2))]
            if px3==0 or px3==1 or px3==2:
                aa=1;
            elif px3==255 or px3==254 or px3==253:
                aa=1;
                arru2.append([x+1,2*y-1])


            px4=img[220+(40*x+20)*cosine(90-y*theta),220+(40*x+20)*sine(90-y*theta)]
            if px4==0 or px4==1 or px4==2:
                aa=1;
            elif px4==255 or px4==254 or px4==253:
                aa=1;
                arrr.append([x,y+1])
                if(y==6):
                    arrr.append([x,1])
                 
                 
            
            px5=img[220+(40*x+20)*cosine(90-(y-1)*theta),220+(40*x+20)*sine(90-(y-1)*theta)]
            if px5==0 or px5==1 or px5==2:
                aa=1;
            elif px5==255 or px5==254 or px5==253:
                aa=1;
                if(y==1):
                    arrl.append([x,6])
                else:
                    arrl.append([x,y-1])
                
            neighbours=arrd+arru1+arru2+arrr+arrl
            
       

        elif(x==2):
            c=int(math.pow(2,x-1))
            theta=int(360/(6*c))
            px1=img[220+40*x*cosine(90-(y*theta) + theta/2),220+40*x*sine(90-(y*theta) + theta/2)]
            if px1==0 or px1==1 or px1==2:
                aa=1;
            elif px1==255 or px1==254 or px1==253:
                aa=1;
                if(x%2==0):
                    x1=int(x/2)
                else:
                    x1=int(x/2)+1
                if(y%2==0):
                    y1=int(y/2)
                else:
                    y1=int(y/2)+1
                arrd.append([x1,y1])

            d=int(math.pow(2,x))
            theta1=360/(6*d)
            px2=img[220+40*(x+1)*cosine(90-(2*y*theta1)+theta1/2),220+40*(x+1)*sine(90-(2*y*theta1)+theta1/2)]
            if px2==0 or px2==1 or px2==2:
                aa=1;
            elif px2==255 or px2==254 or px2==253:
                aa=1;
                arru1.append([x+1,2*y])
                

            px3=img[220+40*(x+1)*cosine(90-(2*y*theta1)+3*(theta1/2)),220+40*(x+1)*sine(90-(2*y*theta1)+3*(theta1/2))]
            if px3==0 or px3==1 or px3==2:
                aa=1;
            elif px3==255 or px3==254 or px3==253:
                aa=1;
                arru2.append([x+1,2*y-1])


            px4=img[220+(40*x+20)*cosine(90-y*theta),220+(40*x+20)*sine(90-y*theta)]
            if px4==0 or px4==1 or px4==2:
                aa=1;
            elif px4==255 or px4==254 or px4==253:
                aa=1;
                if(y==12):
                    arrr.append([x,1])
                else:
                    arrr.append([x,y+1])
            
            px5=img[220+(40*x+20)*cosine(90-(y-1)*theta),220+(40*x+20)*sine(90-(y-1)*theta)]
            if px5==0 or px5==1 or px5==2:
                aa=1;
            elif px5==255 or px5==254 or px5==253:
                aa=1;
                if(y==1):
                    arrl.append([x,12])
                else:
                    arrl.append([x,y-1])
                
            neighbours=arrd+arru1+arru2+arrr+arrl

        elif(x==3):
            
            c=int(math.pow(2,x-1))
            theta=360/(6*c)
            px1=img[220+40*x*cosine(90-(y*theta) + theta/2),220+40*x*sine(90-(y*theta) + theta/2)]
            if px1==0 or px1==1 or px1==2:
                aa=1;
            elif px1==255 or px1==254 or px1==253:
                aa=1;
                if(x%2==0):
                    x1=int(x/2)
                else:
                    x1=int(x/2)+1
                if(y%2==0):
                    y1=int(y/2)
                else:
                    y1=int(y/2)+1
                arrd.append([x1,y1])

            d=int(math.pow(2,x-1))
            theta1=360/(6*d)
            px2=img[220+40*(x+1)*cosine(90-(y*theta1)+theta1/2),220+40*(x+1)*sine(90-(y*theta1)+theta1/2)]
            if px2==0 or px2==1 or px2==2:
                aa=1;
            elif px2==255 or px2==254 or px2==253:
                aa=1;
                arru1.append([x+1,y])
                

            px4=img[220+(40*x+20)*cosine(90-y*theta),220+(40*x+20)*sine(90-y*theta)]
            if px4==0 or px4==1 or px4==2:
                aa=1;
            elif px4==255 or px4==254 or px4==253:
                aa=1;
                if(y==24):
                    arrr.append([x,1])
                else:
                    arrr.append([x,y+1])
            px5=img[220+(40*x+20)*cosine(90-(y-1)*theta),220+(40*x+20)*sine(90-(y-1)*theta)]
            if px5==0 or px5==1 or px5==2:
                aa=1;
            elif px5==255 or px5==254 or px5==253:
                aa=1;
                if(y==1):
                    arrl.append([x,24])
                else:
                    arrl.append([x,y-1])
            neighbours=arrd+arru1+arrr+arrl
            

        elif(x==4):
            
            c=int(math.pow(2,x-2))
            theta=360/(6*c)
            px1=img[220+40*x*cosine(90-(y*theta) + theta/2),220+40*x*sine(90-(y*theta) + theta/2)]
            if px1==0 or px1==1 or px1==2:
                aa=1;
            elif px1==255 or px1==254 or px1==253:
                aa=1;
                arrd.append([x-1,y])
                
            theta1=360/(6*4)
            px2=img[220+40*(x+1)*cosine(90-(y*theta1)+theta1/2),220+40*(x+1)*sine(90-(y*theta1)+theta1/2)]
            if px2==0 or px2==1 or px2==2:
                aa=1;
            elif px2==255 or px2==254 or px2==253:
                aa=1;
                arru1.append([x+1,y])
            

            px4=img[220+(40*x+20)*cosine(90-y*theta),220+(40*x+20)*sine(90-y*theta)]
            if px4==0 or px4==1 or px4==2:
                aa=1;
            elif px4==255 or px4==254 or px4==253:
                aa=1;
                if(y==24):
                    arrr.append([x,1])
                else:
                    arrr.append([x,y+1])
            px5=img[220+(40*x+20)*cosine(90-(y-1)*theta),220+(40*x+20)*sine(90-(y-1)*theta)]
            if px5==0 or px5==1 or px5==2:
                aa=1;
            elif px5==255 or px5==254 or px5==253:
                aa=1;
                if(y==1):
                    arrl.append([x,24])
                else:
                    arrl.append([x,y-1])

            neighbours=arrd+arrr+arrl+arru1

    if(size==2):

        
        if(level==0 and cellnum==0):
            theta0=360/6
            for y1 in xrange(1,7):
                px=img[300+40*cosine(90-(y1*theta0) + theta0/2),300+40*sine(90-(y1*theta0) + theta0/2)]
                if px==0 or px==1 or px==2:
                    aa=1;
                elif px==255 or px==254 or px==253:
                    aa=1;
                    arr0.append([x+1,y1])
                    neighbours=arr0;

        if(x==1):
        
            c=int(math.pow(2,x-1))          
            theta=360/(6*c)
            px1=img[300+40*x*cosine(90-(y*theta) + theta/2),300+40*x*sine(90-(y*theta) + theta/2)]
            if px1==0 or px1==1 or px1==2:
                aa=1;
            elif px1==255 or px1==254 or px1==253:
                aa=1;
                arrd.append([0,0])
                
            d=int(math.pow(2,x))
            theta1=360/(6*d)
            px2=img[300+40*(x+1)*cosine(90-(2*y*theta1)+theta1/2),300+40*(x+1)*sine(90-(2*y*theta1)+theta1/2)]
            if px2==0 or px2==1 or px2==2:
                aa=1;
            elif px2==255 or px2==254 or px2==253:
                aa=1;
                arru1.append([x+1,2*y])
                

            px3=img[300+40*(x+1)*cosine(90-(2*y*theta1)+3*(theta1/2)),300+40*(x+1)*sine(90-(2*y*theta1)+3*(theta1/2))]
            if px3==0 or px3==1 or px3==2:
                aa=1;
            elif px3==255 or px3==254 or px3==253:
                aa=1;
                arru2.append([x+1,2*y-1])


            px4=img[300+(40*x+20)*cosine(90-y*theta),300+(40*x+20)*sine(90-y*theta)]
            if px4==0 or px4==1 or px4==2:
                aa=1;
            elif px4==255 or px4==254 or px4==253:
                aa=1;
                if(y==6):
                    arrr.append([x,1])
                else:
                    arrr.append([x,y+1])
            
            px5=img[300+(40*x+20)*cosine(90-(y-1)*theta),300+(40*x+20)*sine(90-(y-1)*theta)]
            if px5==0 or px5==1 or px5==2:
                aa=1;
            elif px5==255 or px5==254 or px5==253:
                aa=1;
                if(y==1):
                    arrl.append([x,6])
                else:
                    arrl.append([x,y-1])
                
            neighbours=arrd+arru1+arru2+arrr+arrl
       

        elif(x==2):
            c=int(math.pow(2,x-1))
            theta=360/(6*c)
            px1=img[300+40*x*cosine(90-(y*theta) + theta/2),300+40*x*sine(90-(y*theta) + theta/2)]
            if px1==0 or px1==1 or px1==2:
                aa=1;
            elif px1==255 or px1==254 or px1==253:
                aa=1;
                if(x%2==0):
                    x1=int(x/2)
                else:
                    x1=int(x/2)+1
                if(y%2==0):
                    y1=int(y/2)
                else:
                    y1=int(y/2)+1
                arrd.append([x1,y1])

            d=int(math.pow(2,x))
            theta1=360/(6*d)
            px2=img[300+40*(x+1)*cosine(90-(2*y*theta1)+theta1/2),300+40*(x+1)*sine(90-(2*y*theta1)+theta1/2)]
            
            if px2==0 or px2==1 or px2==2:
                aa=1;
            elif px2==255 or px2==254 or px2==253:
                aa=1;
                arru1.append([x+1,2*y])
                

            px3=img[300+40*(x+1)*cosine(90-(2*y*theta1)+3*(theta1/2)),300+40*(x+1)*sine(90-(2*y*theta1)+3*(theta1/2))]
            if px3==0 or px3==1 or px3==2:
                aa=1;
            elif px3==255 or px3==254 or px3==253:
                aa=1;
                arru2.append([x+1,2*y-1])


            px4=img[300+(40*x+20)*cosine(90-y*theta),300+(40*x+20)*sine(90-y*theta)]
            if px4==0 or px4==1 or px4==2:
                aa=1;
            elif px4==255 or px4==254 or px4==253:
                aa=1;
                if(y==12):
                    arrr.append([x,1])
                else:
                    arrr.append([x,y+1])
            
            px5=img[300+(40*x+20)*cosine(90-(y-1)*theta),300+(40*x+20)*sine(90-(y-1)*theta)]
            if px5==0 or px5==1 or px5==2:
                aa=1;
            elif px5==255 or px5==254 or px5==253:
                aa=1;
                if(y==1):
                    arrl.append([x,12])
                else:
                    arrl.append([x,y-1])
                
            neighbours=arrd+arru1+arru2+arrr+arrl

        elif(x==3):
            
            c=int(math.pow(2,x-1))
            theta=360/(6*c)
            px1=img[300+40*x*cosine(90-(y*theta) + theta/2),300+40*x*sine(90-(y*theta) + theta/2)]
            if px1==0 or px1==1 or px1==2:
                aa=1;
            elif px1==255 or px1==254 or px1==253:
                aa=1;
                if(x%2==0):
                    x1=int(x/2)
                else:
                    x1=int(x/2)+1
                if(y%2==0):
                    y1=int(y/2)
                else:
                    y1=int(y/2)+1
                arrd.append([x1,y1])
                

            d=int(math.pow(2,x-1))
            theta1=360/(6*d)
            px2=img[300+40*(x+1)*cosine(90-(y*theta1)+theta1/2),300+40*(x+1)*sine(90-(y*theta1)+theta1/2)]
            if px2==0 or px2==1 or px2==2:
                aa=1;
            elif px2==255 or px2==254 or px2==253:
                aa=1;
                arru1.append([x+1,y])
                

            px4=img[300+(40*x+20)*cosine(90-y*theta),300+(40*x+20)*sine(90-y*theta)]
            if px4==0 or px4==1 or px4==2:
                aa=1;
            elif px4==255 or px4==254 or px4==253:
                aa=1;
                if(y==24):
                    arrr.append([x,1])
                else:
                    arrr.append([x,y+1])
            px5=img[300+(40*x+20)*cosine(90-(y-1)*theta),300+(40*x+20)*sine(90-(y-1)*theta)]
            if px5==0 or px5==1 or px5==2:
                aa=1;
            elif px5==255 or px5==254 or px5==253:
                aa=1;
                if(y==1):
                    arrl.append([x,24])
                else:
                    arrl.append([x,y-1])
            neighbours=arrd+arru1+arrr+arrl
            

        elif(x==4):
            
            c=int(math.pow(2,x-2))
            theta=360/(6*c)
            px1=img[300+40*x*cosine(90-(y*theta) + theta/2),300+40*x*sine(90-(y*theta) + theta/2)]
            if px1==0 or px1==1 or px1==2:
                aa=1;
            elif px1==255 or px1==254 or px1==253:
                aa=1;
                arrd.append([x-1,y])
                
            theta1=360/(6*4)
            px2=img[300+40*(x+1)*cosine(90-(y*theta1)+theta1/2),300+40*(x+1)*sine(90-(y*theta1)+theta1/2)]
            if px2==0 or px2==1 or px2==2:
                aa=1;
            elif px2==255 or px2==254 or px2==253:
                aa=1;
                arru1.append([x+1,y])
            

            px4=img[300+(40*x+20)*cosine(90-y*theta),300+(40*x+20)*sine(90-y*theta)]
            if px4==0 or px4==1 or px4==2:
                aa=1;
            elif px4==255 or px4==254 or px4==253:
                aa=1;
                if(y==24):
                    arrr.append([x,1])
                else:
                    arrr.append([x,y+1])
            px5=img[300+(40*x+20)*cosine(90-(y-1)*theta),300+(40*x+20)*sine(90-(y-1)*theta)]
            if px5==0 or px5==1 or px5==2:
                aa=1;
            elif px5==255 or px5==254 or px5==253:
                aa=1;
                if(y==1):
                    arrl.append([x,24])
                else:
                    arrl.append([x,y-1])

            neighbours=arrd+arrr+arrl+arru1

    
        if(x==5):
            
            
            theta=360/(6*4)
            px1=img[300+40*x*cosine(90-(y*theta) + theta/2),300+40*x*sine(90-(y*theta) + theta/2)]
            if px1==0 or px1==1 or px1==2:
                aa=1;
            elif px1==255 or px1==254 or px1==253:
                aa=1;
                arrd.append([x-1,y])
                 
            
            theta1=(360/(6*8))
            
            
            px2=img[300+40*(x+1)*cosine(90-(2*y*theta1)+theta1/2),300+40*(x+1)*sine(90-(2*y*theta1)+theta1/2)]
            
            if px2==0 or px2==1 or px2==2:
                aa=1;
            elif px2==255 or px2==254 or px2==253:
                aa=1;
                arrur.append([x+1,2*y])
                

            px3=img[300+40*(x+1)*cosine(90-(2*y*theta1)+3*(theta1/2)),300+40*(x+1)*sine(90-(2*y*theta1)+3*(theta1/2))]
            
            if px3==0 or px3==1 or px3==2:
                aa=1;
            elif px3==255 or px3==254 or px3==253:
                aa=1;
                arrul.append([x+1,2*y-1])
                

            px4=img[300+(40*x+20)*cosine(90-y*theta),300+(40*x+20)*sine(90-y*theta)]
        
            if px4==0 or px4==1 or px4==2:
                aa=1;
            elif px4==255 or px4==254 or px4==253:
                aa=1;
                
                if(y==24):
                    arrr.append([x,1])
                elif (y<24):
                    arrr.append([x,y+1])
                
                    
            px5=img[300+(40*x+20)*cosine(90-(y-1)*theta),300+(40*x+20)*sine(90-(y-1)*theta)]
            if px5==0 or px5==1 or px5==2:
                aa=1;
            elif px5==255 or px5==254 or px5==253:
                aa=1;
                
                if(y==1):
                    arrl.append([x,24])
                elif (y>1):
                    arrl.append([x,y-1])
                
                    

            neighbours=arrd+arrur+arrul+arrr+arrl


            
        elif(x==6):
            theta=360/(6*8)
            px1=img[300+40*x*cosine(90-(y*theta) + theta/2),300+40*x*sine(90-(y*theta) + theta/2)]
            if px1==0 or px1==1 or px1==2:
                aa=1;
            elif px1==255 or px1==254 or px1==253:
                aa=1;
                if(x%2==0):
                    x1=int(x/2)+2
                else:
                    x1=int(x/2)+1
                if(y%2==0):
                    y1=int(y/2)
                else:
                    y1=int(y/2)+1
                arrd.append([x1,y1])
                
                
            
            px4=img[300+(40*x+20)*cosine(90-y*theta),300+(40*x+20)*sine(90-y*theta)]
            if px4==0 or px4==1 or px4==2:
                aa=1;
            elif px4==255 or px4==254 or px4==253:
                aa=1;
                if(y==48):
                    arrr.append([x,1])
                else:
                    arrr.append([x,y+1])
                     
            px5=img[300+(40*x+20)*cosine(90-(y-1)*theta),300+(40*x+20)*sine(90-(y-1)*theta)]
            if px5==0 or px5==1 or px5==2:
                aa=1;
            elif px5==255 or px5==254 or px5==253:
                aa=1;
                if(y==1):
                    arrl.append([x,48])
                else:
                    arrl.append([x,y-1])
                    
            neighbours=arrd+arrr+arrl

    return neighbours

##  colourCell function takes 5 arguments:-
##            img - input image
##            level - level of cell to be coloured
##            cellnum - cell number of cell to be coloured
##            size - size of maze
##            colourVal - the intensity of the colour.
##  colourCell basically highlights the given cell by painting it with the given colourVal. Care should be taken that
##  the function doesn't paint over the black walls and only paints the empty spaces. This function returns the image
##  with the painted cell.
#Function Name: colourCell()
#Input: image, parameter 1(level), parameter 2(cellnum), parameter3(size),colorVal(The the color code as given in section 1=230)-these parameters are called from the main function.
#Output:  Returns img whiich has all the colored accessible neighbours.
#Logic: Size of the image controls the center which according to the level number thereby colors the required sector by the help of inbuilt function cv2.ellipse.
#Example: colourCell(img, 1, 6, 1, 230)
def colourCell(img, level, cellnum, size, colourVal):

    y=cellnum
    x=level
    theta=0
    if(size==1):
        cv2.circle(img,(220,220), 40, (colourVal,colourVal,colourVal), -1)
    elif(size==2):
        cv2.circle(img,(300,300), 40, (colourVal,colourVal,colourVal), -1)
        
    if (x==1):
        theta=360/6
    elif (x==2):
        theta=360/12
    elif (x==3):
        theta=360/24
    elif (x==4):
        theta=360/24
    elif(x==5):
        theta=360/24
    elif(x==6):
        theta=360/48
        
    for k in xrange(40*x+3,40*(x+1)-3):
        if (size==1):
            cv2.ellipse(img,(220,220),(k,k), 0,(y-1)*theta+1, y*theta-1,(colourVal,colourVal,colourVal), 2)
        elif (size==2):
            cv2.ellipse(img,(300,300),(k,k), 0,(y-1)*theta+1, y*theta-1,(colourVal,colourVal,colourVal), 2)

    return img

##  Function that accepts some arguments from user and returns the graph of the maze image.
#Function Name: buildGraph()
#Input: key(Stores the coordinates of around which nieghbours were found), neigh(Stores the coordinates of accesible neighbours); image, size(-these parameters are called from the main function).
#Output: Returns the graph{}  which contains all the neighbours with their cell itself.
#Logic: level(i) varies with size which along with cellnumber(cellnum) controls the input to key and neigh which  thereby builds the graph.
#Example: buildGraph(img,1)
def buildGraph(img,size):   ## You can pass your own arguments in this space.
    graph = {}
    
    neigh=findNeighbours(img,0,0,size);
    
    key=str(0)+','+str(0);
    k=0;
    while(k<len(neigh)):
        graph[key]=neigh;
        k+=1;


    i=1;
    if (size==1):
        level=4;
    elif(size==2):
        level=6;
    
    while(i<=level):
        j=1;
        if(i<4):
            cellnum=6*(math.pow(2,i-1))
        elif(i==4 or i==5):
            cellnum=24
        elif(i==6):
            cellnum=48
        while(j<=cellnum):
            key=str(i)+','+str(j);
            
            neigh1=findNeighbours(img,i,j,size);
            
            k1=0;
            while(k1<len(neigh1)):
                graph[key]=neigh1;
                k1+=1;
            j+=1;
        i+=1;
    



    
    return graph


##  Function accepts some arguments and returns the Start coordinates of the maze.
#Function Name: findStartPoint()
#Input: px(stores the value of pixel),theta(base angle which veries according to the size);image and size-these parameters are called from the main function.
#Output: Returns the start[] which stores the starting point of the maze.
#Logic: start point is obtained where px value becomes corresponding to white color(0,1 or 2) which is checked by using the formula (x+rcos(a),y+rsin(a)).
#Example: findStartPoint(img,1)
def findStartPoint(img,size):     ## You can pass your own arguments in this space.
    
    start=[]
    
    if (size==1):
        theta=360/24;
        for y in xrange(1,25):
            px=img[220+200*cosine(90-y*theta+theta/2),220+200*sine(90-y*theta+theta/2)]
            if px==0 or px==1 or px==2:
                aa=1;
            elif px==255 or px==254 or px==253:
                aa=1;
                start.extend((4,y))
                
    if (size==2):
        theta=360/48;
        for y in xrange(1,49):
            px=img[300+280*cosine(90-y*theta+theta/2),300+280*sine(90-y*theta+theta/2)]
            if px==0 or px==1 or px==2:
                aa=1;
            elif px==255 or px==254 or px==253:
                aa=1;
                start.extend((6,y))
    
    
    #################################################################################
    return start

##  Finds shortest path between two coordinates in the maze. Returns a set of coordinates from initial point
##  to final point.
#Function Name: findPath()
#Input: strt(stores the start in the form of string), end_nd(stores end in the form of string), graph(from buildGraph()), start(from findStartPoint()), end(end point accroding to the size), path(stores the coordinates of required path).
#Output: Returns the path required from initial point o final point.
#Logic: Use of Breadth First Search Mechanism(BFS) to find the shortest path.
#Example: findPath(graph,['4,16'],['220,220'],path=[])
def findPath(graph,start,end,path=[]):      ## You can pass your own arguments in this space.

        strt=str(start[0])+','+str(start[1]);
        end_nd=str(end[0])+','+str(end[1]);
        
        path = path + [strt]
        
        
        if strt == end_nd:
            return path
        for node in graph[strt]:
            
            test=str(node[0])+','+str(node[1]);
            if test not in path:
                newpath = findPath(graph, node, end, path)
                
                if newpath:
                    return newpath
        return None
    

    #################################################################################
        return shortest

##  This is the main function where all other functions are called. It accepts filepath
##  of an image as input. You are not allowed to change any code in this function. You are
##  You are only allowed to change the parameters of the buildGraph, findStartPoint and findPath functions
#Function Name: main()
#Input: filePath(File path of the maze to be solved.), flag, img(stores the filePath).
#Output: The shortest path is printed and solved image is shown.
#Logic: Predefined logic for execution of the code.
#Example: main("image_00.jpg",flag=0)
def main(filePath, flag = 0):
    img = readImage(filePath)     ## Read image with specified filepath
    if len(img) == 440:           ## Dimensions of smaller maze image are 440x440
        size = 1
    else:
        size = 2
  
    graph = buildGraph(img,size)   ## Build graph from maze image. Pass arguments as required
    print graph
                
    start = findStartPoint(img,size)  ## Returns the coordinates of the start of the maze
    
    end=(0,0)
    shortestPath = findPath(graph,start,end,path=[])  ## Find shortest path. Pass arguments as required.
    print shortestPath
    string = str(shortestPath) + "\n"
    for i in shortestPath:               ## Loop to paint the solution path.
        my_list=i.split(",");
        img = colourCell(img, int(my_list[0]), int(my_list[1]), size,230)
   
    if __name__ == '__main__':     ## Return value for main() function.
        return img
    else:
        if flag == 0:
            return string
        else:
            return graph
        
## The main() function is called here. Specify the filepath of image in the space given.
if __name__ == "__main__":
    filepath = "image_00.jpg"     ## File path for test image
    img = main(filepath)          ## Main function call
    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
