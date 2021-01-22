def int_tamanho(x:int) -> int:
	'''Função que calcula a quantidade de dígitos de um número inteiro'''

	t = 1
	while x > 0:
		x = x // (10 ** 1)
		t += 1
	return t - 1

x = int(input())
print(int_tamanho(x))