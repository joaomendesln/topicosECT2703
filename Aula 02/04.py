def eh_palindromo(s:str) -> bool:
	'''Função que verifica se uma string é um palíndromo'''

	for i in range(0, len(s) // 2 + 1):
		if s[i] != s[-(i + 1)]:
			return False
	return True

s = input()
print(eh_palindromo(s))