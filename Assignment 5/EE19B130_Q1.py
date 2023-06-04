"""
	BT3051 Data Structures and Algorithms for Biology - 2022
	Name - Yogesh Agarwala
	Roll - EE19B130

	Assignment: 5
	Q1. Graph Perturbation
"""

import random


def average_degree(adjM):
	# adjM: n x n
	n = len(adjM)

	degrees = []
	for i in range(n):
		degrees.append(sum(adjM[i]))
	return sum(degrees)/len(degrees)

def average_degree_after_perturbation(adjM):
	n = len(adjM)
	degrees = []
	for i in range(n):
		degrees.append(sum(adjM[i]))
	to_remove = random.choice(adjM) # nodes connected to the node we want to remove
	sum_degrees = sum(degrees) - 2*sum(to_remove) #after deleting the selected node
	return sum_degrees/(len(adjM)-1)

def calc_mean(lst):
	return sum(lst)/len(lst)

def calc_standard_deviation(lst):
	n = len(lst)
	mean = sum(lst)/n
	deviations = [(x - mean)**2 for x in lst]
	variance = sum(deviations)/(n-1)
	return variance**(0.5)


if __name__ == "__main__":
	adjM1 = []
	with open('Graph1.txt') as f:
		lines = f.readlines()
		for line in lines:
			adjM1.append(list(map(int,line.rstrip().split(" "))))

	adjM2 = []
	with open('Graph2.txt') as f:
		lines = f.readlines()
		for line in lines:
			adjM2.append(list(map(int,line.rstrip().split(" "))))

	adjM3 = []
	with open('Graph3.txt') as f:
		lines = f.readlines()
		for line in lines:
			adjM3.append(list(map(int,line.rstrip().split(" "))))

	#-------------------- Part-1 ---------------------------- 
	avg_deg1 = average_degree(adjM1)
	avg_deg2 = average_degree(adjM2)
	avg_deg3 = average_degree(adjM3)
	print("Average Degree of Graph 1:",avg_deg1)
	print("Average Degree of Graph 2:",avg_deg2)
	print("Average Degree of Graph 3:",avg_deg3)
	print("")

	#-------------------- Part-2 ----------------------------
	new_avg_deg1 = average_degree_after_perturbation(adjM1)
	new_avg_deg2 = average_degree_after_perturbation(adjM2)
	new_avg_deg3 = average_degree_after_perturbation(adjM3)
	print("Average Degree after perturbation of Graph 1:",new_avg_deg1)
	print("Average Degree after perturbation of Graph 2:",new_avg_deg2)
	print("Average Degree after perturbation of Graph 3:",new_avg_deg3)
	print("")

	#-------------------- Part-3 ----------------------------
	print("After repeating the above experminent for 1000 times:")
	new_avg_deg_lst1 = []
	new_avg_deg_lst2 = []
	new_avg_deg_lst3 = []
	for i in range(1000):
		new_avg_deg_lst1.append(average_degree_after_perturbation(adjM1))
		new_avg_deg_lst2.append(average_degree_after_perturbation(adjM2))
		new_avg_deg_lst3.append(average_degree_after_perturbation(adjM3))
	print("Average Degree of Graph 1:",calc_mean(new_avg_deg_lst1))
	print("Average Degree of Graph 2:",calc_mean(new_avg_deg_lst2))
	print("Average Degree of Graph 3:",calc_mean(new_avg_deg_lst3))

	change_in_avg_degrees1 = [(avg_deg1 - x) for x in new_avg_deg_lst1]
	change_in_avg_degrees2 = [(avg_deg2 - x) for x in new_avg_deg_lst2]
	change_in_avg_degrees3 = [(avg_deg3 - x) for x in new_avg_deg_lst3]
	print("Standard Deviation in change of avg deg of Graph 1:",calc_standard_deviation(change_in_avg_degrees1))
	print("Standard Deviation in change of avg deg of Graph 2:",calc_standard_deviation(change_in_avg_degrees2))
	print("Standard Deviation in change of avg deg of Graph 3:",calc_standard_deviation(change_in_avg_degrees3))