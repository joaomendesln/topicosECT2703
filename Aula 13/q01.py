from itertools import islice 
import csv

def lista_primeiros_n(arquivo, n):
	'''Retorna os n primeiros n elementos de um arquivo csv'''
	with open(arquivo) as csvfile:
		cr = csv.reader(csvfile)
		_ = next(cr)
		for x in islice(cr, n):
			yield(x)

print([x for x in lista_primeiros_n('owid-covid-data-topicos.csv',20)])