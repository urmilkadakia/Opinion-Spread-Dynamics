function grids = evolve (n, m, t)

population = initpopulation(n,m);
grids = zeros(n, m, t);
grids(:, :, 1) = population;

for i=1:1:t
    populationExtended = periodicLat(population);
    population = applyExtended(populationExtended);
    grids(:, :, i) = population;
end
