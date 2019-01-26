function population1 = Voter_majority()

global population r;

n = size(population,1);
m = size(population,2);

rx = randi(n,r,1);
ry = randi(m,r,1);
su = 0;
for i=1:1:r
    su = su + population(rx(i),ry(i));
end

for i=1:1:r
    if su > 0
        population(rx(i),ry(i)) = 1;
    else
        population(rx(i),ry(i)) = -1;
    end
end

population1 = population;





    

