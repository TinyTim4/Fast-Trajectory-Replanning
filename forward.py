import random
from heapq import heapify, heappush, heappop

#Initializes a node which represents a grid point. Each node will contain
#the x y coordinate, its g value, h value, and a pointer to the parent node
class Node:
    def __init__(self, gval, xcoord, ycoord, parent, hval):
        self.gval = gval
        self.hval = hval
        self.fval = gval + hval
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.parent = parent
        self.obs = False
    


def make_maze(lengthx, lengthy): 
    rows, cols = (lengthx, lengthy)
    sampleList = ['0 ','1 ']
    arr = [random.choices(
        sampleList, weights=(80,20), k=lengthx) for j in range(rows)]
    arr[0][0] = '0 '
    arr[lengthx-1][lengthy-1] = '0 '
    return arr


#Runs A* on a specific gridpoint to find the most optimal path to the goal
def astar(robx, roby, goalx, goaly, explored):
    openList = []
    closedList = {}
    heapify(openList)
    current = Node(0,robx,roby,None, calculateDistance(robx,roby,goalx,goaly))
    closedList[(robx, roby)] = current
    while(True):
        if(current.ycoord > 0):
            north = Node(current.gval+1,current.xcoord,current.ycoord-1,current, calculateDistance(current.xcoord,current.ycoord-1,goalx,goaly))
            if((current.xcoord, current.ycoord-1) in explored):
                if(explored[(current.xcoord, current.ycoord-1)] == False):
                    openList = pushHeap(north, openList, lengthx, lengthy)
            else:
                openList = pushHeap(north, openList, lengthx, lengthy)
        if(current.ycoord < goaly):
            south = Node(current.gval+1,current.xcoord,current.ycoord+1,current, calculateDistance(current.xcoord,current.ycoord+1,goalx,goaly))
            if((current.xcoord, current.ycoord+1) in explored):
                if(explored[(current.xcoord, current.ycoord+1)] == False):
                    openList = pushHeap(south, openList, lengthx, lengthy)
            else:
                openList = pushHeap(south, openList, lengthx, lengthy)
        if(current.xcoord < goalx):
            east = Node(current.gval+1,current.xcoord+1,current.ycoord,current, calculateDistance(current.xcoord+1,current.ycoord,goalx,goaly))
            if((current.xcoord+1, current.ycoord) in explored):
                if(explored[(current.xcoord+1, current.ycoord)] == False):
                    openList = pushHeap(east, openList, lengthx, lengthy)
            else:
                openList = pushHeap(east, openList, lengthx, lengthy)
        if(current.xcoord > 0):
            west = Node(current.gval+1,current.xcoord-1,current.ycoord,current, calculateDistance(current.xcoord-1,current.ycoord,goalx,goaly))
            if((current.xcoord-1, current.ycoord) in explored):
                if(explored[(current.xcoord-1, current.ycoord)] == False):
                    openList = pushHeap(west, openList, lengthx, lengthy)
            else:
                openList = pushHeap(west, openList, lengthx, lengthy)
        if(not openList):
            return None
        tempNode = heappop(openList)[4]
        if(tempNode.gval > 10000):
            return None
        if(tempNode.hval == 0):
            closedList[(tempNode.xcoord, tempNode.ycoord)] = tempNode
            return tempNode
        else:
            if ((tempNode.xcoord, tempNode.ycoord) in closedList):
                if(closedList[(tempNode.xcoord, tempNode.ycoord)].fval > tempNode.fval):
                    closedList[(tempNode.xcoord, tempNode.ycoord)] = tempNode
            else:
                closedList[(tempNode.xcoord, tempNode.ycoord)] = tempNode
            current = tempNode
            continue

#Pushes a Node into the open list. If a node with the same x y position is already in it,
#compare the f values and replaes it if it is lower
def pushHeap(node, heap, lengthx, lengthy):
    for element in heap:
        if(element[4].xcoord == node.xcoord and element[4].ycoord == node.ycoord):
            if(element[4].fval > node.fval):
                element[4].fval = node.fval
            return heap
    heappush(heap, (node.fval, -node.gval,lengthx-node.xcoord, lengthy-node.ycoord, node))
    return heap

#Calculates the h value of each node, which would be the Manhattan distance
def calculateDistance(xval, yval, goalx, goaly):
    return abs(goalx-xval) + abs(goaly-yval)

#When travelling throught the grid, keep track of the properties of the neighbors and
#check whether or not it has an obstacle or not
def addNeighbors(node, exploredList, arr, lengthx, lengthy):
    x = node.xcoord
    y = node.ycoord
    if(node.ycoord > 0 and not((x,y-1) in exploredList)):
        if(arr[x][y-1] == '1 '):
            exploredList[(x,y-1)] = True
        else:
            exploredList[(x,y-1)] = False
    if(node.ycoord < lengthy and not((x,y+1) in exploredList)):
        if(arr[x][y+1] == '1 '):
            exploredList[(x,y+1)] = True
        else:
            exploredList[(x,y+1)] = False
    if(node.xcoord < lengthx and not((x+1,y) in exploredList)):
        if(arr[x+1][y] == '1 '):
            exploredList[(x+1,y)] = True
        else:
            exploredList[(x+1,y)] = False
    if(node.xcoord > 0 and not((x-1,y) in exploredList)):
        if(arr[x-1][y] == '1 '):
            exploredList[(x-1,y)] = True
        else:
            exploredList[(x-1,y)] = False


#Main function
if __name__ == '__main__':
    exploredList = {}
    arr = make_maze(101,101)
    currentx, currenty = (0,0)
    (x,y) = (0,0)
    ansFile = open('outputForward.txt', 'w')
    lengthx, lengthy = (100,100)
    while(x != lengthx or y != lengthy):
        for row in arr:
            ansFile.writelines(row)
            ansFile.write("\n")
        ansFile.write("\n")
        finalNode = astar(currentx,currenty,lengthx,lengthy,exploredList)
        if(finalNode == None):
            ansFile.write("No Solution \n")
            break
        hval = finalNode.hval
        gval = finalNode.gval
        path = []
        while(finalNode):
            path.append(finalNode)
            finalNode = finalNode.parent
        while(path):
            tempNode = path.pop()
            (x,y) = (tempNode.xcoord, tempNode.ycoord)
            current = Node(0,x,y,None,calculateDistance(x,y,lengthx, lengthy))
            if(arr[x][y] == '1 '):
                tup = (x,y)
                exploredList[tup] = True
                currentx = tempNode.parent.xcoord
                currenty = tempNode.parent.ycoord
                break
            else:
                exploredList[(x,y)] = False
                addNeighbors(current,exploredList,arr, lengthx, lengthy)
                arr[x][y] = '* '
    for row in arr:
        ansFile.writelines(row)
        ansFile.write("\n")       
        