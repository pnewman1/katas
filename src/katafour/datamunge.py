#!/usr/bin/python
import sys

#http://codekata.pragprog.com/2007/01/kata_four_data_.html

def find_smallest(data):

    smallest_value = None
    smallest_item_name = None

    for d in data:
        tmp = data[d][0] - data[d][1]
        if smallest_value == None:
            smallest_value = tmp
            smallest_item_name = d
        elif tmp < smallest_value:
            smallest_value = tmp
            smallest_item_name = d
    return smallest_item_name, smallest_value

def process_file(filename, field_title, value1, value2):
    #open a file and create a hash from its contents
    #assumes the file is in the directory we're running the script from

    try:
        f = open(filename, "r")
    except e:
        print e

    bool = 0
    data = {}
    smallest_value = None
    smallest_item_name = None

    for line in f:
        if line.strip() == "<pre>":
            bool = 1
        elif line.strip() == "</pre>":
            bool = 0

        if bool == 1 and line.strip() != "<pre>":
            l = line.split()
            if (len(l) >= value2):
                #todo: strip non-numeric characters
                try:
                    v1 = float(l[value1])
                    v2 = float(l[value2])
                    tmp = v1 - v2
                    if (smallest_value == None) or (tmp < smallest_value):
                        smallest_value = tmp
                        smallest_item_name = l[field_title]
                    data[l[field_title]] = [v1, v2]
                except:
                    pass

    f.close()
   
    return smallest_item_name, smallest_value

args = sys.argv

#weather.dat == ./datamunge.py weather.dat 0 1 2
#football.dat == ./datamunge.py football.dat 1 6 8

#data = process_file(args[1], 0, 1, 2)
data = process_file(args[1], int(args[2]), int(args[3]), int(args[4]))
print data
