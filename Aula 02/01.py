def eh_primo(x:int) -> bool:
	'''Função que verifica se um número é primo'''

	aux = x - 1

	if x <= 1:
		return False
	else:
		while aux >= 2:
			if x % aux == 0:
				return False
			aux -= 1

	return True

x = int(input())
print(eh_primo(x))

help(eh_primo)