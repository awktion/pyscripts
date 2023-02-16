#!/usr/bin/python
#fizzbuzz by 42
"""
Fizz buzz is a group word game for children to teach them about division.
Players take turns to count incrementally, replacing any number divisible by
three with the word "fizz", and any number divisible by five with the word
"buzz", and any number divisible by both 3 and 5 with the word "fizzbuzz".
"""
#letsdoit python2.x


for num in range(01,61):
	if num % 15 == 0:
			print str(num) + " fizzbuzz!!"
	elif num % 3 == 0:
		print str(num) + " fizz!"
	elif num % 5 == 0:
		print str(num) + " buzz!"
	else:
		print num
