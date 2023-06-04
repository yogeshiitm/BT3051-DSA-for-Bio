"""
	BT3051 Data Structures and Algorithms for Biology - 2022
	Name - Yogesh Agarwala
	Roll - EE19B130

	Assignment: 4
	Q2. Weighted Graph
"""

import matplotlib.pyplot as plt
import networkx as nx

"""
Output of Q1:
	Cost of  gene_A  to  gene_B  =  22
	Cost of  gene_A  to  gene_C  =  12
	Cost of  gene_A  to  gene_D  =  14
	Cost of  gene_B  to  gene_A  =  10
	Cost of  gene_B  to  gene_C  =  15
	Cost of  gene_B  to  gene_D  =  24
	Cost of  gene_C  to  gene_A  =  9
	Cost of  gene_C  to  gene_B  =  24
	Cost of  gene_C  to  gene_D  =  23
	Cost of  gene_D  to  gene_A  =  14
	Cost of  gene_D  to  gene_B  =  36
	Cost of  gene_D  to  gene_C  =  26
"""


if __name__ == '__main__':
	G=nx.MultiDiGraph()
	G.add_edge('A','B',weight=22)
	G.add_edge('A','C',weight=12)
	G.add_edge('A','D',weight=14)
	G.add_edge('B','A',weight=10)
	G.add_edge('B','C',weight=15)
	G.add_edge('B','D',weight=24)
	G.add_edge('C','A',weight=9)
	G.add_edge('C','B',weight=24)
	G.add_edge('C','D',weight=23)
	G.add_edge('D','A',weight=14)
	G.add_edge('D','B',weight=36)
	G.add_edge('D','C',weight=26)

	edge_labels = dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)])
	pos = nx.spring_layout(G)

	nx.draw(G,pos,with_labels=True,connectionstyle='arc3,rad=0.1')
	nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,font_size=8,label_pos=0.8)
	plt.show()