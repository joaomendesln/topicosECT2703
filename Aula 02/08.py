def inverter(x:int) -> int:
	'''Função que inverte um número inteiro'''

	result = 0

	while x > 0:
		result = result * 10 + x % 10 
		x = x // 10

	return result

x = int(input())
print(inverter(x))