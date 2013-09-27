#!/usr/bin/python

#http://codekata.pragprog.com/2007/01/kata_two_karate.html
#day 3
def chop(findme, base_list):
    bl_size = len(base_list)
    midway = (bl_size / 2)
    bottom = 0
    top = bl_size
    while bl_size > 0:
        if base_list[midway] > findme:
            top = midway
        elif base_list[midway] < findme:
            bottom = midway
        else:
            return midway
        midway = (top + bottom) / 2
        bl_size = bl_size / 2
    return -1

