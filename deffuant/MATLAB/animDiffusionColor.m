function M = animDiffusionColor(grids,m,n)
% ANIMDIFFUSIONCOLOR - Function to return color movie visualization 
% of grids in grids
global MAX 

lengthGrids = size(grids, 3);
M = moviein(lengthGrids);

map = zeros(MAX + 1, 3);
for i = 0:MAX
    amt = i/MAX;
    map(i + 1, :) = [amt, 0, 1 - amt];
end; 
colormap(map);
map

for k = 1:lengthGrids
    g = grids(:, :, k);
    image(g + 1)
    colormap(map);

    %axis([0 m 0 n]);
    %axis equal;
    axis off;
    axis square
    M(k) = getframe;
    pause(0.05);
end;
%keyboard;

