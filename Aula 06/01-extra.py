import eh_primo

def decomposicao(n):
	'''Gera uma sequência tuplas representando a decomposição em fatores primos do valor de entrada'''
	for x in range(n):
		cont = 0
		if eh_primo.func(x) and n % x == 0:
			k = n
			while k % x == 0:
				k /= x
				cont += 1	
			yield (x, cont)

l = list(decomposicao(10))
print(l)