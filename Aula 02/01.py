def eh_primo(x:int) -> bool:
	'''Função que verifica se um número é primo'''

	if x <= 1:
		return False

	for i in range(2,x):
		if i % x == 0:
			return False

	return True

x = int(input())
print(eh_primo(x))