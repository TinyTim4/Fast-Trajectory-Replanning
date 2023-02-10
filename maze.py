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

"""
Some ideas
----------
boolean obstacle for node
Nnode = roby + 1
Snode = roby - 1
Enode = robx + 1
Wnode = robx - 1

We need to tweak this code below:
The code below compares all of the nodes. Either the node is an obstacle or it does not have the smallest fval.
We should first check if the node is a node we explored before.
Then, we should compare the nodes
Then, we should determine if the node we want to go to is an obstacle.


if Nnode.fval < Enode.fval and Nnode.fval < Snode.fval and Nnode.fval < Wnode.fval and Nnode.obs == False:
    roby = roby + 1
// Either Nnode is not the optimal path or it is an obstacle
else if Snode.fval < Enode.fval and Snode.fval < Wnode.fval and Snode.obs ==  False:
    roby = roby - 1
//Either Snode is not the optimal path or it is an obstacle
else if Enode.fval < Wnode.fval and Enode.obs == False:
    robx = robx + 1
// Either Enode is an obstacle or is not the optimal path
else if Wnode.fval  == False:
    robx = robx - 1
else 
"""
        
def make_maze(): 
    rows, cols = (10, 10)
    sampleList = [0,1]
    arr = [random.choices(
        sampleList, weights=(70,30), k=10) for j in range(rows)]
    arr[0][0] = 0
    arr[9][9] = 0
    return arr

def astar(robx, roby, goalx, goaly):
    g = 0
    openList = []
    closedList = {}
    heapify(openList)
    current = Node(g,robx,roby,None, calculateDistance(robx,roby,goalx,goaly))
    while(True):
        g = g+1
        if(roby < 9):
            north = Node(g,current.xcoord,current.ycoord+1,current, calculateDistance(current.xcoord,current.ycoord+1,goalx,goaly))
            heappush(openList, (north.fval, north))
        if(roby > 0):
            south = Node(g,current.xcoord,current.ycoord-1,current, calculateDistance(current.xcoord,current.ycoord-1,goalx,goaly))
            heappush(openList, (south.fval, south))
        if(robx < 9):
            east = Node(g,current.xcoord+1,current.ycoord,current, calculateDistance(current.xcoord+1,current.ycoord,goalx,goaly))
            heappush(openList, (east.fval, east))
        if(robx > 0):
            west = Node(g,current.xcoord-1,current.ycoord,current, calculateDistance(current.xcoord-1,current.ycoord,goalx,goaly))
            heappush(openList, (west.fval, west))
        tempNode = heappop(openList)
        if(tempNode.hval == 0):
            return closedList
        else:
            if((tempNode.xcoord, tempNode.ycoord) in closedList): 
                if(closedList.get(tempNode.xcoord, tempNode.ycoord).fval > closedList.fval):
                    closedList.get(tempNode.xcoord, tempNode.ycoord).fval = closedList.fval
            else:
                closedList[(tempNode.xcoord, tempNode.ycoord)] = tempNode
            current = tempNode
            continue

def calculateDistance(xval, yval, goalx, goaly):
    return abs(goalx-xval) + abs(goaly-yval)

if __name__ == '__main__':
    arr = make_maze()
    closedlist = astar(0,0,9,9)
    for row in arr:
        print(row)
    print(closedlist)
