#!/usr/bin/python
from JumpFurther import JumpFurther
import unittest

#http://codekata.pragprog.com/2007/01/kata_two_karate.html

class jiro_tests(unittest.TestCase):

    def setUp(self):
        self.j = JumpFurther()

    def test_jiro(self):
        self.assertEqual(3, self.j.furthest(2, 2))
	self.assertEqual(2, self.j.furthest(2, 1))
        self.assertEqual(5, self.j.furthest(3, 3))
        self.assertEqual(862641, self.j.furthest(1313, 5858))
        self.assertEqual(1, self.j.furthest(1, 757065))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
