# Calvin Anderson, Spring 2023 Homework 2
# 01-19-2023

# range(j, k , l)	Identifies a range of integers from j  to k–1 separated by some interval l.
# 1.
# list = []
# i = len(list)
# for i in range(i, 100, 3):

# 1.

mylist = []
for i in range(0, 3*100, 3):
    mylist.append(i)
    
print(mylist)
print(len(mylist))

# 2.



    

"""
Create a list of numbers 100 elements in length that counts by 3s - i.e., [3,6,9,12,...]

Using the list from question 1, create a second list whose elements are the same values converted to strings. hint: use a for loop and the function str().

Using the list from question 2, create a variable that concatenates each of the elements in order of index (Hint: result should be like "36912...").

Using .pop() and .append(), create a list whose values are the same as the list from question 1 but in reverse order. (Hint: .pop() removes the last element from a list. The value can be save, i.e., x = lst.pop().)

Using len(), calculate the midpoint of the list from question 1. Pass this midpoint to slice the list so that the resultant copy includes only the second half of the list from question 1.

Create a string that includes only every other element, starting from the 0th element, from the string in question 3 while maintaining the order of these elements (Hint: this can be done be using a for loop whose values are descending).

Explain the difference between a dynamic list in Python (usually referred to as a list) and a tuple.
"""