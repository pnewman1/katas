#!/usr/bin/python

#http://codekata.pragprog.com/2007/01/kata_two_karate.html
#day 2
def chop(findme, base_list):
		bl_size = len(base_list)
		index_low = 0
		index = bl_size / 2
		index_high = bl_size
		if bl_size == 0:
				return -1

		while base_list[index] != findme:
				if (index == index_low) or (index == index_high):
						return -1
				elif base_list[index] > findme:
						index_high = index
						index = index / 2
				elif base_list[index] < findme:
						index_low = index
						index = (index_high + index) / 2
		
		return index

