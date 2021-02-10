type Data = (Int, Int, Int)

compararDatas :: (Data) -> (Data) -> Int
compararDatas (d1, m1, a1) (d2, m2, a2)
 | a1 <  a2 = -1
 | a2 >  a1 = 1
 | m1 <  m2 = -1
 | m2 <  m1 = 1
 | d1 <  d2 = -1
 | d2 <  d1 = 1
 | d1 == d2 = 0