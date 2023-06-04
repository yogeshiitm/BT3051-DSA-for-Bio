"""
	BT3051 Data Structures and Algorithms for Biology - 2022
	Name - Yogesh Agarwala
	Roll - EE19B130

	Assignment: 1
	Q5. Conversion to binary
"""

def decimal_to_binary(n):
	if(n==0):
		return "0"

	str = ""
	while(n>0):
		str += f"{n%2}" #append remainder of n/2
		n = n // 2 #keep dividing n by 2

	binary = str[::-1] #reverse of str
	return binary

n = int(input())
print(decimal_to_binary(n))