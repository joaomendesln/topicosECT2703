from typing import List, Iterable, Iterator, TypeVar

T1 = TypeVar('T1')

def repete_inf (n:int) -> Iterator:
	while True:
		yield n


def primeiros(n, seq) -> Iterator:
    for i in range(n):
        try:
            v = next(seq)
            yield v
        except StopIteration:
            break

def repete_n (n: int) -> List[int]:
	return list(primeiros(n, repete_inf(n)))


def seqinf() -> Iterator:
    i = 1
    while True:
        yield i
        i+=1

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

def seq() -> Iterator:
	cont = 1
	l = []
	while True:
		l.append(repete_n(cont))
		yield list(elementos_da_lista(l))
		cont += 1

g = seq()
print(next(g))
print(next(g))
print(next(g))