from typing import List, TypeVar

T1 = TypeVar('T1')

def listaEmLista(l1:List[T1], l2:List[T1]) -> bool:
	'''Checa se todos os elementos de uma lista fazem parte de outra'''

	return True if set(l1).union(set(l2)) == set(l2) else False

print(listaEmLista([1,2,3],[1,3,4,5,2]))

print(listaEmLista([1,2,1],[3,4,1,5]))