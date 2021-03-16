from datetime import date
import csv

def para_int(s):
	return 0 if s == '' else int(s)

def novos_casos_dia(arquivo, pais):
	'''Retona uma tupla com o dia e quantidade de casos novos de um pais do mês atual'''
	with open(arquivo) as csvfile:
		cr = csv.reader(csvfile)
		_ = next(cr)
		for x in cr:
			if date.fromisoformat(x[3]).month == date.today().month and date.fromisoformat(x[3]).year == date.today().year:
				if x[2] == pais:
					yield(date.fromisoformat(x[3]), para_int(x[5]))
				elif pais == '':
					yield(date.fromisoformat(x[3]), para_int(x[5]))

result = [x for x in novos_casos_dia('owid-covid-data-topicos.csv', 'Brazil')]

for x in result:
	print(f'{x[0]} ---> {x[1]}')