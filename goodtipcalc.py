#!/usr/bin/python
#tip calc v1 by 42
#python is cake
def tipeach(bill, people, tipcentage):
	"""docs go here"""
	while True:
		try:
			return float(bill * tipcentage / people / 100 )
		except:
			print "something went wrong calculating tip"




def billeach(bill, people):
	"""docs go here"""
	while True:
		try:
			return float(bill/people)
		except:
			print "something went wrong calculating bill"


def payeach(bill, people, tipcentage):
	"""docs go here"""
	while True:
		try:
			return tipeach(bill, people, tipcentage) + billeach(bill, people)
		except:
			print "something went wrong calculating bill"






def main():
# populate bill
	while True:
		try:
			bill = float(raw_input("How Much Is The Bill?"))
			print "bill is", bill
			break
		except:
			print "error error will robinson on bill - must be numbers"
# populate people
	while True:
		try:
			people = int(raw_input("How Many People Are Present?"))
			print "number of people", people
			break
		except:
			print "error error will robinson on people, must be an integer"

# populate tip
	while True:
		try:
			tipcentage = int(raw_input("What Percentage To Tip?"))
			print "tipping percentage is", tipcentage
			break
		except:
			print "error error will robinson on tip percentage, must be an integer"


	print bill, people, tipcentage
	print "tip total", round(tipeach(bill, people, tipcentage), 2) * people
	print "tip each", round(tipeach(bill, people, tipcentage), 2)
	print "bill each", round(billeach(bill, people), 2)
	print "each person should pay", round(payeach(bill, people, tipcentage), 2)

if __name__ == "__main__":
	main()
