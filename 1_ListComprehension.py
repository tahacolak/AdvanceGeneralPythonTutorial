#List Comprehension with Time & Space Complexity 
'''
@author:tahacolak
In short-hand, List Comprehension is usage of a comprehensive
expressions despite usage of element appending in list with long-way.

A little insightful sample:  
    list=[expression for item in range(0,5,1)]
'''

numbers = []

for i in range(0,5,1):
    numbers.append(i)

print("Stable Condition of the List:\t",(numbers))
print(numbers.pop(-1)) #a little bit reminder! .pop(indexNumber) method provides remove the last element into the list that based in stack.
print("New Condition of the List:\t"+str(numbers))

#list comprehension version
from random import randbytes
numbers_new=[list for list in randbytes(5) ]
print("The Comprehension List:\t",numbers_new)

random_numbers1=randbytes(4)
random_numbers2=randbytes(2)

numbers_new_complex=random_numbers2,[i for i in(random_numbers1)]
print(f"The Merged List:\t{numbers_new_complex}")

print(type(random_numbers2)) 
#if you retrieve to write random_numbers2 to assign numbers_new_complex it is not expected situation. To fix it..:

numbers_new_complex=[i*2 for i in random_numbers2]+[i+3 for i in(random_numbers1)]
print(f"The Corrected Merged List:\t{numbers_new_complex}")

#Another Example

print("Please Write your country")
a=input("Your Country is ")
print(a)


print("Please Write your city")
b=input("Your City is ")
print(b)

print("Please Write your province")
c=input("Your Province is ")
print(c)
upper_name_of_country=[a.upper() for i in a]
upper_name_of_city=[b.upper() for i in b]
upper_name_of_province=[c.upper() for i in c]

print(f"Your Country: {upper_name_of_country}, Your City: {upper_name_of_city}, Your Province: {upper_name_of_province}")