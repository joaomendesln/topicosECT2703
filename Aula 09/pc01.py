from typing import Iterable, Iterator, TypeVar

T1 = TypeVar('T1')

def agrupar(c: Iterable[T1], n:int) -> Iterator[Iterable[T1]]:
	i = iter(c)
	while True:
		l = []
		try:
			for x in range(n):
				l.append(next(i))
		except StopIteration:
			return

		yield l

print(list(agrupar(range(10),3)))
print(list(agrupar(['a','b','c','d','e','f','g','h','i','j','k'],2)))

g = agrupar(range(10),3)
print(next(g))
print(next(g))
print(next(g))