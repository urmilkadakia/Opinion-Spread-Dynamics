function grids = evolve (n, m, t)

population = initpopulation(n,m);
grids = zeros(n, m, int64(t/100));
grids(:, :, 1) = population;

for i=1:1:t
    population = applydeffuant(population);
    if mod(t,100) == 0
        grids(:, :, int64(i/100) + 1) = population;
    end
end
