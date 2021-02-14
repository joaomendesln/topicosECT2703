ordenarListasOrdenadas :: (Ord a) => [a] -> [a] -> [a]
ordenarListasOrdenadas l1 []          = l1
ordenarListasOrdenadas [] l2          = l2
ordenarListasOrdenadas (x:xs) (y:ys) = if x <= y then (x : ordenarListasOrdenadas xs (y:ys)) else (y : ordenarListasOrdenadas (x:xs) ys)


-- ordenarListasOrdenadas' :: (Ord a) => [a] -> [a] -> [a]
-- ordenarListasOrdenadas' l1 l2 = ordenarListasOrdenadasRec l1 l2 []
--  where ordenarListasOrdenadasRec :: (Ord a) => [a] -> [a] -> [a] -> [a]
--        ordenarListasOrdenadasRec l1 [] res         = l1 ++ res
--        ordenarListasOrdenadasRec [] l2 res         = l2 ++ res
--        ordenarListasOrdenadasRec (x:xs) (y:ys) res = if x <= y then (ordenarListasOrdenadasRec xs (y:ys) (x:res)) else (ordenarListasOrdenadasRec (x:xs) ys (y:res))