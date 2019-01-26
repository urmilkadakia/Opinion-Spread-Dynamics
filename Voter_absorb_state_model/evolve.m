function grids = evolve (n, m, t)

[population ,absorb] = initpopulation(n,m);
grids = zeros(n, m, t);
grids(:, :, 1) = population;

global absorbExtended;
for i=1:1:t
    [populationExtended, absorbExtended] = periodicLat(population, absorb);
    population = applyExtended(populationExtended, absorbExtended);
    grids(:, :, i) = population;
end
