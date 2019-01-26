close all;
global r
r = 11;
m=50;
n=50;
grids = evolve(50,50,2200);
M = showgraph(grids,m,n);
% figure(2);
% M = animDiffusionColor(grids,m,n);
