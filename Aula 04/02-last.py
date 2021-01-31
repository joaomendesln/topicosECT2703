from typing import List, TypeVar

T1 = TypeVar('T1')

def last(l1:List[T1]) -> T1:
	'''Retorna o último elemento de uma lista'''

	return l1[-1]

print(last([1,2,3]))

print(last(['a','e','b','-']))