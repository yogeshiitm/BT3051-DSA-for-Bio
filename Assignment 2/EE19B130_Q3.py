"""
	BT3051 Data Structures and Algorithms for Biology - 2022
	Name - Yogesh Agarwala
	Roll - EE19B130

	Assignment: 2
	Q3. Primer designing
"""


def print_valid_nucleotides(str):
	"""
	prints 20 nucleotide primer of the sequence str which satisfies
	a) GC content: 40-60%
	b) Melting temperature(Tm): 52-56
	"""

	#slide over 20 bases (1 to 20, 2 to 21, ..)
	cnt = 0
	for i in range(len(str)-19):
		if(cnt>20):
			return

		substr = str[i:i+20]

		A = substr.count('A')
		C = substr.count('C')
		G = substr.count('G')
		T = substr.count('T')

		total = A+C+G+T
		GC = (G+C)*100/total
		Tm = 4*(G+C) + 2*(A+T)

		if(GC>=40 and GC<=60 and Tm>=52 and Tm<=56):
			print(f"{substr} - GC:{GC}% - Tm:{Tm}")
			cnt += 1


str = "ATGGCAATCAAGTCATTGGAATCGTTCCTTTTCGAAAGAGGTCTAGTAGG"
print_valid_nucleotides(str)