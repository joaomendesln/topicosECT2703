from typing import Iterable, Iterator, TypeVar, Callable

T1 = TypeVar('T1')

def meu_filter(f: Callable[[T1], bool], l: Iterable[T1]) -> Iterator[T1]:
	for x in l:
		if f(x):
			yield x

def eh_par(n : int) -> bool:
	return True if n % 2 == 0 else False

l = [7,4,6,1,10,3]

g = meu_filter(eh_par, l)
print(next(g))
print(next(g))
print(next(g))