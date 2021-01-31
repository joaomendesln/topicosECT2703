primChar :: [Char] -> Bool
primChar (h:t) = elem h t

-- iguaisIniFim :: (Num n) => n -> [n] -> Bool
-- iguaisIniFim k l = take k l == drop (length l - k) l

iguaisIniFim :: Int -> [Int] -> Bool
iguaisIniFim n l = take n l == drop (length l - n) l

ehMaiuscula :: Char -> Bool
ehMaiuscula c = c `elem` ['A'..'Z']