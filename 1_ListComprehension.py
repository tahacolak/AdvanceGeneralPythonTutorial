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
upper_name_of_country=[a.upper() for i in a] #upper country name with times of length of word
upper_name_of_city=[b.upper() for i in b]#upper city name with times of length of word
upper_name_of_province=[c.upper() for i in c] #upper province name with times of length of word

print(f"Your Country: {upper_name_of_country}, Your City: {upper_name_of_city}, Your Province: {upper_name_of_province}")

print("****List Comprehension with Conditional Statements****")
#ComplexExample: with AsyncListIterator iterator class

import asyncio

class AsyncListIteration:
    def __init__(self,raw_sum):
        self.raw_sum=raw_sum
        self.index=0

    async def __anext__(self):
        if self.index < len(self.raw_sum):
            value = self.raw_sum[self.index]
            self.index += 1
            return value*1.2
        else:
            raise StopAsyncIteration  # Stops the async iteration

    def __aiter__(self):
        return self #provides iteration

async def main():
    async_list = AsyncListIteration([100, 200, 300,1000,250,780,490,130,640])
    async  for item in async_list:
        print(item)
asyncio.run(main())

'''
REMINDER!!! AsyncListIterator is a custom asynchronous iterator class in Python

@params: __aiter__(): Returns the asynchronous iterator itself.
        __anext__(): Asynchronously returns the next item or raises StopAsyncIteration when the list is exhausted.


REMINDER!!! StopAsyncIteration is a built-in exception in Python used to stop asynchronous iteration

        It works similarly to StopIteration, but it's specifically designed for asynchronous iterators.
        If StopAsyncIteration is raised inside __anext__(), the async for loop terminates.
'''

#End-Practices:

#Question1: Take the number divisible by 12 between (0-100) and assign in list(note: total 100 number but they are random between 0-100)
import random as rd 

divisible_numbers=[]
total_numbers=[int(rd.random()*100) for i in range(0,101,1)]

for i in total_numbers:
    if i%12==0:
        divisible_numbers.append(i)
print(divisible_numbers)

print("*******************************")

#Question2: create a list that created with only takes numbers in given mixed clause.

text=input("Please write your clause:\n")
result=[i for i in text if i.isdigit()]

print(result,"\n")

#Question3: rewrite the below code example with list comprehension, JOKER: use dict to represent output
'''
result=[]
for x in range(3):
    for y in range(3): 
        for z in range(3):
            result.append((x,y,z))
'''
new_result=[{"x:":x," y:":y," z:":z} for x in range(3) for y in range(3) for z in range(3)]
print(new_result)

#Question4: look students and notes lists and take students and their notes who has note that greater than 50
students=["Abigail","Jeremiah","Paul","Taha"]
notes=[45,95,50,85]

merged_list=[(students[i], notes[i]) for i in range(len(students))]
dict_list={key:value for (key,value) in merged_list if value>50}
print(dict_list)

