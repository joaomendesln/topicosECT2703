from typing import List, TypeVar

T1 = TypeVar('T1')

def drop(n:int, l1:List[T1]) -> List[T1]:
	'''Retorna uma lista com exceção dos seus n primeiros elementos'''

	return l1[n:]

print(drop(1, [1,2,3]))

print(drop(10, ['a','e','b','-']))