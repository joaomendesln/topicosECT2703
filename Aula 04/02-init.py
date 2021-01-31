from typing import List, TypeVar

T1 = TypeVar('T1')

def init(l1:List[T1]) -> List[T1]:
	'''Retorna uma lista com exceção do seu último elemento'''

	return l1[:-1]

print(init([1,2,3]))

print(init(['a','e','b','-']))