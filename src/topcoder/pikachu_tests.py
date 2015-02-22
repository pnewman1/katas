#!/usr/bin/env python

from PikachuEasy import PikachuEasy
import unittest

class pikachu_tests:
  def setUp(self):
    self.p = PikachuEasy

  def p_tests(self):
    self.assertEqual("YES", self.PikachuEasy.check("pikapi"))
    self.assertEqual("YES", self.PikachuEasy.check("pipikachu"))
    self.assertEqual("YES", self.PikachuEasy.check("chupikachupipichu"))
    self.assertEqual("NO", self.PikachuEasy.check("pikaqiu"))
    self.assertEqual("NO", self.PikachuEasy.check("topcoder"))
    self.assertEqual("NO", self.PikachuEasy.check("pikapipachu"))
    self.assertEqual("NO", self.PikachuEasy.check("pikap"))

def main():
  unittest.main()

if __name__ == '__main__':
  main()
