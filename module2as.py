# -*- coding: utf-8 -*-
"""Module2AS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I-wteTyBuKnc6djRuN5rUu_zCC3kQ_Sk
"""

#1 What is the output of the following code?
#nums =set([1,1,2,3,3,3,4,4])
#print(len(nums))
#Answer#--> 4 as a set only considers unique values

#2 Answer John and Peter
d ={"john":40, "peter":45}
print(list(d.keys()))
#ans john and peter

#3 A website requires a user to input username and password to register.
# Write a program to check the validity of password given by user.
# Following are the criteria for checking password:
# #1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
import re
# print("Enter a username :")
# user=input()
print("Enter the password :")
pwd=input()
if len(pwd)<6:
  print("Password length should be at least 6 ")
elif len(pwd)>12:
  print("Password length should not be more than 12")

special_char=['$','#','@']
if not any(char.isdigit() for char in pwd):
  print('Password should have at least one numeral')
if not any(char.isupper() for char in pwd):
  print('Password should have at least one uppercase letter')
if not any(char.islower() for char in pwd):
  print("Password should atleast have one lowercase letter")
if not any(char in special_char for char in pwd):
  print("Password should have atleast one of the symbols @$#")

#Write a for loop that prints all elements of a list and their position in the list.
a = [4,7,3,2,5,9] 
for i in a:
  print("the element of list is ",i,"and the postion is",a.index(i))

# #write   a   program   which accepts  a   string   from   console   and   print   the characters that have even indexes.
# Example: If the following string is given as input to the program
# H1e2l3l4o5w6o7r8l9dThen, 
# the output of the program should be:Helloworld
print("Enter the String :")
_inp = input()
y = len(_inp)
out=""
for i in range(y):
    if (_inp.index(_inp[i])) % 2 == 0:
        out+=(_inp[i])
print("the wrangled string is :",out)

#6. 
user_inp=input("Enter a string :")
i=len(user_inp)
print(user_inp[::-1])

#7Please write a program which count and print the numbers of each character in a string input by console.
print("Enter a string :")
inp=input()
_x=set(inp)#converting the input string to unqiue set
for letter in _x:
  if letter in inp:#comapring with orignal set to count each letter 
    print(letter,inp.count(letter))

#8With   two   given   lists   [1,3,6,78,35,55]   and   [12,24,35,24,88,120,155],
#write   a program to make a list whose elements are intersection of the above given lists.
li=[1,3,6,78,35,55]
li1=[12,24,35,24,88,120,155]
x=set(li).intersection(li1)
print("The intersection of",li,"and", li1,"is",x)

#9 By usinglist comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155]
li_=[12,24,35,24,88,120,155]
newlist = [x  for x in li_ if x!=24]
print(newlist)

#10 By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155]
li=[12,24,35,70,88,120,155]
newlist = [x for x in li if li.index(x) not in [0,4,5]]
print(newlist)

#11 By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in
li= [12,24,35,70,88,120,155]
li=[x for x in li if (x%5 and x%7)!=0]
print(li)

#12Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a  given  n  input  by console (n>0)
num = int(input("Enter a number: "))
newnum = 0

for i in range(1,num+1):
    newnum = newnum+(i/(i+1))

print("computed value : ",format(round(newnum,2)))