class Set:
	def __init__(self, lst):
		#self._st = set(lst)
		self._st = lst[0]
		self._st += [lst[i] for i in range(1,len(lst)) if lst[i-1]!=lst[i]]

	def __sub__(self, arg):
		#return list(set(self._st).difference(set(arg._st)))
		return [k for k in self._st if k not in arg._st]

	def __add__(self, arg):
		#return list(set(self._st).union(set(arg._st)))
		return list(set(list(self._st) + list(arg._st)))

	def __xor__(self, arg):
		#return list(set(self._st).intersection(set(arg._st)))
		return [k for k in self._st if k in arg._st]

	def __mul__(self,arg):
		cartesian_product = set()
		for i in self._st:
			for j in arg._st:
				cartesian_product.add((i,j))

		return cartesian_product


a = Set([1,2,3])		
b = Set([3])
c = Set([3,4])
print(a-b)
print(a+c)
print(a^c)
print(a*c)