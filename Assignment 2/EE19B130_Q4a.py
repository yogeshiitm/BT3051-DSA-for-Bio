"""
	BT3051 Data Structures and Algorithms for Biology - 2022
	Name - Yogesh Agarwala
	Roll - EE19B130

	Assignment: 2
	Q4.a) Palindromic sequence
"""


def six_base_palindrome_count(DNA):
	"""
	returns the count of 6 base pair long 
	palindromic sites in the DNA sequence
	"""
	mapping = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
	palindromic_cnt = 0

	for i in range(len(DNA)-5):
		forward_strand = DNA[i:i+6]
		complementary_strand = "".join([mapping[i] for i in forward_strand])
		
		"""
		palindromic sequence occurs when complementary strands of DNA 
		read the same in both directions i.e. either from the 5-prime end or the 3-prime end
		"""
		if(forward_strand[::-1] == complementary_strand):
			palindromic_cnt += 1

	return palindromic_cnt



f = open("dna.fasta", "r")
text = f.readlines()
DNA_seq = text[1]
print(six_base_palindrome_count(DNA_seq))