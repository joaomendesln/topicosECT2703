def int_tamanho(x:int) -> int:
	'''Função que calcula a quantidade de dígitos de um número inteiro'''

	t = 0
	while x > 0:
		x = x // 10
		t += 1
	return t

x = int(input())
print(int_tamanho(x))