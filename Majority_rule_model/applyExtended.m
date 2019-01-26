function newmat = applyExtended()

global population;

n = size(population, 1);
m = size(population, 2);
newmat = zeros(n,m);

newmat = Voter_majority();