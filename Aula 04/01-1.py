from typing import List, TypeVar

T1 = TypeVar('T1')

def elemRepet(l:List[T1]) -> bool:
	'''Checa se uma lista tem algum elemento repetido'''

	return len(l) > len(set(l))

print(elemRepet([1,2,3,1]))
print(elemRepet([1,2,2,3]))
print(elemRepet(['a','e','b']))