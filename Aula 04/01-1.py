from typing import List, TypeVar

T1 = TypeVar('T1')

def elemRepet(l:List[T1]) -> bool:
	'''Checa se uma lista tem algum elemento repetido'''
	for (i,v) in enumerate(l):
		if v in l[:i] + l[i+1:]:
			return True

	return False

print(elemRepet([1,2,3,1]))
print(elemRepet([1,2,2,3]))
print(elemRepet(['a','e','b']))