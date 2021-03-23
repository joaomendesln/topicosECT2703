from q06 import *
from functools import reduce

def maior (x,y):
	'''Retorna tupla que tem o maior segundo elemento'''
	return x if x[1] > y[1] else y

result = [(x[3], para_int(x[5])) for x in so_no_Brasil(lerDados('owid-covid-data-topicos.csv'))]

if __name__ == '__main__':
	print(reduce(maior, result))