# Author: Finn O'Connor
# Find the length of the longest path starting from vertex 0.

import networkx as nx

def dag_path_chooser(cP, cN, nLen, nodes):
	while(nLen != cN):
		cP.append(cN)
		nLen = cN
		cN = nodes[cN][1]

def dag_longest_path(G):
	nodes = {}
	chosenPath = []
	nodeLength = None
	for crntNode in nx.topological_sort(G):
		nL = [(nodes[nodeLength][0] + data.get('weight', 1), nodeLength)
			for (nodeLength, data) in G.pred[crntNode].items()]
		if (nL):
			maxNodeLength = max(nL)
		else:
			maxNodeLength = (0, crntNode)
		if (maxNodeLength[0] >= 0):
			nodes[crntNode] = maxNodeLength
		else:
			nodes[crntNode] = (0, crntNode)
	crntNode = max(nodes, key = nodes.get)
	dag_path_chooser(chosenPath, crntNode, nodeLength, nodes)
	chosenPath.reverse()
	return chosenPath

def longest_path_length(G):
	descOfZero = nx.descendants(G,0)
	descOfZero = list(descOfZero)
	for node in nx.nodes(G):
		if (node not in descOfZero and node != 0):
			G.remove_node(node)
	
	final = dag_longest_path(G)
	finalLen = len(final)-1
	return finalLen

currentNode = -1
graphIndex = -1
graphs = []
x = "start"

# Building the Graphs:

while (True):
	x = input()
	if (currentNode == -1) and (x == ' '):
		break
	if (currentNode == -1):
		graphIndex += 1
		if ('0' in x.split()):
			break			    				# Exits while loop.				  	    
		else:
			graphOrder = int(x)      			# Sets order.
			G = nx.DiGraph() 					# Creates graph.
		
		for i in range(0,graphOrder):			# Generates graph nodes.
			G.add_node(i)
	else:
		line = x.split()					    # Seperates connections.
		
		for tok in line:					    # Creates edges for each 
			G.add_edge(currentNode, int(tok))   # connection with currentNode.

	currentNode += 1						    # If currentNode is last node, then store value
	if (currentNode == graphOrder):				# into graph[], reset and read in next graph.
		currentNode = -1
		graphs.append(longest_path_length(G))
	
# Printing the Results:

for tok in graphs:
	print(str(tok))