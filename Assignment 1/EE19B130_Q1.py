"""
	BT3051 Data Structures and Algorithms for Biology - 2022
	Name - Yogesh Agarwala
	Roll - EE19B130

	Assignment: 1
	Q1. List comprehension
"""

#given string
str = "all models are wrong, but some are useful"

#a's in the above string, using list comprehension
str_a = [i for i in str if i=='a']

#count the number of a's in this string
count = len(str_a)
print(count)