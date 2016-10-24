# Author: Finn
# Determine the number of connected components in the underlying graph.

import networkx as nx

currentNode = -1
graphIndex = -1
graphs = []
x = "start"

# Building the Graphs:

while (x != ""):
    x = input()
    if (currentNode == -1) and (x == ' '):
        break
    if (currentNode == -1):
        graphIndex += 1
        if (x != '0'):
            graphOrder = int(x)                 # Sets order.
            G = nx.Graph()                      # Creates graph.
        else:
            break                               # Exits while loop.
        
        for i in range(0,graphOrder):           # Generates graph nodes.
            G.add_node(i)
    else:
        line = x.split()                        # Seperates connections.

        for tok in line:                        # Creates edges for each 
            G.add_edge(currentNode, int(tok))   # connection with currentNode.
            
    currentNode += 1                            # If currentNode is last node, then store value
    if (currentNode == graphOrder):             # into graph[], reset and read in next graph.
        currentNode = -1
        graphs.append(nx.number_connected_components(G))

# Printing the Results:

for tok in graphs:
    print(str(tok))