function M = animDiffusionGray(grids,m,n)
% ANIMDIFFUSIONGRAY - Function to return grayscale movie visualization 
% of grids in grids
global MAX 
file= [num2str(m) '_' num2str(n) '_gray.gif'];
lengthGrids = size(grids, 3);
M = moviein(lengthGrids);

map = zeros(MAX + 1, 3);
for i = 0:MAX
    amt = i/MAX;
    map(i + 1, :) = [amt, amt, amt];
end; 
colormap(map);

%m = size(grids, 1);
%n = size(grids, 2);

for k = 1:lengthGrids
    g = grids(:, :, k);
    image(MAX - g + 1);
    colormap(map);

    axis([0 m 0 n]);
    axis equal;
    axis off;
    drawnow;
    M(k) = getframe;
    
%title('heat diffusion with normal distributed random numbers','FontSize',16);
end;
%title('heat diffusion with normal distributed random numbers','FontSize',16);
%movie2gif(M,file,'LoopCount', 0, 'DelayTime', 0);
