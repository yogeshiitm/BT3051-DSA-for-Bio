"""
	BT3051 Data Structures and Algorithms for Biology - 2022
	Name - Yogesh Agarwala
	Roll - EE19B130

	Assignment: 1
	Q4. Harmonic mean
"""

def harmonic_mean(n):
	""" 
	calculate and return the harmonic mean of the first 'n' number
	"""
	denominator = 0
	for i in range(1,n+1):
		denominator += 1/i

	hm = n/denominator
	return hm


n = int(input())
print(f"Harmonic mean of first {n} numbers: {harmonic_mean(n)}")