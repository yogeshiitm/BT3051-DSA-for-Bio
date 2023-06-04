class Queue:
	def __init__(self):
		self._arr = [None]
		self._size = 0
		self._capacity = 1
		self._frontptr = 0
		self._backptr = -1

	def enqueue(self,x):
		if(self._size < self._capacity):
			self._backptr = (self._backptr+1) % self._capacity
			self._arr[self._backptr] = x
			self._size += 1
		else:
			self._capacity *= 2
			temp = [None]*(self._capacity)
			f = self._frontptr
			b = self._backptr
			n = self._size

			if(f<=b):
				for i in range(f,b+1):
					temp[i] = self._arr[i]
			else:
				j=0
				for i in range(f,n):
					temp[j] = self._arr[i]
					j += 1

				for i in range(0,b+1):
					temp[j] = self._arr[i]
					j += 1

			temp[self._size] = x
			self._arr = temp
			self._frontptr = 0
			self._backptr = self._size
			self._size += 1

	def dequeue(self):
		# 1 2 3 N N N
		# N N N 1 2 3
		# 2 3 N N N 1
		# N 1 2 3 N N
		x = self._arr[self._frontptr]
		self._arr[self._frontptr] = None
		self._frontptr = (self._frontptr+1) % self._capacity
		self._size -= 1
		return x

	def isEmpty(self):
		return self._size==0

	def isFull(self):
		return self._size==self._capacity

	def size(self):
		return self._size

	def __repr__(self):
		return "Internally: {self._arr}".format(self=self)


if __name__ == "__main__":
	q = Queue()
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	q.enqueue(4)
	q.enqueue(5)
	print(q)
	q.dequeue()
	print(q)
	q.dequeue()
	print(q)
	q.enqueue(6)
	q.enqueue(7)
	print(q)
	q.enqueue(8)
	q.enqueue(9)
	q.enqueue(10)
	print(q)
	q.enqueue(11)
	print(q)