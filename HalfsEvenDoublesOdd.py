#Create a function that:
#	1. Halves even numbers
#	2. Doubles odd numbers
#	3. Returns the sum of all


#create function that takes a list as a parameter
#the function should have a for loop that iterates thru the given list
#   inside the loop have an if condition that checks whether the current number is even,if true, return it halved and assigned it to variable even
#   else if the number is odd, return it doubled and assign it to a variable odd
#After each element in the list is looped through, sum it and return the total

def sum_list(somelist):
    even=0
    odd=0
    for i in somelist:
        if (i%2==0):
            even+=i/2
        else:
            odd+=i*2
        total=odd+even
        print total
    print total

sum_list(somelist=[3,2,2,4])