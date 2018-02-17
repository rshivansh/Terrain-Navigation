import numpy as np
import cv2

## The readImage function takes a file path as argument and returns image in binary form.
## You can copy the code you wrote for section1.py here.
def readImage(filePath):
    #############  Add your Code here   ###############

    img=cv2.imread(filePath,0)
    _,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    binaryImage=thresh



    ###################################################
    return binaryImage

## The findNeighbours function takes a maze image and row and column coordinates of a cell as input arguments
## and returns a stack consisting of all the neighbours of the cell as output.
## Note :- Neighbour refers to all the adjacent cells one can traverse to from that cell provided only horizontal
## and vertical traversal is allowed.
## You can copy the code you wrote for section1.py here.
def findNeighbours(img,row,column):
    neighbours = []
    #############  Add your Code here   ###############

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


    #print arr+arr1+arr2+arr3
    neighbours=arr+arr1+arr2+arr3
    ###################################################
    return neighbours

def colourCell(img,row,column,colorVal):
    x=int(row);
    y=int(column);
    img[(x+1)*20-20:20*(x+1)-1,(y+1)*20-20:20*(y+1)-1]=int(colorVal)
    #############  Add your Code here   ###############
 

    ###################################################
    return img

##  Function that accepts some arguments from user and returns the graph of the maze image.
def buildGraph(img,breadth,length):  ## You can pass your own arguments in this space.
    graph={}
    i=0;
    
    #############  Add your Code here   ###############
    while(i<breadth):
        j=0;
        while(j<length):
            key= str(i)+','+str(j);
            
            neigh=findNeighbours(img,i,j);
            
            k=0;
            while(k<len(neigh)):
                graph[key]=neigh;
                k+=1;
            j+=1
        i+=1;
    
    return graph;


    ###################################################

    
##  Finds shortest path between two coordinates in the maze. Returns a set of coordinates from initial point
##  to final point.
def findPath(graph, start, end, path=[]):
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


## This is the main function where all other functions are called. It accepts filepath
## of an image as input. You are not allowed to change any code in this function.
def main(filePath, flag = 0):                 
    img = readImage(filePath)      ## Read image with specified filepath.
    print img.shape
    breadth = img.shape[0]/20          ## Breadthwise number of cells
    length = img.shape[1]/20           ## Lengthwise number of cells
    if length == 10:
        initial_point = (0,0)      ## Start coordinates for maze solution
        final_point = (9,9)        ## End coordinates for maze solution    
    else:
        initial_point = (0,0)
        final_point = (19,19)
    
    graph = buildGraph(img,breadth,length)       ## Build graph from maze image. Pass arguments as required.
    
    shortestPath = findPath(graph,initial_point,final_point)  ## Find shortest path. Pass arguments as required.
    print shortestPath             ## Print shortest path to verify
    string = str(shortestPath) + "\n"
    for i in shortestPath:         ## Loop to paint the solution path.
        my_list=i.split(",");
        
        img = colourCell(img, my_list[0], my_list[1], 200)
    if __name__ == '__main__':     ## Return value for main() function.
        return img
    else:
        if flag == 0:
            return string
        else:
            return graph
        
## The main() function is called here. Specify the filepath of image in the space given.            
if __name__ == '__main__':
    filePath = 'maze09.jpg'        ## File path for test image
    img = main(filePath)           ## Main function call
    cv2.imshow('canvas', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




