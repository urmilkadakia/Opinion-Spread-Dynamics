function newlat = deffuant(lat)

m = size(lat,1);
n = size(lat,2);

ix = randi(m);
iy = randi(n);

jx = randi(m);
jy = randi(n);

mu = 0.5;
d = 0.2;

if (lat(ix,iy) - lat(jx,jy)) < d 
    lat(ix,iy) = lat(ix,iy) + mu*(lat(jx,jy) - lat(ix,iy));
    lat(jx,jy) = lat(jx,jy) + mu*(lat(ix,iy) - lat(jx,jy));
end

newlat = lat;
    
