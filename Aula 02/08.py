def int_tamanho(x:int) -> int:
	'''Função que calcula a quantidade de dígitos de um número inteiro'''

	t = 1
	while x > 0:
		x = x // (10 ** 1)
		t += 1
	return t - 1

def inverter(x:int, tamanho:int) -> int:
	'''Função que inverte um número inteiro'''

	t = int_tamanho(x)

	if x == 0:
		return 0

	return inverter(x % 10 ** (t - 1), tamanho) + (x // 10 ** (t - 1)) * 10 ** (tamanho - t)
	

x = int(input())
print(inverter(x, int_tamanho(x)))