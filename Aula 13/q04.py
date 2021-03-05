from functools import reduce


def concat(x:str, y:str) -> str:
	return (x) + "," + (y)

l = [1,2,3]

print(reduce(concat, map(str, l)))