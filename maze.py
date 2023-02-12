import random
from heapq import heapify, heappush, heappop

class Node:
    def __init__(self, gval, xcoord, ycoord, parent, hval):
        self.gval = gval
        self.hval = hval
        self.fval = gval + hval
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.parent = parent

def make_maze(): 
    rows, cols = (10, 10)
    sampleList = ['0','1']
    arr = [random.choices(
        sampleList, weights=(70,30), k=10) for j in range(rows)]
    arr[0][0] = '0'
    arr[9][9] = '0'
    return arr

def astar(robx, roby, goalx, goaly):
    openList = []
    closedList = {}
    heapify(openList)
    current = Node(0,robx,roby,None, calculateDistance(robx,roby,goalx,goaly))
    while(True):
        if(current.ycoord > 0):
            north = Node(current.gval+1,current.xcoord,current.ycoord-1,current, calculateDistance(current.xcoord,current.ycoord-1,goalx,goaly))
            heappush(openList, (north.fval,north.hval,1, north))
        if(current.ycoord < goaly):
            south = Node(current.gval+1,current.xcoord,current.ycoord+1,current, calculateDistance(current.xcoord,current.ycoord+1,goalx,goaly))
            heappush(openList, (south.fval, south.hval, 2, south))
        if(current.xcoord < goalx):
            east = Node(current.gval+1,current.xcoord+1,current.ycoord,current, calculateDistance(current.xcoord+1,current.ycoord,goalx,goaly))
            heappush(openList, (east.fval, east.hval,3,  east))
        if(current.xcoord > 0):
            west = Node(current.gval+1,current.xcoord-1,current.ycoord,current, calculateDistance(current.xcoord-1,current.ycoord,goalx,goaly))
            heappush(openList, (west.fval, west.hval,4, west))
        tempNode = heappop(openList)[3]
        if(tempNode.hval == 0):
            return closedList
        else:
            if ((tempNode.xcoord, tempNode.ycoord) in closedList):
                if(closedList[(tempNode.xcoord, tempNode.ycoord)].fval > tempNode.fval):
                    closedList[(tempNode.xcoord, tempNode.ycoord)] = tempNode
            else:
                closedList[(tempNode.xcoord, tempNode.ycoord)] = tempNode
            current = tempNode
            continue

def calculateDistance(xval, yval, goalx, goaly):
    return abs(goalx-xval) + abs(goaly-yval)

if __name__ == '__main__':
    exploredList = []
    arr = make_maze()
    closedlist = astar(0,0,9,9)
    for keys in closedlist:
        if(arr[keys[0]][keys[1]] == '1'):
            break
        else:
            arr[keys[0]][keys[1]] = '*'
    for row in arr:
        print(row)