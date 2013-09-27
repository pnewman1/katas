#!/usr/bin/python

#http://codekata.pragprog.com/2007/01/kata_two_karate.html
#day 1
def chop(findme, base_list):
		bl_size = len(base_list)
		index = bl_size / 2
		if bl_size == 0:
				return -1

		loops = 0
		while base_list[index] != findme:
				if index == 0:
						return -1
				elif index == bl_size:
						return -1
				#brute force, there must be a better way
				elif loops > bl_size:
						return -1
				elif base_list[index] > findme:
						#print "greater"
						index = index / 2
				elif base_list[index] < findme:
						#print "less"
						index = (bl_size + index ) / 2
				loops+=1
		
		return index

