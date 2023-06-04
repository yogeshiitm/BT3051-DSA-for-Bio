"""
	BT3051 Data Structures and Algorithms for Biology - 2022
	Name - Yogesh Agarwala
	Roll - EE19B130

	Assignment: 5
	Q3. Floyd-Warshall Algorithm
"""


import networkx as nx
import math


def max_distance_of_any_node_from_a_source(G,source):
	"""
	Given an connected undirected weighted networkx graph and a source node, find the shortest paths to all other nodes and return the largest among them.
	"""

	N = G.number_of_nodes()

	#---------------------------------- Floyd-Warshall algorithm -----------------------------------#
	# let dist be a |V| × |V| array of minimum distances initialized to ∞ (infinity)
	dist = [[math.inf for i in range(N+1)] for j in range(N+1)]   # Initialise the distance array
	# for each edge (u, v) in edge_list do dist[u][v] ← w(u, v)
	edge_list = list(G.edges(data="weight"))
	for edge in edge_list:
		u,v,w = map(int,edge)
		dist[u][v] = w
		dist[v][u] = w
	# for each vertex v do dist[v][v] ← 0
	for v in range(1,N+1):                                  
		dist[v][v] = 0
	# for rest of the edges (u,v)
	for k in range(1,N+1):
		for i in range(1,N+1):
			for j in range(1,N+1):
				if dist[i][j] > (dist[i][k] + dist[k][j]):
					dist[i][j] = dist[i][k] + dist[k][j]
	# where dist[u][] stores the shortest path from a given node u to all other nodes

	#-------------------- shortest paths from source node to all other nodes -----------------------#
	shortest_paths = [0]*(N+1) 
	for v in range(1,N+1):
		shortest_paths[v] = dist[source][v]

	#----------------------------- longest among these shortest paths ------------------------------#
	max_distance = 0
	for i in range(1,N+1):
		max_distance = max(max_distance, shortest_paths[i])

	return max_distance


def critical_node(G):
	"""
	Given an connected undirected weighted networkx graph, return the node that has the shortest longest path. 
	"""
	N = G.number_of_nodes()

	# finding long_short_paths corresponding to each node
	long_short_paths = [math.inf]*(N+1)
	for v in range(1,N+1):
		# longest among the shortest paths from source node v
		long_short_path = max_distance_of_any_node_from_a_source(G,v)
		long_short_paths[v] = long_short_path
		print("Source node =",v," long_short_path =",long_short_path)

	# nodes with shortest long_short_paths
	min_long_short_path = math.inf
	for v in range(1,N+1):
		if(long_short_paths[v] < min_long_short_path):
			min_long_short_path = long_short_paths[v]
			critical_node = v

	return critical_node


if __name__ == '__main__':
	g = nx.Graph()
	#Generate the graph from the edge list provided
	with open('q3.edgelist') as f:
		edge_list = f.readlines()
		for edge in edge_list:
			u,v,w = edge.rstrip().split(" ")
			g.add_edge(u,v,weight=int(w))

	print("\nCritical node =",critical_node(g))

	# Output: Critical node = 2
	# Explanation: both node 2 and node 4 have equal shortest long_short_path 
	# but as mentioned in piazza, we can return either one of them