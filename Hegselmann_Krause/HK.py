import networkx as nx
import matplotlib.pyplot as plt
import random as random
import math as math
from colormap import Colormap

def show_scatter(t):
	
	fig_scatter.hold(True)
	for i in range(1,N,1):	
		plt.scatter(100 - t,G.node[i]['value'], marker='o' ,s=80, facecolors='none', edgecolors='r')
		plt.show

def show_graph(flag = 0):
	
	plt.figure(3)
	pos = nx.random_layout(G)
	nx.draw_networkx_nodes(G,pos,cmap = plt.get_cmap('coolwarm'),vmin = 0 , vmax = 1,node_color = color_map,alpha=1)
	nx.draw_networkx_edges(G,pos,width=1,alpha=1)
	nx.draw_networkx_labels(G,pos)
	if (flag == 0):	
		plt.draw()
		plt.pause(0.05)
	else:
		plt.show()

def create_graph():
	
	for i in range(1,N,1):
		G.add_node(i)
		x = random.random()
		color_map.append(x)
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
	
	d = 0.2
	mu = 0.5

	while(time > 0):
		v = math.floor(random.uniform(1,N))
		neighbors = list(nx.all_neighbors(G,v))
		cnt = 0
		opinion = 0
		if neighbors:
		
			print('selected node: ' + repr(v))
			print('neighbors: '+ repr(neighbors) + '\n')	
		
			for w in neighbors:
				if (G.node[v]['value'] - G.node[w]['value']) < d :
					cnt = cnt + 1
					opinion = opinion + G.node[w]['value']
			if cnt > 0:
				G.node[v]['value'] = opinion / cnt		
				color_map[int(v-1)] = G.node[v]['value']
			show_scatter(time)		
			time = time - 1
		else:
			print('selected node: '+ repr(v) + ' has no neighbors\n')
		
		#if (math.fmod(time,30) == 0):
		#	show_graph()


N = 10;
E = 30;
time = 50;
G = nx.Graph()
color_map = []
create_graph()
show_graph(1)
fig_scatter = plt.figure(1)
evolve_graph(time)
show_graph(1)
