embaralhar :: String -> String -> String
embaralhar s1 [] = s1
embaralhar [] s2 = s2
embaralhar (x:xs) (y:ys) = x:(y:(embaralhar xs ys))


-- embaralhar' :: String -> String -> String
-- embaralhar' s1 s2 = embaralharRec s1 s2 []
--  where embaralharRec :: String -> String -> String -> String
--        embaralharRec s1 [] res         = s1 ++ res
--        embaralharRec [] s2 res         = s2 ++ res
--        embaralharRec (x:xs) (y:ys) res = embaralharRec xs ys (y:(x:res))