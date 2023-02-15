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
        self.obs = False


def make_maze(): 
    rows, cols = (10, 10)
    sampleList = ['0','1']
    arr = [random.choices(
        sampleList, weights=(70,30), k=10) for j in range(rows)]
    arr[0][9] = '0'
    arr[9][9] = '0'
    return arr

def astar(robx, roby, goalx, goaly, explored):
    openList = []
    closedList = {}
    heapify(openList)
    current = Node(0,robx,roby,None, calculateDistance(robx,roby,goalx,goaly))
    while(True):
        if(current.ycoord > 0):
            north = Node(current.gval+1,current.xcoord,current.ycoord-1,current, calculateDistance(current.xcoord,current.ycoord-1,goalx,goaly))
            if((current.xcoord, current.ycoord-1) in explored):
                if(explored[(current.xcoord, current.ycoord-1)] == False):
                    openList = pushHeap(north, openList)
            else:
                openList = pushHeap(north, openList)
        if(current.ycoord < goaly):
            south = Node(current.gval+1,current.xcoord,current.ycoord+1,current, calculateDistance(current.xcoord,current.ycoord+1,goalx,goaly))
            if((current.xcoord, current.ycoord+1) in explored):
                if(explored[(current.xcoord, current.ycoord+1)] == False):
                    openList = pushHeap(south, openList)
            else:
                openList = pushHeap(south, openList)
        if(current.xcoord < goalx):
            east = Node(current.gval+1,current.xcoord+1,current.ycoord,current, calculateDistance(current.xcoord+1,current.ycoord,goalx,goaly))
            if((current.xcoord+1, current.ycoord) in explored):
                if(explored[(current.xcoord+1, current.ycoord)] == False):
                    openList = pushHeap(east, openList)
            else:
                openList = pushHeap(east, openList)
        if(current.xcoord > 0):
            west = Node(current.gval+1,current.xcoord-1,current.ycoord,current, calculateDistance(current.xcoord-1,current.ycoord,goalx,goaly))
            if((current.xcoord-1, current.ycoord) in explored):
                if(explored[(current.xcoord-1, current.ycoord)] == False):
                    openList = pushHeap(west, openList)
            else:
                openList = pushHeap(west, openList)
        if(not openList):
            return {}
        tempNode = heappop(openList)[4]
        if(tempNode.gval > 100):
            return {}
        if(tempNode.hval == 0):
            closedList[(tempNode.xcoord, tempNode.ycoord)] = tempNode
            return closedList
        else:
            if ((tempNode.xcoord, tempNode.ycoord) in closedList):
                if(closedList[(tempNode.xcoord, tempNode.ycoord)].fval > tempNode.fval):
                    closedList[(tempNode.xcoord, tempNode.ycoord)] = tempNode
            else:
                closedList[(tempNode.xcoord, tempNode.ycoord)] = tempNode
            current = tempNode
            continue

def pushHeap(node, heap):
    for element in heap:
        if(element[4].xcoord == node.xcoord and element[4].ycoord == node.ycoord):
            if(element[4].fval > node.fval):
                element[4].fval = node.fval
            return heap
    heappush(heap, (node.fval, 9-node.gval,9-node.xcoord, 9-node.ycoord, node))
    return heap

def calculateDistance(xval, yval, goalx, goaly):
    return abs(goalx-xval) + abs(goaly-yval)

def addNeighbors(node, exploredList, arr):
    x = node.xcoord
    y = node.ycoord
    if(node.ycoord > 0 and not((x,y-1) in exploredList)):
        if(arr[x][y-1] == '1'):
            exploredList[(x,y-1)] = True
        else:
            exploredList[(x,y-1)] = False
    if(node.ycoord < 9 and not((x,y+1) in exploredList)):
        if(arr[x][y+1] == '1'):
            exploredList[(x,y+1)] = True
        else:
            exploredList[(x,y+1)] = False
    if(node.xcoord < 9 and not((x+1,y) in exploredList)):
        if(arr[x+1][y] == '1'):
            exploredList[(x+1,y)] = True
        else:
            exploredList[(x+1,y)] = False
    if(node.xcoord > 0 and not((x-1,y) in exploredList)):
        if(arr[x-1][y] == '1'):
            exploredList[(x-1,y)] = True
        else:
            exploredList[(x-1,y)] = False

        


if __name__ == '__main__':
    exploredList = {}
    arr = make_maze()
    currentx, currenty = (0,9)
    (x,y) = (0,0)
    while(x != 9 or y != 9):
        for row in arr:
                print(row)
        print("\n")
        closedlist = astar(currentx,currenty,9,9,exploredList)
        if(len(closedlist) <= 1):
            print("No Solution")
            break
        for keys in closedlist:
            (x,y) = (keys[0], keys[1])
            current = Node(0,keys[0],keys[1],None,calculateDistance(keys[0],keys[1],9,9))
            if(arr[keys[0]][keys[1]] == '1'):
                tup = (keys[0],keys[1])
                exploredList[(keys[0],keys[1])] = True
                currentx = closedlist[tup].parent.xcoord
                currenty = closedlist[tup].parent.ycoord
                break
            else:
                exploredList[(keys[0],keys[1])] = False
                addNeighbors(current,exploredList,arr)
                arr[keys[0]][keys[1]] = '*'
            (x,y) = (keys[0], keys[1])
    for row in arr:
        print(row)
    print("\n")        
        