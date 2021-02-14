listaRepetida :: (Integral a) => v -> a -> [v]
listaRepetida x n = listaRepetidaRec x n []
 where listaRepetidaRec :: (Integral a) => v -> a -> [v] -> [v]
       listaRepetidaRec x 0 res = res
       listaRepetidaRec x n res = listaRepetidaRec x (n - 1) (x:res)