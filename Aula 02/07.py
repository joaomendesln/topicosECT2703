def encontrar(s:str) -> bool:
	'''Função que verifica se uma string contém o caractere $'''

	return '$' in s

s = input()
print(encontrar(s))