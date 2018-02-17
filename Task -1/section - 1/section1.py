import numpy as np
import cv2

## The readImage function takes a file path as argument and returns image in binary form.
def readImage(filePath):
    img=cv2.imread(filePath,0)
    _,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    binaryImage=thresh
    ###################################################
    return binaryImage

## The findNeighbours function takes a maze image and row and column coordinates of a cell as input arguments
## and returns a stack consisting of all the neighbours of the cell as output.
## Note :- Neighbour refers to all the adjacent cells one can traverse to from that cell provided only horizontal
## and vertical traversal is allowed.
def findNeighbours(img,row,column):
    neighbours = []
    arr=[]
    arr1=[]
    arr2=[]
    arr3=[]
    x =row;
    y =column;
    aa=0;
    
    if img[(x+1)*20-1,(y+1)*20-11] == 0 or img[(x+1)*20-1,(y+1)*20-11]== 1 or img[(x+1)*20-1,(y+1)*20-11] == 2:
        aa=1;
    elif img[(x+1)*20-1,(y+1)*20-11] == 253 or img[(x+1)*20-1,(y+1)*20-11] == 254 or img[(x+1)*20-1,(y+1)*20-11] == 255:
        aa=1;
        arr.append([])
        arr[0].append(x+1)
        arr[0].append(y)
    

    if img[(x+1)*20-11,(y+1)*20-1] == 0 or img[(x+1)*20-11,(y+1)*20-1] == 1 or img[(x+1)*20-11,(y+1)*20-1] == 2:
        aa=1;
    elif img[(x+1)*20-11,(y+1)*20-1] == 253 or img[(x+1)*20-11,(y+1)*20-1] == 254 or img[(x+1)*20-11,(y+1)*20-1] == 255:
        aa=1;
        arr1.append([])
        arr1[0].append(x)
        arr1[0].append(y+1)

    if img[(x+1)*20-21,(y+1)*20-11] == 0 or img[(x+1)*20-21,(y+1)*20-11] == 1 or img[(x+1)*20-21,(y+1)*20-11] == 2:
        aa=1;
    elif img[(x+1)*20-21,(y+1)*20-11] == 253 or img[(x+1)*20-21,(y+1)*20-11] == 254 or img[(x+1)*20-21,(y+1)*20-11] == 255:
        aa=1;
        arr2.append([])
        arr2[0].append(x-1)
        arr2[0].append(y)

    if img[(x+1)*20-11,(y+1)*20-21] == 0 or img[(x+1)*20-11,(y+1)*20-21] == 1 or img[(x+1)*20-11,(y+1)*20-21] == 2:
        aa=1;
    elif img[(x+1)*20-11,(y+1)*20-21] == 253 or img[(x+1)*20-11,(y+1)*20-21] == 254 or img[(x+1)*20-11,(y+1)*20-21] == 255:
        aa=1;
        arr3.append([])
        arr3[0].append(x)
        arr3[0].append(y-1)

    neighbours=arr+arr1+arr2+arr3
    
    ###################################################
    return neighbours

##  colourCell function takes 4 arguments:-
##            img - input image
##            row - row coordinates of cell to be coloured
##            column - column coordinates of cell to be coloured
##            colourVal - the intensity of the colour.
##  colourCell basically highlights the given cell by painting it with the given colourVal. Care should be taken that
##  the function doesn't paint over the    walls and only paints the empty spaces. This function returns the image
##  with the painted cell.
def colourCell(img,row,column,colorVal):
    x=row;
    y=column;
    img[(x+1)*20-20:20*(x+1)-1,(y+1)*20-20:20*(y+1)-1]=colorVal
    #############  Add your Code here   ###############
 

    ###################################################
    return img

##  Main function takes the filepath of image as input.
##  You are not allowed to change any code in this function.
def main(filePath):
    img = readImage(filePath)
    coords = [(0,0),(9,9),(3,2),(4,7),(8,6)]
    string = ""
    for coordinate in coords:
        img = colourCell(img, coordinate[0], coordinate[1], 150)
        neighbours = findNeighbours(img, coordinate[0], coordinate[1])
        string = string + str(neighbours) + "\n"
        for k in neighbours:
            img = colourCell(img, k[0], k[1], 230)
    if __name__ == '__main__':
        return img
    else:
        return string + "\t"
## Specify filepath of image here. The main function is called in this section.
if __name__ == '__main__':
    filePath ='maze00.jpg'
    img = main(filePath)
    cv2.imshow('canvas', img)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()
