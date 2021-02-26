from functools import reduce

def soma(a:int, b:int) -> int:
	return a + b

l = ["3", "5", "b5", "", "2"]

l_ints = filter(lambda x: x.isnumeric() == True, l)
l_ints2 = map(int, l_ints)
soma_l_ints = reduce(soma, l_ints2)

print(soma_l_ints)