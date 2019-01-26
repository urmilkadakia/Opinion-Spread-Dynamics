import networkx as nx
import matplotlib.pyplot as plt
import random as random
import math as math

def show_graph(flag = 0):
	pos = nx.random_layout(G)
	nx.draw_networkx_nodes(G,pos,node_color=color_map,alpha=0.4)
	nx.draw_networkx_edges(G,pos,width=1,alpha=0.4)
	#nx.draw_networkx_labels(G,pos)
	if (flag == 0):	
		plt.draw()
		plt.pause(0.05)
	else:
		plt.show()

def create_graph():
	
	for i in range(1,N,1):
		G.add_node(i)
		x = random.random()
		if (x > 0.5):
			x = 1
			color_map.append('blue')
		else:
			x = -1
			color_map.append('red')
		G.node[i]['value'] = x
	i=0
	while(i < E):
		v = math.floor(random.uniform(1,N))
		y = math.floor(random.uniform(1,N))
		while(v==y):
			y = math.floor(random.uniform(1,N))
		G.add_edge(v,y)
		i = i+1

def evolve_graph(time):
	while(time > 0):
		v = math.floor(random.uniform(1,N))
		neighbors = list(nx.all_neighbors(G,v))
		x = int(math.floor(random.uniform(0,nx.degree(G,v))))
		if neighbors:
			w =neighbors[x]
		
			print('selected node: ' + repr(v))
			print('second node: ' + repr(w))
			print('neighbors: '+ repr(neighbors) + '\n')		
		
			if (G.node[v]['value'] == G.node[w]['value']):
				for i in neighbors:
					G.node[i]['value'] = G.node[v]['value']
					color_map[int(i-1)] = color_map[int(v-1)]
		else:
			print('selected vertex has no neighbors')
				
		time = time - 1
		#if (math.fmod(time,30) == 0):
		#	show_graph()


N = 1000;
E = 1500;
time = 20000;
G = nx.Graph()
color_map = []
create_graph()
show_graph(1)
fig_scatter = plt.figure(2)
evolve_graph(time)
show_graph(1)
