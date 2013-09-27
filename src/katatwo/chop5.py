#!/usr/bin/python

#http://codekata.pragprog.com/2007/01/kata_two_karate.html
#day 4
def chop(findme, base_list):
    bl_size = len(base_list)
    index = bl_size
    const = bl_size

    f = lambda x, i, u: int(x * float(float(u)/float(i)))
    units = 1
    i = 2
    while bl_size > 0:
        index = f(const, i, units)
        if base_list[index] == findme:
            return index
        elif base_list[index] > findme:
            addme = -1
        elif base_list[index] < findme:
            addme = 1
        i = i*2
        units = (units*2) + addme
        bl_size = bl_size / 2
    return -1
