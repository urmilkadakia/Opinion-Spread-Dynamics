function newmat = applyExtended(latExtended)

n = size(latExtended, 1) - 2;
m = size(latExtended, 2) - 2;
newmat = zeros(n,m);    
for j = 2:(m + 1)
    for i = 2:(n + 1)
        newmat(i - 1, j - 1) = Voter(i, j , latExtended);
    end;
end;