#QUESTION=Create a function that gets the sum of all the digits in a list given as a parameter

#def sum_digits(a):

	# Step 1 : initialize a total for the sum value
#	total = 0

	# Step 2 : Loop through the list (a)
#	for i in a:

		# Step 3 : Loop through individual numbers as string characters using str()
#		for x in str(i):

			# Step 4 : As the Loop goes round, add each character as an integer to the total value
#			total = int(x) + total

	# Step 5 : return the total value
#	return total

# Step 6 : print out
#print sum_digits([10,30,45])

def sum_digits(a):
    total = 0

    for i in a:
        for x in str(i):
            total = int(x)+total

    print total

sum_digits(a=[1,4,10,34])























