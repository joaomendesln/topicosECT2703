from typing import List, Tuple, TypeVar

T1 = TypeVar('T1')
T2 = TypeVar('T2')

def meu_unzip(l: List[Tuple[T1,T2]]) -> Tuple[List[T1],List[T2]]:
	l1 = []
	l2 = []

	for x in l:
		l1.append(x[0])
		l2.append(x[1])

	return (l1, l2)


l = [(1,2),(3,4),(5,6),(7,8)]

result = ([x for (x,_) in l], [y for (_,y) in l])

print(meu_unzip(l))
print(result)