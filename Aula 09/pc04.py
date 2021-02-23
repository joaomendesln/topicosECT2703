from typing import Iterable, Iterator, TypeVar

T1 = TypeVar('T1')

def posicoes_pares(l: Iterable[T1]) -> Iterator[T1]:
	cont = 0
	for x in l:
		if cont % 2 == 1:
			yield x
		cont += 1

def posicoes_pares2(l: Iterable[T1]) -> Iterator[T1]:
	cont = 0
	i = iter(l)
	while True:
		try:
			if cont % 2 == 1:
				yield next(i)
			else:
				next(i)
			cont += 1

		except StopIteration:
			return

l = [5,-1,4,3,7,13,51]

g = (v for i,v in enumerate(l) if i % 2 == 1)

print(list(posicoes_pares(l)))
print(list(posicoes_pares2(l)))
print(list(g))