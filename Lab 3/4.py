class dna_manipulation:
	def __init__(self,str):
		self._str = str
		self._mapping = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

	def complementary(self):
		return "".join([self._mapping[i] for i in self._str])

	def transcription(self):
		return "".join([('U' if(i=='T') else i) for i in self._str])

print(dna_manipulation("ATTGCCAG").complementary())
print(dna_manipulation("ATTGCCAG").transcription())




class dna_manipulation2:
	def complementary(arg):
		_mapping = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
		return "".join([_mapping[i] for i in arg])

	def transcription(arg):
		return "".join([('U' if(i=='T') else i) for i in arg])

print(dna_manipulation2.complementary("ATTGCCAG"))
print(dna_manipulation2.transcription("ATTGCCAG"))
