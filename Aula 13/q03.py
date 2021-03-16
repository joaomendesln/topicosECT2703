import csv

def para_int(s):
	return 0 if s == '' else int(s)

def novos_casos_dia(arquivo, pais):
	'''Retona uma tupla com o dia e quantidade de casos novos de um pais'''
	with open(arquivo) as csvfile:
		cr = csv.reader(csvfile)
		_ = next(cr)
		for x in cr:
			if x[2] == pais:
				yield(x[3], para_int(x[5]))
			elif pais == '':
				yield(x[3], para_int(x[5]))

result = [x for x in novos_casos_dia('owid-covid-data-topicos.csv', 'Brazil')]

for x in result:
	print(f'{x[0]} ---> {x[1]}')
