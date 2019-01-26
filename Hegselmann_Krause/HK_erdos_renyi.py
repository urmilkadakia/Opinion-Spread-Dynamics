import networkx as nx
import matplotlib.pyplot as plt
import random as random
import math as math
from colormap import Colormap

def show_scatter(t):
	
	fig_scatter.hold(True)
	for i in range(1,N,1):	
		plt.scatter(time - t,G.node[i]['value'], marker='o' ,s=20, facecolors='none', edgecolors='r')
		plt.xlabel('time')
		plt.ylabel('opinion')
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
	
	for i in range(0,N,1):
		x = random.random()
		color_map.append(x)
		G.node[i]['value'] = x
	
def evolve_graph(time):
	
	d = 0.5
	mu = 0.5

	while(time > 0):
		v = math.floor(random.uniform(1,N))
		neighbors = list(nx.all_neighbors(G,v))
		cnt = 0
		opinion = 0
		if neighbors:
		
			print(time)			
			#print('selected node: ' + repr(v))
			#print('neighbors: '+ repr(neighbors) + '\n')	
		
			for w in neighbors:
				if (G.node[v]['value'] - G.node[w]['value']) < d :
					cnt = cnt + 1
					opinion = opinion + G.node[w]['value']
			if cnt > 0:
				G.node[v]['value'] = opinion / cnt		
				color_map[int(v-1)] = G.node[v]['value']
			if(time % 1000 == 0):	
				show_scatter(time)		
			time = time - 1
		else:
			print('selected node: '+ repr(v) + ' has no neighbors\n')
		
		#if (math.fmod(time,30) == 0):
		#	show_graph()


N = 1000;
E = 2000;
time = 12000;
G = nx.erdos_renyi_graph(N,0.4)
color_map = []
create_graph()
#show_graph(1)
fig_scatter = plt.figure(1)
evolve_graph(time)
plt.show()
#show_graph(1)
