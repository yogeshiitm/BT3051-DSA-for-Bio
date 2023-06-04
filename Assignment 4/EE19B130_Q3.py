"""
	BT3051 Data Structures and Algorithms for Biology - 2022
	Name - Yogesh Agarwala
	Roll - EE19B130

	Assignment: 4
	Q3. Network analysis
"""


f = open("social_edgeList.txt",'r')
lines = f.readlines()[1:]
f.close()


def adjacencyList(edge_list):
	# creating adjacency list using dictionary of lists
	adjacency_list = dict()
	for edge in edge_list:
		s = edge[0]
		d = edge[1]
		if s not in adjacency_list:
			adjacency_list[s] = []
		if d not in adjacency_list:
			adjacency_list[d] = []

		adjacency_list[s].append(d)
		adjacency_list[d].append(s)

	#printing adjacency_list
	print("### ADJACENCY LIST: ###\n")
	for s,d_lst in adjacency_list.items():
		print("Vertex " + s + ":", end="")
		for d in d_lst:
			print(" -> {}".format(d), end="")
		print(" \n")


def adjacencyMatrix(edge_list):
	#mapping each vertex name to a number
	mapNodeNumber = dict()
	x = 0
	for edge in edge_list:
		s = edge[0]
		d = edge[1]
		if s not in mapNodeNumber:
			mapNodeNumber[s] = x; x += 1
		if d not in mapNodeNumber:
			mapNodeNumber[d] = x;x += 1

	#list of vertices
	numNodes = len(mapNodeNumber)
	listVertices = [None]*numNodes
	for v,n in mapNodeNumber.items():
		listVertices[n] = v

	#creating adjacency matrix
	adjacency_matrix = [[0 for i in range(numNodes)] for j in range(numNodes)]
	for edge in edge_list:
		s = edge[0]
		d = edge[1]
		s_num = mapNodeNumber[s]
		d_num = mapNodeNumber[d]

		adjacency_matrix[s_num][d_num] = 1
		adjacency_matrix[d_num][s_num] = 1

	#printing adjacency matrix
	print("### ADJACENCY MATRIX: ###\n")
	print("".ljust(22),listVertices)
	for i in range(numNodes):
		print(listVertices[i].ljust(22), adjacency_matrix[i])


def neighborsCount(edge_list):
	# creating adjacency list using dictionary of lists
	adjacency_list = dict()
	for edge in edge_list:
		s = edge[0]
		d = edge[1]
		if s not in adjacency_list:
			adjacency_list[s] = []
		if d not in adjacency_list:
			adjacency_list[d] = []

		adjacency_list[s].append(d)
		adjacency_list[d].append(s)

	#printing adjacency_list
	print("### NEIGHBORS COUNT: ###\n")
	for s,d_lst in adjacency_list.items():
		print("{s}: {n}".format(s=s,n=len(d_lst)))
		


def networks(edge_list):
	adjacencyList(edge_list)
	print("\n\n")
	adjacencyMatrix(edge_list)
	print("\n\n")
	neighborsCount(edge_list)


if __name__ == '__main__':
	lines = [line.rstrip() for line in lines]
	edge_list = [line.split('\t') for line in lines if line]
	networks(edge_list)