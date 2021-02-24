from typing import Iterable, Iterator, TypeVar, List

T1 = TypeVar('T1')

def elementos_da_lista(c:Iterable[Iterable[T1]]) -> Iterator[T1]:
	i = iter(c)
	while True:
		try:
			g = next(i)
			for x in g:
				yield x
		except StopIteration:
			return


l : List[List[int]] = [[1,2,3],[4,5],[],[6,7]]

print(list(elementos_da_lista(l)))

g = list(y for x in l for y in x)
print(g)