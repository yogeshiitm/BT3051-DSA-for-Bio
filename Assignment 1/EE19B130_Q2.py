"""
	BT3051 Data Structures and Algorithms for Biology - 2022
	Name - Yogesh Agarwala
	Roll - EE19B130

	Assignment: 1
	Q2. Identifying structure
"""

def find_structure(str):
	structure = ""
	for c in str:
		ascii = ord(c)
		if(ascii>=65 and ascii<=90):
			structure += 'A'
		elif(ascii>=97 and ascii<=122):
			structure += 'A'
		elif(ascii>=48 and ascii<=57):
			structure += 'N'

	return structure


str = input()
structure = find_structure(str)
if(structure == "AAAAANNNNA"):
	print("Yes. Input string is concurrent with the structure of the PAN ID")
else:
	print("No. Input string is not concurrent with the structure of the PAN ID")