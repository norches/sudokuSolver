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
shuffledRows=random.sample(indecies, len(numbers))
shuffledColumns=random.sample(indecies, len(numbers))

reset=True
attempt=1
bestProgress=8

def generateValidGrid():
    global reset
    global attempt
    global bestProgress
    global ary
    ary=np.zeros(shape=(base**2,base**2)).astype(int)
    print("attempt #{}".format(attempt))
    print("bestProgress:{}/81".format(bestProgress))
    reset=False


    attempt+=1
    currentProgress=0
    #populate rest rows
    for column in shuffledColumns:       
        for row in shuffledRows:
            #starting at second row
            possibleNumbers = numbers.copy()
            #remove impossible numbers for this column row square position
            if bestProgress < currentProgress:
                    bestProgress = currentProgress
            for n in range(0,9):
                #check rows and columns
                if ary[row][n] in possibleNumbers:
                    possibleNumbers.remove(ary[row][n])
                if ary[n][column] in possibleNumbers:
                    possibleNumbers.remove(ary[n][column])
            sqRow=computeGroup(row)
            sqColumn=computeGroup(column)
            
            for cell in squares[sqRow][sqColumn]:
                if ary[cell[0]][cell[1]] in possibleNumbers:
                    possibleNumbers.remove(ary[cell[0]][cell[1]])
            if not possibleNumbers:
                reset=True
                break
            else:
                ary[row][column]=random.choice(possibleNumbers)
            currentProgress+=1
        if reset==True:
            break
    else:
        reset=False
while reset==True:
    generateValidGrid()
pprintN(ary)