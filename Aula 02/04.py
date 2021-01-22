def eh_palindromo(s:str) -> bool:
	'''Função que verifica se uma string é um palíndromo'''

	i = 0
	while i <= len(s) // 2:
		if s[i] != s[-(i + 1)]:
			return False
		i += 1
	return True

s = input()
print(eh_palindromo(s))