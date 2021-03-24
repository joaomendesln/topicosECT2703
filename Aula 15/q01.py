from itertools import groupby
from functools import reduce

def maior (x,y):
	return x if x[1] > y[1] else y

paragrafo = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur fringilla placerat interdum. Nunc scelerisque rutrum arcu, eget fringilla lorem aliquam sit amet. Quisque risus lacus, suscipit a maximus in, facilisis eget leo. Quisque iaculis purus vitae est vulputate, vitae posuere erat vehicula. In sit amet ex congue, imperdiet orci at, porta sem. Quisque eu lorem lorem. Etiam ac tortor consequat, posuere tellus non, consectetur lectus."

pals = paragrafo.split()
pals = [x if x[-1] not in [".", ","] else x[0:-1] for x in pals]

pals = sorted(pals, key = str.lower)
result = [(k, len(list(elems))) for k, elems in groupby(pals, key = str.lower)]

if __name__ == '__main__':
	print(reduce(maior, result)[0])