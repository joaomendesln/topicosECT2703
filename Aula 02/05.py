def eh_triangulo_retangulo(x:int, y:int, z:int) -> bool:
	'''Função que verifica se três números correspondem aos lados de um triângulo retângulo'''

	if y > x:
		x, y = y, x
	if z > x:
		x, z = z, x
	if x ** 2 == y ** 2 + z ** 2:
		return True
	return False

x, y, z = int(input()), int(input()), int(input())

print(eh_triangulo_retangulo(x, y, z))