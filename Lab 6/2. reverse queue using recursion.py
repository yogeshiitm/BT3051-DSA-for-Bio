from queue_implementation import Queue

def reverse_queue(q):
	if(q.isEmpty()):
		temp = Queue()
		return temp

	q_copy = q
	first = q_copy.dequeue()
	reverse_queue(q_copy) # q without first element
	q_copy.enqueue(first) # first becomes last
	return q_copy

if __name__ == '__main__':
	q = Queue()
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	q.enqueue(4)
	q.enqueue(5)

	print(q)
	q = reverse_queue(q)
	print(q)
