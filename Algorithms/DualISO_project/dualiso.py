#!/usr/bin/python2
'''The input Query graph and Data graph are both given as edge lists. Any form of representation can be used, it is upto the flexibility of networkx library.'''
import networkx as nx
import dualiso_main

G = nx.read_edgelist("test-g.txt",nodetype=int,create_using=nx.DiGraph())
Q = nx.read_edgelist("test-q.txt",nodetype=int,create_using=nx.DiGraph())

print "G",G.number_of_nodes()
print "Q",len(Q.nodes())
print "======"

result = dualiso_main.findMatches(G,Q)

matches_as_graph=[]
for m  in result:
	R=nx.DiGraph()
	for u,u_ in Q.edges():
		R.add_edge(m[u][0],m[u_][0])
		matches_as_graph.append(R)
print "Matches found in Data Graph\n==============="

for r in matches_as_graph:
	print r.edges()
