#Tuples: ordered, immutable, allows duplicate elements
mytuple = ("Hassaan", 28, "LA")

print(mytuple)


#IMPORTANT, to know if its tuple or not just print out print(type(mytuple))

item=mytuple[0]

print(item)

'''you can uncomment this to try it out
mytuple[0] = "zain" #this will not work, as you can't change the contents of tuples.
'''

print(mytuple[::-1]) #this will reverse the tuple list 

#using for loops with tuples.

for i in mytuple:
	print(i)

if 'Hassaan' in mytuple:
	print('ayo')
else:
	print('fam')

#Lets create a new tuple with letters or alphabets

alpha_tuples = ('a', 'b', 'b', 'c', 'd')

print(len(alpha_tuples)) #just like we used in the lists
# this returns 5 elements

print(alpha_tuples.count('b')) #this will return the number of times 'b' is in the tuple
#which is 2 times

#again just like in lists you can use .index method to findout the psotion
print(alpha_tuples.index('a'))

#Now, you can convert a tuple to list. Fairly simple tbh

my_list = list(alpha_tuples)

print(my_list)

#Now we convert it back to tuples

tuple2 = tuple(my_list)

print(tuple2)

# now we create tuples with integers
#this time we will do slicing 
#Slicing in python means taking elements from one given index to another given index
a = (1, 2, 3, 4, 5, 6, 7)
b = a[2:5]

print(b)

#we can use slice()
#lets create a tuple with days of the week

days_week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

#using slice() method
#the first value of the slicing method is the starting index postion and second value is ending index postion
#!!!!!!!!!!!!!!REMINDER: index positioning starts from 0 !!!!!!!!!!!!!!!!!!!!!

'''
Now, if you want to slice of the working days in a week, it would be from starting position 1 which is Monday
and ending postion 5 which is Friday, right? WRONG...
#here is why.
'''  

alt_week = slice(1,5)
print(days_week[alt_week])
# when you this out you see that it gives us a tuple from Mon-Thurs but where is friday?
#usually the ending index is neglected and considers the value before it, since you're ending it on the 5th value
#so instead of using 5 we use 6th index position to give us the value of the 5th index position

alt_week2 = slice(1,6)
print(days_week[alt_week2])