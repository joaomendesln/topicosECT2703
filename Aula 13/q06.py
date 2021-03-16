from datetime import date
import csv
import operator
from functools import reduce

def para_int(s):
	return 0 if s == '' else int(s)

def novos_casos_dia_continente(arquivo, data, continente):
	'''Retona uma tupla com o dia e quantidade de casos novos de um pais do mês atual'''
	with open(arquivo) as csvfile:
		cr = csv.reader(csvfile)
		_ = next(cr)
		for x in cr:
			if date.fromisoformat(x[3]) == date.fromisoformat(data):
				if x[1] == continente:
					yield(para_int(x[5]))

print(reduce(operator.add, [x for x in novos_casos_dia_continente('owid-covid-data-topicos.csv', '2021-01-01', 'Asia')]))

print(reduce(operator.add, [x for x in novos_casos_dia_continente('owid-covid-data-topicos.csv', '2021-02-02', 'Europe')]))