#!/usr/bin/env python

import sys

def readKnapsack(fileKnapsack):
    kFile = open(fileKnapsack,'r')
    line = kFile.readline()
    line = line.strip()
    columns = line.split()
    C, count =int(columns[0]), int(columns[1])
    print("Number of items: ", count)
    print("Knapsack capacity: ", C)

    # Pre-allocate vectors v and w
    v = [0]*count
    w = [0]*count
    
    i=0
    for line in kFile:
        line=line.strip()
        columns = line.split()
        v[i], w[i] = int(columns[0]), int(columns[1])
        i+=1

    return v, w, C        
		
def knapsack(v, w, C):
    P = {}                                      # memoezation - save values at (i, x) already visited (acts like a sparse array)
    def recurse(i, x):                          # recursive implementation of knapsack algorithm
        if (i, x) not in P:                     # if there is a value at (i,x) do not recurse
            if i == 0:                      
                P[i,x] = 0                      
            elif w[i-1] > x:                    # if weight greater than current capacity level (x), save previous value
                P[i,x] = recurse(i-1,x)
            else:                               # save max of [previous value] or [value at current capacity - weight + current value]
                P[i,x] = max(recurse(i-1,x),
                             recurse(i-1,x-w[i-1]) +
                             v[i-1])

        return P[i,x]

    return recurse(len(v),C)

def main():
    sys.setrecursionlimit(5000)                 # increase recursion depth - default is 1500
    v, w, C = readKnapsack("Knapsack2.txt")
    maxValue = knapsack(v, w, C)
    print("Maximum Knapsak Value: ", maxValue)
    
if __name__ == '__main__':
    main()
