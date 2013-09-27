#!/usr/bin/python

#http://codekata.pragprog.com/2007/01/kata_two_karate.html
#day 3

def recurse_list(findme, base_list, low, high):
    index = (high + low) / 2
    if base_list[index] == findme:
        return index
    elif (low == index):
        return -1
    elif (high == index):
        return -1
    elif base_list[index] > findme:
        high = index
        return recurse_list(findme, base_list, low, high)
    elif base_list[index] < findme:
        low = index
        return recurse_list(findme, base_list, low, high)

def chop(findme, base_list):
    bl_size = len(base_list)
    if bl_size == 0:
        return -1
    else:
        result = recurse_list(findme, base_list, 0, bl_size)

    return result

