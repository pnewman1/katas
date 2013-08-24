#!/usr/bin/python

#http://codekata.pragprog.com/2007/01/kata_two_karate.html
#day 3
def chop(findme, base_list):
    bl_size = len(base_list)
    midway = (bl_size / 2)
    while bl_size > 0:
        if base_list[midway] > findme:
            midway = midway / 2
        elif base_list[midway] < findme:
            midway = (midway + len(base_list)) / 2
        else:
            return midway
        bl_size = bl_size / 2
    return -1

