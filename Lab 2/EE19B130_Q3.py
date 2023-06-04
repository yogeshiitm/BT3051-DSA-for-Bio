def linear_search(lst, to_find):
	for i in range(len(lst)):
		if(lst[i]==to_find):
			return i

	return "Element not found"


def iterative_binary_search(lst, to_find):
	l = 0
	r = len(lst)-1
	while(l+1 < r): #l+1==r
		mid = (l+r)//2
		if(lst[mid] >= to_find):
			r = mid
		else:
			l = mid+1

	print(l,r)

	if(lst[l]==to_find): return l
	elif(lst[r]==to_find): return r
	else: return "Element not found"



def recursive_binary_search_helper(lst, to_find, l, r):
	if(l+1>=r):
		if(lst[l]==to_find): return l
		elif(lst[r]==to_find): return r
		else: return "Element not found"

	mid = (l+r)//2
	if(lst[mid] >= to_find):
		return recursive_binary_search_helper(lst,to_find,l,mid-1)
	else:
		return recursive_binary_search_helper(lst,to_find,mid,r)

def recursive_binary_search(lst, to_find):
	l=0;r=len(lst)-1
	return recursive_binary_search_helper(lst,to_find,l,r)


lst = [1,1,2,3,4,4,5,6,7,7,8,9,9,9,11]
to_find = 1
print(f"Position of element {to_find}: {linear_search(lst,to_find)}")
print(f"Position of element {to_find}: {iterative_binary_search(lst,to_find)}")
print(f"Position of element {to_find}: {recursive_binary_search(lst,to_find)}")


