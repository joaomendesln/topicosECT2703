separarEm :: Int -> [v] -> ([v],[v])
separarEm 0 l      = ([],l)
separarEm n (x:xs) = (x:l1, l2)
 where (l1, l2) = separarEm (n - 1) xs

-- separarEm :: Int -> [v] -> ([v],[v])
-- separarEm n l = separarEmRec n l ([],[])
--  where separarEmRec :: Int -> [v] -> ([v],[v]) -> ([v],[v])
--        separarEmRec 0 l res = (fst res, l)
--        separarEmRec n (x:xs) res = separarEmRec (n - 1) xs (((x:xs)!!(n-1)):(fst res), snd res)