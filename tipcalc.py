#!/usr/bin/python
#tip calc v1 by 42
#python is cake


bill = float(raw_input("How Much Is The Bill?"))
print ""
#test input:
#print "the bill is", bill
people = int(raw_input("How Many People Together?"))
print ""
tipcentage = int(raw_input("What Percentage Do You Want To Tip?"))
print ""
print "Calculating Payment..."
#lets do math
tip = round(bill * tipcentage / 100, 2)
total = bill + tip
tipeach = round(tip / people, 2)
totaleach = round(total / people, 2)
billeach = round(bill / people, 2)
print "for a bill of", bill
print "tipping percentage", tipcentage
print "with a group of", people
print "tip is", tip
print "tip plus bill is", total
print "each person's part of teh bill is $", billeach
print "each person's part of the tip is $", tipeach
print "this means each person pays $", totaleach
