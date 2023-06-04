"""
	BT3051 Data Structures and Algorithms for Biology - 2022
	Name - Yogesh Agarwala
	Roll - EE19B130

	Assignment: 4
	Q1. Edit distance
"""

replacement_matrix = {
	'A':{'A':0,'G':2,'C':3,'T':3},
	'G':{'A':2,'G':0,'C':3,'T':3},
	'C':{'A':3,'G':3,'C':0,'T':1},
	'T':{'A':3,'G':3,'C':1,'T':0},
}

def edit_distance_recurse(s1, s2, m, n, dp):
	if m == 0:
		return n
	if n == 0:
		return m
	if(dp[m][n] != -1):
		return dp[m][n]

	ans1 = edit_distance_recurse(s1, s2, m, n-1, dp) + 5# Insert
	ans2 = edit_distance_recurse(s1, s2, m-1, n, dp) + 2# Remove
	ans3 = edit_distance_recurse(s1, s2, m-1, n-1, dp) + replacement_matrix[s1[m-1]][s2[n-1]]# Replace
	dp[m][n] = min(ans1,ans2,ans3)
	return dp[m][n]


def edit_distance(s1, s2):
	m = len(s1)
	n = len(s2)
	dp = [[-1 for i in range(n+1)] for j in range(m+1)]
	return edit_distance_recurse(s1, s2, m, n, dp)


def closely_related(lst):
	min_cost = 1000000000
	ans = [None, None]

	for i in range(len(lst)):
		for j in range(len(lst)):
			if(i!=j):
				cost = edit_distance(genes[lst[i]], genes[lst[j]])
				print("Cost of ",lst[i]," to ",lst[j]," = ",cost)
				if(cost < min_cost):
					min_cost = cost
					ans = [lst[i], lst[j]]
	print("\nClosest species pair is: '{ans[0]}' and '{ans[1]}'".format(ans=ans))


if __name__ == '__main__':
	genes = {
		"gene_A": "TATGCCGGATCCTTTCCTTGGATAAAAGATTTGTAAACCAACATTTGTGTGGCTCCCATCTGGTTGAAGCTTTGTACTTGGTTTGCG",
		"gene_B": "TATGCCGGATCCTTTCAGCTTGGATAAAAGATTTATAAAACCAACATTTGTGTGGCTCCCATCTGGTTGAAGCTTTGTACTTGGTTTGCGT",
		"gene_C": "TATGCCGGGTCCTTTCCTTGGATAAAAGATTTGTGAACCAACATTTGTGTGGCTCCCCTCTGGTTGAAGCTTTGTACTTGGTTTGCGT",
		"gene_D": "TATGCGATCCTTTCCTTGGATAAAAGATTTGTAAACCAACATTTGCTGGTGGCTCCCATCTGGTTGAAGCTTTGTACTTGGTTTGCG"
	}
	closely_related(["gene_A", "gene_B", "gene_C", "gene_D"])
"""
Output:
	Cost of  gene_A  to  gene_B  =  22
	Cost of  gene_A  to  gene_C  =  12
	Cost of  gene_A  to  gene_D  =  14
	Cost of  gene_B  to  gene_A  =  10
	Cost of  gene_B  to  gene_C  =  15
	Cost of  gene_B  to  gene_D  =  24
	Cost of  gene_C  to  gene_A  =  9
	Cost of  gene_C  to  gene_B  =  24
	Cost of  gene_C  to  gene_D  =  23
	Cost of  gene_D  to  gene_A  =  14
	Cost of  gene_D  to  gene_B  =  36
	Cost of  gene_D  to  gene_C  =  26

	Closest species pair is: 'gene_C' and 'gene_A'
"""