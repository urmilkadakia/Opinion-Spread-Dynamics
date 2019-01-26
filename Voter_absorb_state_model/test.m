
close all;
global MAX
MAX = 50;
m=200;
n=200;
grids = evolve(50,50,100);
M = showgraph(grids,m,n);
% figure(2);
% M = animDiffusionColor(grids,m,n);
