def selectionSort(l: list):
	for i in range(len(l)):
		minIdx = i
		minEle = l[i]
		for j in range(i+1,len(l)):
			if(l[j] < minEle):
				minEle = l[j]
				minIdx = j
		l[i],l[minIdx] = l[minIdx],l[i]

if __name__=='__main__':
	l = [4,1,3,2,7]
	selectionSort(l)
	print(l)