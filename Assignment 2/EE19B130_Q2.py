"""
	BT3051 Data Structures and Algorithms for Biology - 2022
	Name - Yogesh Agarwala
	Roll - EE19B130

	Assignment: 2
	Q2. Linear Algorithm
"""


def farther_sum_pair(lst):
	"""
	finds and prints the pair of integers in an array 
	whose sum is farthest from zero
	"""

	lst = [abs(i) for i in lst]

	#a and b maintains max two elements
	a=max(lst[0],lst[1])
	b=min(lst[0],lst[1])

	for i in lst:
		if(i>=a):
			b=a
			a=i
		elif(a>i and i>b):
			b=i
	
	return (a,b)

lst = [1,3,7,-10,5,8]
print(farther_sum_pair(lst))