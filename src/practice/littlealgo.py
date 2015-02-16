#!/usr/bin/python

#hashes thing
#this showed up in an interview I had a few years ago.
#given an array of numbers, see if there's another number in the array that adds up to 100

numbers = [1, 10, 20, 30, 32, 33, 45, 49, 50, 50, 52, 55, 60, 67, 70, 99]
combos = {}

#build a hash of the number in the array
for n in numbers:
  combos[n] = "notfound"

#iterate over the list again, looking for matches
for n in numbers:
  match = 100 - n
  if match in combos:
     combos[match] = n

for c in combos:
  if combos[c] == "notfound":
    pass
  else:
    print c, ":", combos[c]


