
close all;
global MAX
MAX = 50;
m=200;
n=200;
grids = evolve(100,100,10000);
M = showgraph(grids,m,n);
figure(2);
M = animDiffusionGray(grids,m,n);
