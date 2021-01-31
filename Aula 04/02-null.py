from typing import List, TypeVar

T1 = TypeVar('T1')

def null(l1:List[T1]) -> bool:
	'''Checa se uma lista é vazia'''
	
	return l1 == []

print(null([1,2,3]))

print(null(['a','e','b','-']))

print(null([]))