from typing import List, TypeVar

T1 = TypeVar('T1')

def head(l1:List[T1]) -> T1:
	'''Retorna o primeiro elemento de uma lista'''

	return l1[0]

print(head([1,2,3]))

print(head(['a','e','b','-']))