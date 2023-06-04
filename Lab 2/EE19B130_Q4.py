
# Time: O(n^2)
def find_pair_quadratic(lst,sum):
	for i in range(len(lst)):
		for j in range(i+1,len(lst)):
			if (lst[i]+lst[j] == sum):
				return {lst[i], lst[j]}


def iterative_binary_search(lst, to_find):
	l = 0
	r = len(lst)-1
	while(l+1 < r):
		mid = (l+r)//2
		if(lst[mid] > to_find):
			r = mid-1
		else:
			l = mid

	if(lst[l]==to_find): return l
	elif(lst[r]==to_find): return r
	else: return -1


# Time: O(nlog(n))
def find_pair_linearithmic(lst,sum):
	lst.sort()
	for i in range(len(lst)):
		to_find = sum - lst[i]
		if(iterative_binary_search(lst,to_find) != -1):
			return {lst[i], to_find}



lst = [1, 3, 2, -2, 6]
value = 5
print(f"Pair with sum {value} is: ",find_pair_quadratic(lst,value))
print(f"Pair with sum {value} is: ",find_pair_linearithmic(lst,value))