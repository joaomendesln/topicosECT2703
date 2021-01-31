primChar :: [Char] -> Bool
primChar (h:t) = elem h t

iguaisIniFim :: (Eq n) => Int -> [n] -> Bool
iguaisIniFim n l = take n l == drop (length l - n) l

ehMaiuscula :: Char -> Bool
ehMaiuscula c = c `elem` ['A'..'Z']