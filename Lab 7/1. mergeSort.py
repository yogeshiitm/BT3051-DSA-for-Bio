# Python program for implementation of MergeSort
def merge(L, R):
	i = j = k = 0
	temp = [None]*(len(L)+len(R))
	while i < len(L) and j < len(R):
		if L[i] < R[j]:
			temp[k] = L[i]
			i += 1
		else:
			temp[k] = R[j]
			j += 1
		k += 1
	while i < len(L):
		temp[k] = L[i]
		i += 1
		k += 1
	while j < len(R):
		temp[k] = R[j]
		j += 1
		k += 1
	return temp

def mergeSort(arr):
	if len(arr) > 1:
		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]
		L = mergeSort(L)
		R = mergeSort(R)
		arr = merge(L,R)

	return arr
		

if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]
	print(arr)
	arr = mergeSort(arr)
	print(arr)