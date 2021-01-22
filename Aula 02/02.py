def mdc(a:int,b:int) -> int:
	'''Função que calcula o M.D.C. de dois números'''
	
	if a % b == 0:
		return b
	elif b % a == 0:
		return a
	elif a > b:
		return mdc(a - b, b)
	else:
		return mdc(a, b - a)

x, y = int(input()), int(input())

print(mdc(x,y))