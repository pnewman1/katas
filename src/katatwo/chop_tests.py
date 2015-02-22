#!/usr/bin/python
import chop3 as chop
import unittest

#http://codekata.pragprog.com/2007/01/kata_two_karate.html

class chop_tests(unittest.TestCase):
		def test_chop(self):
				self.assertEqual(-1, chop.chop(3, []))
				self.assertEqual(-1, chop.chop(3, [1]))
				self.assertEqual(0, chop.chop(1, [1]))

				self.assertEqual(0, chop.chop(1, [1, 3, 5]))
				self.assertEqual(1, chop.chop(3, [1, 3, 5]))
				self.assertEqual(2, chop.chop(5, [1, 3, 5]))
				self.assertEqual(-1, chop.chop(0, [1, 3, 5]))
				self.assertEqual(-1, chop.chop(2, [1, 3, 5]))
				self.assertEqual(-1, chop.chop(4, [1, 3, 5]))
				self.assertEqual(-1, chop.chop(6, [1, 3, 5]))

				self.assertEqual(0, chop.chop(1, [1, 3, 5, 7]))
				self.assertEqual(1, chop.chop(3, [1, 3, 5, 7]))
				self.assertEqual(2, chop.chop(5, [1, 3, 5, 7]))
				self.assertEqual(3, chop.chop(7, [1, 3, 5, 7]))
				self.assertEqual(-1, chop.chop(0, [1, 3, 5, 7]))
				self.assertEqual(-1, chop.chop(2, [1, 3, 5, 7]))
				self.assertEqual(-1, chop.chop(4, [1, 3, 5, 7]))
				self.assertEqual(-1, chop.chop(6, [1, 3, 5, 7]))
				self.assertEqual(-1, chop.chop(8, [1, 3, 5, 7]))
				self.assertEqual(4, chop.chop(6, [0, 2, 4, 5, 6, 9, 12, 14, 15, 18, 20]))
				self.assertEqual(7, chop.chop(14, [0, 2, 4, 5, 6, 9, 12, 14, 15, 18, 20]))
				self.assertEqual(8, chop.chop(15, [0, 2, 4, 5, 6, 9, 12, 14, 15, 18, 20]))
				self.assertEqual(0, chop.chop(0, [0, 2, 4, 5, 6, 9, 12, 14, 15, 18, 20]))
				self.assertEqual(10, chop.chop(20, [0, 2, 4, 5, 6, 9, 12, 14, 15, 18, 20]))
				self.assertEqual(-1, chop.chop(19, [0, 2, 4, 5, 6, 9, 12, 14, 15, 18, 20]))

				arr = []
				for i in range(60, 100000):
						arr.append(i)
				self.assertEqual(8, chop.chop(68, arr))

def main():
		unittest.main()

if __name__ == '__main__':
		main()
