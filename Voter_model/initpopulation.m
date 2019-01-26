function population = initpopulation ( n, m )
population = rand(n,m);

for i=1:1:n
    for j=1:1:m
        if population(i,j) > 0.5
            population(i,j) = 1;
        else
            population(i,j) = 0;
        end
    end
end

