function M = showgraph(graphList,m,n)
% SHOWGRAPHS - Function to return movie visualization 
% of grids in graphList
file= [num2str(m) '_' num2str(n) '_gray.gif'];
map = [0.1 0.75 0.2;     % green
        0.6 0.2 0.1];    % orange
colormap(map);
m = size(graphList, 3);
for k = 1:m
    gg = graphList(:,:,k);
    %keyboard;
    for i=1:1:size(gg,1)
        for j=1:1:size(gg,2)
            if gg(i,j) < 0.5
                gg(i,j) = -1;
            else
                gg(i,j) = 1;
            end
        end
    end
    g = gg(:, :);
    image(g + 1)
    axis off
    %axis square
    M(k) = getframe;
    %pause(0.05);
end;

%movie2gif(M,file,'LoopCount', 0, 'DelayTime', 0);