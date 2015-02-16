#!/usr/bin/python

#fizzbuzz

for i in range(1,101):
  if (i % 3 == 0) and (i % 5 == 0):
    print i
    print "FizzBuzz!"
  elif (i % 3 == 0):
    print i
    print "Fizz"
  elif (i % 5 == 0):
    print i
    print "Buzz"


