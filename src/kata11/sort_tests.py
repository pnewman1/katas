#!/usr/bin/python
import sort
import unittest

#http://codekata.com/kata/kata11-sorting-it-out/

class sort_tests(unittest.TestCase):
  def test_sort(self):
    self.assertEqual("aaaaabbbbcccdeeeeeghhhiiiiklllllllmnnnnooopprsssstttuuvwyyyy", sort.sort("When not studying nuclear physics, Bambi likes to play beach volleyball."))

def main():
  unittest.main()

if __name__ == '__main__':
  main()
