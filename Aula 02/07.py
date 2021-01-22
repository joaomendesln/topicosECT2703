def encontrar(s:str) -> bool:
	'''Função que verifica se uma string contém o caractere $'''

	for i in range(0,len(s)):
		if s[i] == '$':
			return True
	return False

s = input()
print(encontrar(s))