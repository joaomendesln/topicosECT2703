pontoEmRetangulo :: (Num a, Ord a) => (a, a) -> ((a, a), a, a) -> Bool
pontoEmRetangulo (xp, yp) ((xr, yr), l, h) = if xp >= xr && xp <= (xr + l) && yp >= yr && yp <= (yr + l) 
	then True
	else False