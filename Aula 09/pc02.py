from typing import Iterable, Iterator, TypeVar

T1 = TypeVar('T1')

def elementos_da_lista(c:Iterable[Iterable[T1]]) -> Iterator[T1]:
	i = iter(c)
	while True:
		try:
			g = next(i)
			h = iter(g)
			for x in g:
				yield next(h)
		except StopIteration:
			return


l = [[1,2,3],[4,5],[],[6,7]]

print(list(elementos_da_lista(l)))

g = list(y for x in l for y in x)
print(g)