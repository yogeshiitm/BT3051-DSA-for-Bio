from queue_implementation import Queue
from stack_implementation import Stack

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q)

s = Stack()
while(not q.isEmpty()):
	s.push(q.dequeue())

while(not s.isEmpty()):
	q.enqueue(s.pop())

print(q)