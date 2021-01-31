from typing import List, TypeVar

T1 = TypeVar('T1')

def take(n:int, l1:List[T1]) -> List[T1]:
	'''Retorna os n primeiros elementos de uma lista'''

	return l1[:n]

print(take(2, [1,2,3]))

print(take(10, ['a','e','b','-']))