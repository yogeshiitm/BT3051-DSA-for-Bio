"""
	BT3051 Data Structures and Algorithms for Biology - 2022
	Name - Yogesh Agarwala
	Roll - EE19B130

	Assignment: 5
	Q4. Birthday problem
"""

import random

def has_shared_birthday(n):
	birthdays=[]
	"""
	First lets generate n random birthdays.
	Each no. from 1 to 365 will represent a birthday, so we can select n random nos. from 1 to 365
	"""
	for i in range(n):
		birthdays.append(random.randint(1,365))

	"""Now check is their any pair with same birthday"""
	if(len(set(birthdays)) < len(birthdays)):
		return True
	return False


def birthday_problem(n):
	shared_birthday_cnt = 0
	total_experiment_cnt = 10000
	"""
	To calculate experimental probability we need to repeat the experiment over and over again.
		so lets repeat it for 10,000 times for each value of n
	"""
	for exp in range(total_experiment_cnt): 
		if(has_shared_birthday(n)):
			shared_birthday_cnt += 1

	prob = shared_birthday_cnt/total_experiment_cnt
	return prob


if __name__ == '__main__':
	n = 23
	print("Probability for n={n} is {p}".format(n=n,p=birthday_problem(n)))