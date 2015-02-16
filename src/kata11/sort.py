#!/usr/bin/python

import re

# http://codekata.com/kata/kata11-sorting-it-out/

def sort(string):

  #sanitize input, convert to array
  string = string.lower()
  p = re.compile(r'[\W]')
  string = re.sub(p, "", string)
  string = string.replace(" ", "")
  stringlist = list(string)
  print len(stringlist)

  #insertion sort
  for i in range(0, len(stringlist)):
    #store the current character
    x = stringlist[i]
    #iterate backwards from the index poin
    j = i
    while (j > 0) and (stringlist[j-1] > x):
      stringlist[j] = stringlist[j-1]
      j=j-1
    stringlist[j] = x

  return ''.join(stringlist)

#string = "When not studying nuclear physics, Bambi likes to play beach volleyball."
#sort(string)
