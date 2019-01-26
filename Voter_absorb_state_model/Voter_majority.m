function newSite = Voter_majority(i, j , latExtended)

global absorbExtended;
neighbour = [latExtended(i-1,j) latExtended(i,j+1) latExtended(i+1,j) latExtended(i,j-1)];

sm = sum(neighbour);
if sm == 0 
    newSite = 0;
    absorbExtended(i,j) = 1;
elseif sm == 4
    newSite = 1;
    absorbExtended(i,j) = 1;
end
if absorbExtended(i,j) ~= 1
    if sm > 2
        newSite = 1;
    elseif sm < 2
        newSite = 0;
    else
        r = rand();
        if r > 0.5
            newSite = 1;
        else
            newSite = 0;
        end
    end
end
    

