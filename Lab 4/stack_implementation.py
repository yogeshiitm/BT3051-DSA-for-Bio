class Stack:
	def __init__(self):
		self._st = list()

	def size(self):
		return len(self._st)

	def isEmpty(self):
		if(len(self._st) == 0):
			return True
		return False

	def isFull(self):
		#just incase we want a upper limit on stack size
		if(len(self._st) > 1000000):
			return True
		return False

	def push(self,e):
		if(self.isFull()):
			print("Stack is full!")
		else:
			self._st.append(e)

	def pop(self):
		if(self.isEmpty()):
			print("Stack is empty!")
		else:
			last = self._st[-1]
			self._st.pop()
			return last