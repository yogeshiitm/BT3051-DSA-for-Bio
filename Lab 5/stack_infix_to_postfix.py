from stack_implementation import Stack
from queue_implementation import Queue

def parseString(str):
	lst = []
	i=0; n=len(str)
	while(i<n):
		c = str[i]
		num = ""
		isnumber = False
		while(i<n and str[i].isdigit()):
			num += str[i]
			isnumber = True
			i+=1
		if(isnumber): 
			lst.append(num)
		else:
			lst.append(c)
			i+=1
	return lst


def infix_to_postfix(str):
	lst = parseString(str)
	operator = Stack()
	operand = Queue()

	postfix = []

	for x in lst:
		if(x=='(' or x==' '):
			continue
		elif(x=='+' or x=='-' or x=='*' or x=='/'):
			operator.push(x)
		elif(x==')'):
			while(operand.size()!=0):
				postfix.append(operand.dequeue())

			while(operator.size()!=0):
				postfix.append(operator.pop())
		else:
			operand.enqueue(x)

	while(operand.size()!=0):
		postfix.append(operand.dequeue())
	while(operator.size()!=0):
		postfix.append(operator.pop())

	print(postfix)
	print("".join(postfix))


str = "(3*(x+1)-1)/2"
infix_to_postfix(str)