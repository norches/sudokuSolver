import numpy as np
import random
import pprint

def pprintN(A):
    if A.ndim==1:
        print(A)
    else:
        w = max([len(str(s)) for s in A]) 
        print(u'\u250c'+u'\u2500'*w+u'\u2510') 
        for AA in A:
            print(' ', end='')
            print('[', end='')
            for i,AAA in enumerate(AA[:-1]):
                w1=max([len(str(s)) for s in A[:,i]])
                print(str(AAA)+' '*(w1-len(str(AAA))+1),end='')
            w1=max([len(str(s)) for s in A[:,-1]])
            print(str(AA[-1])+' '*(w1-len(str(AA[-1]))),end='')
            print(']')
        print(u'\u2514'+u'\u2500'*w+u'\u2518')  

def computeGroup(x):
    if x <= 2:
        return 0
    elif row > 2 and row <= 5:
        return 1
    else:
        return 2

def ThreeD(a, b, c):
    lst = [[ ['#' for col in range(a)] for col in range(b)] for row in range(c)]
    return lst

base=3
squares=ThreeD(1,base,base)
#group squares
for cl in range(0,base):
    col=cl*base
    for rw in range(0,base):
        row = rw*base
        squares[cl][rw]=[[col,row],[col,row+1],[col,row+2],[col+1,row],[col+1,row+1],[col+1,row+2],[col+2,row],[col+2,row+1],[col+2,row+2]]
ary=np.zeros(shape=(base**2,base**2)).astype(int)
numbers=[1,2,3,4,5,6,7,8,9]
indecies=[0,1,2,3,4,5,6,7,8]

reset=True
attempt=1
bestProgress=8

#By Solving empty grid you are essentially generating it
def solveGrid(grid):
    shuffledNumbers=list(range(1,10))
    random.shuffle(shuffledNumbers)
    shuffledX=list(range(9))
    random.shuffle(shuffledX)
    shuffledY=list(range(9))
    random.shuffle(shuffledY)
    def possible(y,x,n):
        for i in range(9):
            if grid[y][i] == n:
                return False
        for i in range(9):
            if grid[i][x] == n:
                return False
        x0=(x//3)*3
        y0=(y//3)*3
        for i in range(3):
            for j in range(3):
                if grid[y0+i][x0+j] == n:
                    return False
        return True

    def solveCell():
        for y in shuffledY:
            for x in shuffledX:
                if grid[y][x] == 0:
                    for n in shuffledNumbers:
                        if possible(y,x,n):
                            grid[y][x] = n
                            solveCell()
                            grid[y][x] = 0
                    return
        pprintN(grid)
        return True
    solveCell()

solveGrid(ary)