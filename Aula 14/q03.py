def dif(i):
	b = ''
	while True:
		try:
			a = next(i) if b == '' else b
			b = next(i)
			yield b - a
		except StopIteration:
			return

from itertools import tee

l = [1,4,3,5]
it = iter(l)
it1, it2 = tee(it)
_ = next(it2) # descartar o primeiro elemento de it2
z = zip(it1, it2)

print([x[1] - x[0] for x in z])

print([x for x in dif(y for y in [1,4,3,5])])