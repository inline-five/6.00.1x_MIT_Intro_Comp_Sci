vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

for each in s:
    if each in vowels:
        count += 1

print("Number of vowels: ", count)

'''
Problem 1
10.0/10.0 points (graded)
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels
contained in the string s. Valid vowels are: 'a', 
'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl',
your program should print:

Number of vowels: 5
'''
