function newSite = Voter(i, j , latExtended)

neighbour = [latExtended(i-1,j) latExtended(i,j+1) latExtended(i+1,j) latExtended(i,j-1)];
r = randi(4);
newSite = neighbour(r);

