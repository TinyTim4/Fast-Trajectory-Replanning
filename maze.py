import random
from heapq import heapify, heappush, heappop

class Node:
    def __init__(self, gval, xcoord, ycoord, parent = None, hval = 99999):
        self.gval = gval
        self.hval = hval
        self.fval = gval + hval
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.parent = parent

def make_maze(): 
    rows, cols = (10, 10)
    sampleList = [0,1]
    arr = [random.choices(
        sampleList, weights=(70,30), k=10) for j in range(rows)]
    arr[0][0] = 0
    arr[9][9] = 0
    return arr

def astar(robx, roby, goalx, goaly):
    x = 0
    openList = []
    heapify(openList)
    current = Node(x, calculateDistance(robx,roby,goalx,goaly),robx,roby)
    while(True):
        north,south,east,west = Node()
        x = x+1
        if(roby < 9):
            north = Node(x,current.xcoord,current.ycoord+1,current, calculateDistance(current.xcoord,current.ycoord+1,goalx,goaly))
        if(roby > 0):
            south = Node(x,current.xcoord,current.ycoord-1,current, calculateDistance(current.xcoord,current.ycoord-1,goalx,goaly))
        if(robx < 9):
            east = Node(x,current.xcoord+1,current.ycoord,current, calculateDistance(current.xcoord+1,current.ycoord,goalx,goaly))
        if(robx > 0):
            west = Node(x,current.xcoord-1,current.ycoord,current, calculateDistance(current.xcoord-1,current.ycoord,goalx,goaly))
        heappush(openList, (north.fval, north))
        heappush(openList, (south.fval, south))
        heappush(openList, (east.fval, east))
        heappush(openList, (west.fval, west))
        tempNode = heappop(openList)
        if(tempNode.hval == 0):
            break
        else:
            current = tempNode
            continue
    return 0

def calculateDistance(xval, yval, goalx, goaly):
    return abs(goalx-xval) + abs(goaly-yval)

if __name__ == '__main__':
    arr = make_maze()
    robx, roby = (0,0)
    for row in arr:
        print(row)