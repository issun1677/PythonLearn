
#Uncomment things to print


#Lists:  they ordered, mutable and allows duplicate elements

'''uncomment from here
mylist = ["banana", "cherry", "apple"]
print(mylist)
'''


#lists allows duplicate items 
'''uncomment from here
mylist2 = [5, True, "apple", "apple"]

print(mylist2)
'''

'''
if you want to access an element from a specific list,
you refer the specific item with its index number, REMEMEBER THIS
it starts from 0 and not 1.
'''

'''uncomment from here
item = mylist2[0] #this will give you the first item in mylist2 
print(item)

item1 = mylist2[-1] #this will give you the last item in mylist2 
print("item output is " + item1)
'''


#comment things out if you really want to run individually.

#using for loops with lists
''' uncomment from here
for i in mylist2:
	print(i)
'''


'''uncomment from here
if 5 in mylist2:
	print('yes, its ' + str(mylist2[0]))
else:
	print('no')
''' #till here

#Now if you want to check how many elements you have in the list, you have to use 'len'

#example, we will create a new list 

#'''uncomment from here
car = ['tyres', 'engine', 'brakes', 'AC', 'windows','seats']

#print(len(car))
#'''


#it shows that it has 6 elements 



'''
what if we wanted to add "accelerator" without scrolling all the way up to car list 
(not really all the way up lets just pretend the car list all the way up :) ) 
'''
#we use the append method 


'''uncomment from here
car.append("accelerator")
print(car)
'''



#if you want to insert an item in a specific order or place
#we use the 'insert' method


'''uncomment from here
car.insert(3,'backlights') # backlights will be inserted between brakes and ac 
print(car)
'''




'''
pop is an inbuilt function in Python that removes and returns
last value from the list or the given index value.
'''


'''uncomment from here
item = car.pop()
print(item)
'''

'''
The remove() method removes the first 
occurrence of the element with the specified value.
'''

"""uncomment from here
person = ['a', 'b', 'c', 'd']

person.remove('d')

print(person)
"""


#clear() removes all the element 

'''
item = list(person)

print(item)

item.clear()

print(item)
'''

#reverse() you can even reverse the list.

'''
mylist3 = ['youtube', 'google', 'twitter', 'Outlook']

rev_erse = list(mylist3)

rev_erse.reverse()
print(rev_erse)
'''

#------------------------------
#switching the list back to mylist3

'''
mylist3 = list(rev_erse)
mylist3.reverse()

print(mylist3)
'''



#sort() this method gives the output in an ascending order.

'''
myNum = [-2, 3, -4, 1, 2, -2, 0 ]

myNum.sort()

print(myNum)
'''

'''
number1 = [1, 2, 3, 4]
number2 = [5, 6, 7, 8]

total_num = number1 + number2

print(total_num)
'''

#-----------------------------------------------------------------
#carefully look what's happeing below

original_list = ['Anakin', 'Obi', 'Padme', 'Mace']

updated_list = original_list

updated_list.append('Luke')

print(updated_list)
print(original_list)



'''
Now 'Luke' is added to updated_list but its also included 
into the original_list; however, thats not we want right? Thought so.
how to fix that?
#just add .copy() to the original_list when you're assigning it to the updated_list
'''



original_list = ['Anakin', 'Obi', 'Padme', 'Mace']

updated_list = original_list.copy()

updated_list.append('Luke')

print(updated_list)
print(original_list)



#or you can use list()

original_list = ['Anakin', 'Obi', 'Padme', 'Mace']

updated_list = list(original_list)

updated_list.append('Luke')

print(updated_list)
print(original_list)


# or you could use [:]

original_list = ['Anakin', 'Obi', 'Padme', 'Mace']

updated_list = original_list[:]

updated_list.append('Luke')

print(updated_list)
print(original_list)

#----------------------------------------------------------

#creating new list from existing list 
#List Comprehension 


