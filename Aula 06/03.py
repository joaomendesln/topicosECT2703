def func(l1, l2):
	'''Gera uma sequência de tuplas cujos primeiros elementos pertencem à primeira lista de entrada e os segundos, à segunda lista de entrada'''
	for x, y in zip(l1, l2):
		yield (x, y)

l1 = [1,2,3]
l2 = ["a","b","c"]
res = list(func(l1,l2))
print(res)