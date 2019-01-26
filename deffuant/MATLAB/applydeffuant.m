function newmat = applydeffuant(lat)

n = size(lat, 1) - 2;
m = size(lat, 2) - 2;
newmat = zeros(n,m);    

newmat = deffuant(lat);
    