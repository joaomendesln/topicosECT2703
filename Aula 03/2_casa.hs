type Ponto = (Float, Float)

espelhoX :: Ponto -> Ponto
espelhoX p = (- fst p, snd p)

espelhoY :: Ponto -> Ponto
espelhoY p = (fst p, - snd p)