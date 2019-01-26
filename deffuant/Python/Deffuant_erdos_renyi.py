from mpl_toolkits.mplot3d import Axes3D
import networkx as nx
import matplotlib.pyplot as plt
import random as random
import math as math
from colormap import Colormap
import numpy as np
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from tempfile import TemporaryFile
import csv

def show_scatter(t):
	
	fig_scatter.hold(True)
	for i in range(1,N,1):	
		plt.scatter(time - t,G.node[i]['value'], marker='o' ,s=30, facecolors='none', edgecolors='r')
		plt.xlabel('time')
		plt.ylabel('opinion')
		plt.show

def show_graph(flag = 0):
	
	plt.figure()
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

	for t in range(0,time,1):
		v = math.floor(random.uniform(1,N))
		degree = nx.degree(G,v)
		neighbors = list(nx.all_neighbors(G,v))
		if neighbors:
			
			w = neighbors[int(math.floor(random.uniform(0,nx.degree(G,v))))]
			
			print(t)
			#print('selected node: ' + repr(v))
			#print('second node: ' + repr(w))	
		
			if (G.node[v]['value'] - G.node[w]['value']) < d :
				G.node[v]['value'] = G.node[v]['value'] + mu * ( G.node[w]['value'] - G.node[v]['value'] )
				G.node[w]['value'] = G.node[w]['value'] + mu * ( G.node[v]['value'] - G.node[w]['value'] )
				color_map[int(v-1)] = G.node[v]['value']
				color_map[int(w-1)] = G.node[w]['value']			
			
			for i in range(0,N,1):
				print(repr(i) + ' vv' + repr(t))
				data[i][t] = G.node[i]['value']			
			#if( time == 20000 or (Time - time) % 9800 == 0):	
			#	show_scatter(time)
			#time = time - 1
		else:
			print('selected vertex has no neighbors')
		#if (math.fmod(time,30) == 0):
		#	show_graph()


N = 100
E = 200
Time = 1000
time = 1000
data = [[0 for i in range(time)] for j in range(N)]
G = nx.erdos_renyi_graph(N,0.2)
color_map = []
create_graph()
#show_graph(1)
#fig_scatter = plt.figure(2)
evolve_graph(time)
#plt.show()
fig = plt.figure()
ax = fig.add_subplot(111)
x = np.arange(0,N,1)
y = np.arange(0,time,1)
X,Y = np.meshgrid(y,x)
print('X' + repr(np.shape(X)) + 'Y' + repr(np.shape(Y)) + 'Z' + repr(np.shape(data)))
#surf = ax.plot_surface(X, Y, data, cmap=cm.plasma, linewidth=0, antialiased=False)
contourqq = ax.contourf(X,Y,data,cmap='jet')
cbar = fig.colorbar(contourqq)
#plt.show()
with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(data)
#data.dump("Deffuant_erdos_100_1000.dat")
#show_graph(1)

