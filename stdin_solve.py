from sys import stdin
from re import findall
from itertools import chain

def findNext(grid, i, j):
    for x in range(i,9):
        for y in range(j,9):
            if grid[x][y] == 0:
                return x,y
    for x in range(0,9):
        for y in range(0,9):
            if grid[x][y] == 0:
                return x,y
    return -1,-1

def isValid(grid, i, j, e):
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(9)])
        if columnOk:
            secTopX, secTopY = 3 *(i//3), 3 *(j//3)
            for x in range(secTopX, secTopX+3):
                for y in range(secTopY, secTopY+3):
                    if grid[x][y] == e:
                        return False
            return True
    return False

def solve(grid, i=0, j=0):
    i,j = findNext(grid, i, j)
    if i == -1:
        return True
    for e in range(1,10):
        if isValid(grid,i,j,e):
            grid[i][j] = e
            if solve(grid, i, j):
                return True
            grid[i][j] = 0
    return False

#main
def main():
    data,d=[],[]
    for i in stdin:
             for s in findall(r'\d',i):d.append(s)
    d=list(map(int,d))
    for i in range(0,9):
        data.append(list(map(int, d[i*9:9+i*9])))
    if len(list(chain.from_iterable(data)))!=81:
        print("[-]This input isn't adequate for solving.")
        print("[-]this input may not include 81 numbers(0~9).")
        print("[-]Note: 0 equals a blank cell.")
        exit()
    if solve(data):
        for i in data:print(i)
    else:
        print("[-]Couldn't solve...")
        print("[-]this input may not include 81 numbers(0~9).")
        print("[-]Note: 0 equals a blank cell.")
        print("[-]Or, not be able to solve.")
try:
    main()
except KeyboardInterrupt:
    print("[-]Interrupted!")
    exit()
