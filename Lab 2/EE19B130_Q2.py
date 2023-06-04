def find_smallest_missing_element(lst):
	i = 0
	for ele in range(len(lst)):
		if(lst[i]!=ele):
			return ele
		while(lst[i]==ele):
			i+=1

lst = [0, 1, 1, 1, 2, 3, 5, 6, 9, 11, 15]
print("The smallest missing element is:",find_smallest_missing_element(lst))