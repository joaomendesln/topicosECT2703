import csv

def filtra_pais(arquivo, pais):
	'''Retona os registro de apenas um determinado país'''
	with open(arquivo) as csvfile:
		cr = csv.reader(csvfile)
		_ = next(cr)
		for x in cr:
			if x[2] == pais:
				yield(x)

print([x for x in filtra_pais('owid-covid-data-topicos.csv', 'Brazil')])