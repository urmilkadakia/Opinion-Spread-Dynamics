function extlat = periodicLat(lat)
% PERIODICLAT returns extended lattice
extendRows = [lat(end, :); lat; lat(1, :)];
extlat = [extendRows(:, end) extendRows extendRows(:, 1)];




