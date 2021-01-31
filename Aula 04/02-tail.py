from typing import List, TypeVar

T1 = TypeVar('T1')

def tail(l1:List[T1]) -> List[T1]:
	'''Retorna uma lista com exceção do seu primeiro elemento'''

	return l1[1:]

print(tail([1,2,3]))

print(tail(['a','e','b','-']))