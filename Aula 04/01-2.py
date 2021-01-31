from typing import List, TypeVar

def matrizId(n:int) -> List[List[int]]:
	'''Retorna a matriz identidade de dimensão passada como entrada'''

	m = []

	for i in range(n):
		l = []
		for j in range(n):
			if i == j:
				l.append(1)
			else:
				l.append(0)
		m.append(l)

	return m


print(matrizId(4))