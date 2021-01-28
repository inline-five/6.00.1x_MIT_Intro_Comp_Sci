search = 'bob'
count = 0
index = s.find(search)
index += 1
while index > 0:
    index = s.find(search, index + 1)
    count += 1

print("Number of times bob occurs is: ", count)

'''
Problem 2
10.0/10.0 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' 
occurs in s. For example, if s = 'azcbobobegghakl', then your program 
should print

Number of times bob occurs is: 2
'''
