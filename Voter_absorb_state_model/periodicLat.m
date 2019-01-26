function [extlat, extlat1] = periodicLat(lat,absorb)
% PERIODICLAT returns extended lattice
extendRows = [lat(end, :); lat; lat(1, :)];
extlat = [extendRows(:, end) extendRows extendRows(:, 1)];

extendRows1 = [absorb(end, :); absorb; absorb(1, :)];
extlat1 = [extendRows1(:, end) extendRows1 extendRows1(:, 1)];



