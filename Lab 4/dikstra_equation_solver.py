from stack_implementation import *

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


def dikstra_two_stack(str):
	"""
	Works only for full parametrized expressions
	"""
	lst = parseString(str)
	operator = Stack()
	operand = Stack()

	for x in lst:
		if(x=='(' or x==' '):
			continue
		elif(x.isnumeric()):
			operand.push(int(x))
		elif(x=='+' or x=='-' or x=='*' or x=='/'):
			operator.push(x)
		elif(x==')'):
			a = operand.pop()
			b = operand.pop()
			op = operator.pop()
			# print(a,b,op)

			if(op=='+'):
				operand.push(b + a)
			elif(op=='-'):
				operand.push(b - a)
			elif(op=='*'):
				operand.push(b * a)
			elif(op=='/'):
				operand.push(b / a)

	if(operand.size()!=1 or not operator.isEmpty()):
		print("Invalid input string")
	else:
		return operand.pop()


if __name__ == '__main__':
	str = "((3*4)+((51-3)*(6/2)))"
	print(dikstra_two_stack(str))