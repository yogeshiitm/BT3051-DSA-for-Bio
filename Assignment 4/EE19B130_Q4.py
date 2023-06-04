"""
	BT3051 Data Structures and Algorithms for Biology - 2022
	Name - Yogesh Agarwala
	Roll - EE19B130

	Assignment: 4
	Q4. Dynamic programming
"""

import numpy as np

def max_subSquare(M):	
	"""
	returns max size of sub-squareMatrix with all 1s
	"""
	R = len(M)
	C = len(M[0])

	#dp[i][j] represents max size of sub-squareMatrix with all 1s, whose bottom-right corner is (i,j)
	dp = [[0 for i in range(C)] for j in range(R)]

	# Update 1st row and 1st col
	for i in range(R):
		dp[i][0] = M[i][0]
	for j in range(C):
		dp[0][j] = M[0][j]

	# Update other entries
	for i in range(1, R):
		for j in range(1, C):
			if (M[i][j] == 1):
				dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1

	#Maximum size sub-squareMatrix with all 1s
	maxSize = max(max(x) for x in dp)
	return int(maxSize)


if __name__ == '__main__':
	matrix = np.loadtxt('data.txt')
	print("Maximum size sub-squareMatrix with all 1s: ",max_subSquare(matrix))
	# Output : 17