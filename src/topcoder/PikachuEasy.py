#!/usr/bin/env python

#PikachuEasy
#http://community.topcoder.com/stat?c=problem_statement&pm=11783

class PikachuEasy:

  def check(self, str1):
    str1 = str1.replace("pi", "") 
    str1 = str1.replace("ka", "")
    str1 = str1.replace("chu", "")

    if str1 == "":
      return "YES"
    else:
      return "NO"

