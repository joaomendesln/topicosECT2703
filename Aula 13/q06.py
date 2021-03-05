def eh_par(x:int) -> bool:
	return x % 2 == 0

l1 = [1,2,3]
l2 = [1,3,5]

print(any(map(eh_par,l1)))
print(any(map(eh_par,l2)))