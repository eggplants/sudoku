#https://stackoverflow.com/questions/1697334/algorithm-for-solving-sudoku
from time import time
from re import search
from re import findall
from sys import argv
from os.path import isfile
print("""\
#########################################################################
#########################################################################
 ____  _   _ ____   ___  _  ___   _   ____   ___  _ __     _______ ____
/ ___|| | | |  _ \\ / _ \\| |/ / | | | / ___| / _ \\| |\\ \\   / / ____|  _ \\
\\___ \\| | | | | | | | | | ' /| | | | \\___ \\| | | | | \\ \\ / /|  _| | |_) |
 ___) | |_| | |_| | |_| | . \\| |_| |  ___) | |_| | |__\\ V / | |___|  _ <
|____/ \\___/|____/ \\___/|_|\\_\\\\___/  |____/ \\___/|_____\\_/  |_____|_| \\_\\
#########################################################################
#########################################################################""")
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

def inputFromStdin(data):
    print("[+]Plz input data.(9 sudoku rows)")
    print("[+]Ex.) 607500100 (Here, 0 is a blank cell.)")
    for i in range(1,10):
        while True:
            d=input()
            if len(d)==9 and search(r"\d{9}",d):
                data.append(list(map(int, list(d))))
                if i!=9:
                    print("[+]%d:OK, Next."%i)
                else:
                    print("[+]%d:OK\n[-]Now, solving..."%i)
                break
            else:
                print("[-]%d:NG, retry."%i)

def inputFromFile(data):
    while True:
        file=""
        if len(argv)==2:
            file=argv[1]
        if file=="":
            print("[+]Input file path :",end="")
            file=input()
            if isfile(file):
                break
            else:
                print("[-]%s is not found or an invalid file."%file)
        else:
            break

    file = open(file, "r")
    d=findall(r'\d',file.read())
    if len(d)==81:
        for i in range(0,9):
            data.append(list(map(int, d[i*9:9+i*9])))

#main
def main():
    try:
        while True:
            data=[]
            print("[+]To close, do ctrl+c.")
            print("[+]Plz select an input method.\n[+]1: stdin or 2: file")
            select=input()
            while True:
                if not select in ["1","2"]:
                    print("[-]Invalid input.")
                    print("[+]Plz input method.\n[+]1: stdin or 2: file")
                    select=input()
                else:
                    break

            if select=="1":
                inputFromStdin(data)
            else:
                inputFromFile(data)
            start_time=time()
            if solve(data):
                print("[+]Solved!!!: %fsec."%(time()-start_time))
                for i in data:print(i)
            else:
                print("[-]Unsolved...")
    except KeyboardInterrupt:
        print("                             ",end="")
        print("\r[-]Close?:[y],n ",end="")
        if input()!="n":
            exit()
        else:
            main()
main()
