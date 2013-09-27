#!/usr/bin/python
import sys

f = open("/usr/share/dict/words", "r")

anagrams = {}
words = 0
print "finding anagrams, please wait"

for line in f:
		words += 1
		word = line.strip()

		tmp_list = list(word.lower())
		l = 0
		l = len(tmp_list)

		sorted = False
		unsorts = 0
		while not sorted:
				for i in range(0, l-1):
						if tmp_list[i] > tmp_list[i+1]:
								a = tmp_list[i]
								tmp_list[i] = tmp_list[i+1]
								tmp_list[i+1] = a
								unsorts = 1
				if unsorts == 0:
						sorted = True
				else:
						unsorts = 0

		newstr = ''.join(tmp_list)

		if newstr in anagrams:
				anagrams[newstr].append(word)
		else:
				anagrams[newstr] = [word]

print "done."

total = 0
for a in anagrams:
		if len(anagrams[a]) > 1:
				total = total + len(anagrams[a])
				#print anagrams[a]

print words, "words searched"
print total, " anagrams found"
