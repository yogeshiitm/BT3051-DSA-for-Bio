"""
	BT3051 Data Structures and Algorithms for Biology - 2022
	Name - Yogesh Agarwala
	Roll - EE19B130

	Assignment: 3
	Q2. Class for sequence analysis
"""

class geneticanalysis:
	def __init__(self,sequence):
		self._sequence = sequence

	def validdna(self, printoutput=True):
		result = True
		for c in self._sequence:
			if c not in {'A','G','T','C'}:
				result = False
				break

		if printoutput:
			if result:
				print("{self._sequence} is a valid sequence".format(self=self))
			else:
				print("{self._sequence} is NOT a valid sequence".format(self=self))
		return result

	def potentialgene(self, printoutput=True):
		seq = self._sequence
		n = len(seq)
		start_codon = ('ATG')
		stop_codon = ('TAA','TAG','TGA')
		
		# checking if the seq is a validdna
		if not self.validdna(printoutput=False):
			print("{self._sequence} is NOT a potential gene since it is NOT a valid sequence".format(self=self))			return False

		result = True
		# condition 1
		if len(seq)%3 != 0:
			result = False
		# condition 2
		if seq[:3] not in start_codon or seq[-3:] not in stop_codon:
			result = False
		# condition 3
		for i in range(0,n,3):
			if seq[i:i+3] in stop_codon and i!=n-3:
				result = False

		if printoutput:
			if result:
				print("{self._sequence} is a potential gene".format(self=self))
			else:
				print("{self._sequence} is NOT a potential gene".format(self=self))
		return result


	def aacount(self):
		# checking if the seq is a potentialgene
		if not self.potentialgene(printoutput=False):
			print("{self._sequence} is NOT a potential gene".format(self=self))
		else:
			n = len(self._sequence)
			cnt = n//3 - 1
			print("{self._sequence} will produce a protein of length {cnt}".format(self=self,cnt=cnt))
			return cnt


GA = geneticanalysis('ATGGCAAGCTCGACTTGA')
GA.validdna()
GA.potentialgene()
GA.aacount()