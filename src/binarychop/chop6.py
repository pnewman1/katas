#!/usr/bin/python
import math

#http://codekata.pragprog.com/2007/01/kata_two_karate.html
#day 5
def chop(findme, base_list):
    bl_size = len(base_list)

    f = lambda x, i, u: int(math.floor(x * float(float(u)/float(2**i))))

    i = 1 #iterations
    u = 1
    if bl_size == 0:
        return -1
    elif bl_size == 1:
        max_iterations = 1
    else:
        max_iterations = int(math.ceil(bl_size / 2))

    for i in range (i, max_iterations+2):
        index = f(bl_size, i, u)
        if base_list[index] == findme:
            return index
        elif base_list[index] > findme:
            q = -1
        elif base_list[index] < findme:
            q = 1
        u = (u*2) + q
        
    return -1

