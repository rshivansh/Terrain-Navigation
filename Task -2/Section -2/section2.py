#Team ID: 3920
#Author List: Shivansh Rao, Manish Agrawal, Deepank Grover, Prabhakar Nawale
#Filename: section1.py
#Theme: Navigate A Terrain Set-1
#Functions: sine(), cosine(), readImage(), findNeighbours(), colourCell(), buildGraph(), findStartPoint(), findPath(), main()
#Global Variables: NONE
from __future__ import division
import numpy as np
import cv2
import math
import time

## Reads image in HSV format. Accepts filepath as input argument and returns the HSV
## equivalent of the image.
#Input: filePath(path of image file), mazeImg(reads file path), hsvImg(coverts image form BGR to HSV).
#Output: Returns the image which has been read.
#Logic: Image is read from file path and converted to HSV from BGR.
#Example: readImageHSV("image_00.jpg")
def readImageHSV(filePath):
    mazeImg = cv2.imread(filePath)
    hsvImg = cv2.cvtColor(mazeImg, cv2.COLOR_BGR2HSV)
    return mazeImg

## Reads image in binary format. Accepts filepath as input argument and returns the binary
## equivalent of the image.
#Input: filePath(path of image file), mazeImg(reads file path), grayImg(coverts image form BGR to GRAY),binaryImage(covertys to binary by thresholding).
#Output: Returns the binary image which after read and converted to binary.
#Logic: Image is read from file path and converted to GRAY from BGR then to binary by thresholding.
#Example: readImageHSV("image_00.jpg")
def readImageBinary(filePath):
    mazeImg = cv2.imread(filePath)
    grayImg = cv2.cvtColor(mazeImg, cv2.COLOR_BGR2GRAY)
    ret,binaryImage = cv2.threshold(grayImg,200,255,cv2.THRESH_BINARY)
    return binaryImage

##  Returns sine of an angle.
#Input: angle-Value of angle in degrees
#Output: sine of the angle value input
#Logic: This function coverts the angle in degrees to radians and outputs the corresponding sine value
#Example: sine(30)
def sine(angle):
    return math.sin(math.radians(angle))

##  Returns cosine of an angle
#Input: angle-Value of angle in degrees
#Output: cosine of the angle value input
#Logic: This function coverts the angle in degrees to radians and outputs the corresponding cosine value
#Example: cosine(30)
def cosine(angle):
    return math.cos(math.radians(angle))

##  This function accepts the img, level and cell number of a particular cell and the size of the maze as input
##  arguments and returns the list of cells which are traversable from the specified cell.
#Function Name: findNeighbours()
#Input: image, parameter 1(level), parameter 2(cellnum), parameter3(size)-these parameters are called from the main function
#Output: returns the accessible neighbours
#Logic: analyses all the neighbouring cells of a cell and returns the accessible cells for the cell coordinates specified in parameters 
#Example: findNeighbours(img, level, cellnum, size)
def findNeighbours(img, level, cellnum, size):
    neighbours = []
    ############################# Add your Code Here ################################
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
                
                if(y==6):
                    arrr.append([x,1])
                elif(y<6):
                    arrr.append([x,y+1])
                 
                 
            
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
     

    #################################################################################
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
    ############################# Add your Code Here ################################
     
    y=cellnum
    x=level
    theta=0
    
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
    if size==1:
        cv2.circle(img,(220,220), 40, (colourVal,colourVal,colourVal), -1)
        
        for k in xrange(40*x+3,40*(x+1)-3):
            cv2.ellipse(img,(220,220),(k,k), 0,(y-1)*theta+1, y*theta-1,(colourVal,colourVal,colourVal), 2)
    if size==2:
        cv2.circle(img,(300,300), 40, (colourVal,colourVal,colourVal), -1)
        
        for k in xrange(40*x+3,40*(x+1)-3):
            cv2.ellipse(img,(300,300),(k,k), 0,(y-1)*theta+1, y*theta-1,(colourVal,colourVal,colourVal), 2)

    #################################################################################  
    return img

##  Function that accepts some arguments from user and returns the graph of the maze image.
#Function Name: buildGraph()
#Input: key(Stores the coordinates of around which nieghbours were found), neigh(Stores the coordinates of accesible neighbours); image, size(-these parameters are called from the main function).
#Output: Returns the graph{}  which contains all the neighbours with their cell itself.
#Logic: level(i) varies with size which along with cellnumber(cellnum) controls the input to key and neigh which  thereby builds the graph.
#Example: buildGraph(img,1)
def buildGraph(  img,size  ):      ## You can pass your own arguments in this space.
    graph = {}
    ############################# Add your Code Here ################################
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
        elif(i==4):
            cellnum=24
        elif(i==5 or i==6):
            cellnum=6*(math.pow(2,i-3));
        while(j<=cellnum):
            key= str(i)+','+str(j);
            
            neigh=findNeighbours(img,i,j,size);
            
            k=0;
            while(k<len(neigh)):
                graph[key]=neigh;
                k+=1;
            j+=1;
        i+=1;
    
    
     
    #################################################################################
    return graph

##  Function accepts some arguments and returns the Start coordinates of the maze.
#Function Name: findStartPoint()
#Input: px(stores the value of pixel),theta(base angle which veries according to the size);image and size-these parameters are called from the main function.
#Output: Returns the start[] which stores the starting point of the maze.
#Logic: start point is obtained where px value becomes corresponding to white color(0,1 or 2) which is checked by using the formula (x+rcos(a),y+rsin(a)).
#Example: findStartPoint(img,1)
def findStartPoint(img, size):     ## You can pass your own arguments in this space.
    ############################# Add your Code Here ################################
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
def findPath(graph,start,end,path=[]    ):             ## You can pass your own arguments in this space.
    ############################# Add your Code Here ################################
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

## The findMarkers() function returns a list of coloured markers in form of a python dictionaries
## For example if a blue marker is present at (3,6) and red marker is present at (1,5) then the
## dictionary is returned as :-
##          list_of_markers = { 'Blue':(3,6), 'Red':(1,5)}
#Function Name: findMarkers()
#Input: level, cell number(cellnum), size, filePath,e(array of findMarkers).
#Output: Reurns coordinates of markers in the form of [(x1,y1),(x2,y2)].
#Logic: Value of theta varies according to size and coordinates to be stored are decided on the basis of pixel value at the mid point given by (x+rcos(a),y+rsin(a)).
#Example:findMarkers(1,6,1,img,e) 
def findMarkers(level, cellnum, size,filePath,e):             ## You can pass your own arguments in this space.
    list_of_markers = {}
    ############################# Add your Code Here ################################
    arrd1=[]
    arrd2=[]
    x=level
    y=cellnum
    img=cv2.imread(filePath)


    if size==1:

        if(x==1):
            
            c=int(math.pow(2,x-1))          
            theta=360/(6*c)
            if (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])>245 and (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])<256 and ( img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])<10 and (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])>-1 and ( img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])<10 and ( img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])>-1:
                 
                arrd1.append([x,y])
            if (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])>-1 and (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])<10 and  (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])<10 and (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])>-1 and ( img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][2]) <256 and ( img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])>245:
                
                arrd2.append([x,y])
   
            
       

        elif(x==2):
            
            c=int(math.pow(2,x-1))          
            theta=360/(6*c)
            
            if (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])>245 and (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])<257 and ( img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])<10 and (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])>-1 and ( img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])<10 and ( img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])>-1:
                 
                arrd1.append([x,y])
            if (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])>-1 and (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])<10 and  (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])<10 and (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])>-1 and ( img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][2]) <256 and ( img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])>245:
                 
                arrd2.append([x,y])
   
            
     
        elif(x==3):
            
            c=int(math.pow(2,x-1))          
            theta=360/(6*c)
            if (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])>245 and (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])<256 and ( img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])<10 and (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])>-1 and ( img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])<10 and ( img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])>-1:
                 
                arrd1.append([x,y])
            if (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])>-1 and (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])<10 and  (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])<10 and (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])>-1 and ( img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][2]) <256 and ( img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])>245:
                 
                arrd2.append([x,y])
   
            
        elif(x==4):
            
            c=int(math.pow(2,x-2))
            theta=360/(6*c)
           
            if (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])>245 and (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])<256 and ( img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])<10 and (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])>-1 and ( img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])<10 and ( img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])>-1:
                 
                arrd1.append([x,y])
            if (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])>-1 and (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])<10 and  (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])<10 and (img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])>-1 and ( img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][2]) <256 and ( img[220+((40*x)+20)*cosine(90-(y*theta) + theta/2),220+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])>240:
                
                arrd2.append([x,y])

    if size == 2:
        
        if(x==1):
            
            c=int(math.pow(2,x-1))          
            theta=360/(6*c)
            if (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])>245 and (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])<256 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])<10 and (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])>-1 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])<10 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])>-1:
                
                arrd1.append([x,y])
            if (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])>-1 and (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])<10 and  (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])<10 and (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])>-1 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][2]) <256 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])>245:
                
                arrd2.append([x,y])
   
            
       

        elif(x==2):
            
            c=int(math.pow(2,x-1))          
            theta=360/(6*c)
            if (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])>245 and (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])<256 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])<10 and (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])>-1 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])<10 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])>-1:
                
                arrd2.append([x,y])
            if (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])>-1 and (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])<10 and  (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])<10 and (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])>-1 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][2]) <256 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])>245:
                
                arrd2.append([x,y])
   
            
     
        elif(x==3):
            
            c=int(math.pow(2,x-1))          
            theta=360/(6*c)
            if (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])>245 and (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])<256 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])<10 and (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])>-1 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])<10 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])>-1:
                
                arrd1.append([x,y])
            if (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])>-1 and (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])<10 and  (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])<10 and (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])>-1 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][2]) <256 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])>240:
                
                arrd2.append([x,y])
   
            
        elif(x==4):
            
            c=int(math.pow(2,x-2))
            theta=360/(6*c)
             
            if (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])>240 and (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])<256 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])<10 and (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])>-1 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])<10 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])>-1:
                
                arrd2.append([x,y])
            if (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])>-1 and (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])<10 and  (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])<10 and (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])>-1 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][2]) <256 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])>240:
                
                arrd2.append([x,y])

        elif(x==5):
            c=int(math.pow(2,x-3))
            theta=360/(6*c)
            if (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])>245 and (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])<256 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])<10 and (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])>-1 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])<10 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])>-1:
                
                arrd2.append([x,y])
            if (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])>-1 and (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])<10 and  (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])<10 and (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])>-1 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][2]) <256 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])>245:
                
                arrd2.append([x,y])

        elif(x==6):
            theta=360/(6*8)
            
            if (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])>245 and (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])<256 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])<10 and (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])>-1 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])<10 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])>-1:
                
                
                if(x%2==0):
                    x1=int(x/2)+3
                else:
                    x1=int(x/2)+1
                if(y%2==0):
                    y1=int(y/2)
                else:
                    y1=int(y/2)+1
                arrd1.append([x1,y])
              
                
            if (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])>-1 and (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][0])<10 and  (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])<10 and (img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][1])>-1 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][2]) <256 and ( img[300+((40*x)+20)*cosine(90-(y*theta) + theta/2),300+((40*x)+20)*sine(90-(y*theta) + theta/2)][2])>245:
                
                
                if(x%2==0):
                    x1=int(x/2)+3
                else:
                    x1=int(x/2)+1
                if(y%2==0):
                    y1=int(y/2)
                else:
                    y1=int(y/2)+1
                arrd2.append([x1,y])
                    
   
     

    list_of_markers=arrd1+arrd2
    for i in list_of_markers:
        e.append(i);
    return e;
        
    
    
    #################################################################################    return list_of_markers

## The findOptimumPath() function returns a python list which consists of all paths that need to be traversed
## in order to start from the START cell and traverse to any one of the markers ( either blue or red ) and then
## traverse to FINISH. The length of path should be shortest ( most optimal solution).
#Function Name: findOptimumPath()
#Input: path1 & path3(path from start to marker1 &marker2 respectively),path2 & path4(path from marker1 & marker2 to end respectively), marker1 & marker2(stores first and second coordinates of e respectively), graph(from buildGraph()), start(from findStartPoint()), endArray(this array appends the shortest path),;image(corresponding to image path),e(array returned from findMarkers)- passed from the main function.
#Output: Returns the shortest path consisting the corresponding marker(s) or in the case of equal paths, the path corresponding to marker nearest to start is returned.
#Logic: To compare total path lengths for makers 1 & 2 and append in endArray or to append shortest path from start to marker 1 or 2 in endArray.
#Example: findOptimumPath(img,e,1)
def findOptimumPath(img,e,size):     ## You can pass your own arguments in this space.
    ############################# Add your Code Here ################################
    graph = buildGraph(img,size)
    start = findStartPoint(img,size)
    pathArray=[]
    end=(0,0)
   
    graph = buildGraph(img,size)
    start = findStartPoint(img,size)
    pathArray=[]
    endArray=[]
    end=(0,0)
    marker1=e[0]
    marker2=e[1]

    path1=findPath(graph,start,marker1,path=[])
    path2=findPath(graph,marker1,end,path=[])
    path3=findPath(graph,start,marker2,path=[])
    path4=findPath(graph,marker2,end,path=[])

    if(len(path1+path2)<len(path3+path4)):
        pathArray=path1+path2
        p1=[];
        p2=[];
        for i in path1:
            my_list=[int(x) for x in i.split(',')]
            
            p1.append((my_list[0],my_list[1]));
        
        for i in path2:
            my_list=[int(x) for x in i.split(',')]
            p2.append((my_list[0],my_list[1]));
        endArray.append(p1);
        endArray.append(p2);          
        
    elif(len(path1+path2)>len(path3+path4)):
        pathArray=path3+path4
        p1=[];
        p2=[];
        for i in path3:
            my_list=[int(x) for x in i.split(',')]
            p1.append((my_list[0],my_list[1]));
        for i in path4:
            my_list=[int(x) for x in i.split(',')]
            p2.append((my_list[0],my_list[1]));
        endArray.append(p1);
        endArray.append(p2);
    else:
        if(path1<path3):
            pathArray=path1+path2
            p1=[];
            p2=[];
            for i in path1:
                my_list=[int(x) for x in i.split(',')]
                p1.append((my_list[0],my_list[1]));
            
            for i in path2:
                my_list=[int(x) for x in i.split(',')]
                p2.append((my_list[0],my_list[1]));
            endArray.append(p1);
            endArray.append(p2);      
        else:
            pathArray=path3+path4
            p1=[];
            p2=[];
            for i in path3:
                my_list=[int(x) for x in i.split(',')]
                p1.append((my_list[0],my_list[1]));
            for i in path4:
                my_list=[int(x) for x in i.split(',')]
                p2.append((my_list[0],my_list[1]));
            endArray.append(p1);
            endArray.append(p2);

    
    
    #################################################################################
    return pathArray,endArray

## The colourPath() function highlights the whole path that needs to be traversed in the maze image and
## returns the final image.
#Function Name: colourPath()
#Input: image, size,shortestPath(shortest path from findOptimumPath)-passed from main.
#Output:  Returns image whiich has the colored shortest path.
#Logic: Split the coordinates form path and pass them in colourCell to obtained the coloured path.
#Example: colourPath(img, 1, shortestPath)
def colourPath(  img,size,shortestPath  ):   ## You can pass your own arguments in this space. 
    ############################# Add your Code Here ################################
    for i in path:               ## Loop to paint the solution path.
        my_list=i.split(",");
        
        img = colourCell(img, my_list[0], my_list[1], size, 230)
   
     

    #################################################################################
    return img

#####################################    Add Utility Functions Here   ###################################
##                                                                                                     ##
##                   You are free to define any functions you want in this space.                      ##
##                             The functions should be properly explained.                             ##




##                                                                                                     ##
##                                                                                                     ##
#########################################################################################################

## This is the main() function for the code, you are not allowed to change any statements in this part of
## the code. You are only allowed to change the arguments supplied in the findMarkers(), findOptimumPath()
## and colourPath() functions.    
#Function Name: main()
#Input: filePath(File path of the maze to be solved.), flag, img(stores the filePath).
#Output: The shortest path is printed and solved image is shown.
#Logic: Predefined logic for execution of the code.
#Example: main("image_00.jpg",flag=0)
def main(filePath, flag = 0):
    img = readImageHSV(filePath)
    imgBinary = readImageBinary(filePath)
    x=0;
    y=0;
    coords=[]
    if len(img) == 440:
        size = 1
    else:
        size = 2
    if size==1:
        for x in xrange(1,5):
            if x<4:
                b=math.pow(2,x-1)
                c=int(b)
                for y in xrange(0,(6*c)):
                    y=y+1;
                    coords.append((x,y))
            if x == 4:
                 
                for y in xrange(0,24):
                    y=y+1;
                    coords.append((x,y))
    if size==2:
        for x in xrange(1,7):
            if x<4:
                b=math.pow(2,x-1)
                c=int(b)
                for y in xrange(0,(6*c)):
                    y=y+1;
                    coords.append((x,y))
            if x == 4:
                 
                for y in xrange(0,24):
                    y=y+1;
                    coords.append((x,y))
            if x == 5:
                for y in xrange(0,24):
                    y=y+1;
                    coords.append((x,y))
            if x == 6:
                for y in xrange(0,48):
                    y=y+1;
                    coords.append((x,y))
            
    e=[];     
    for coordinate in coords:
        e = findMarkers(coordinate[0],coordinate[1],size,filePath,e)
    
    
    shortestPath,toPrintPath = findOptimumPath(imgBinary,e,size)
    for i in shortestPath:               ## Loop to paint the solution path.
        my_list=i.split(",");
        img = colourCell(img, int(my_list[0]), int(my_list[1]), size,230)
   # print toPrintPath
   # print listofMarkers
    if __name__ == "__main__":                    
        return img
    else:
        if flag == 0:
            return toPrintPath
        elif flag == 1:
            return str(listofMarkers) + "\n"
        else:
            return img
    
## The main() function is called here. Specify the filepath of image in the space given.
if __name__ == "__main__":
    for g in range(10):
        filePath = "image_0"+str(g)+".jpg"     ## File path for test image
        
        imgBinary = readImageBinary(filePath)
        img = main(filePath,)           ## Main function call
    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
