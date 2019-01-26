function grids = evolve (n, m, t)

global population;
population = initpopulation(n,m);
grids = zeros(n, m, t);
grids(:, :, 1) = population;

for i=1:1:t
    newmat = applyExtended();
    grids(:, :, i) = newmat;
end
