#Create a function that gets the sum of all the digits in a list given as a parameter

#   list1=[2,3,7,5,4]
 #   listlength=len(list1)


   # for i in list1:
    #    i+=i
     #   print i
  #  sum1=sum(list1)
   # print sum1

#numbers()



def numbers(somelist):
    totalsum=0

    for i in somelist:

        if (i%10==0):
            i=i/10


        totalsum=totalsum+i
    print totalsum

numbers(somelist=[2,20,5,6,])























