from q04 import *

def novos_casos_dia(data, i):
	while True:
		try:
			x = next(i)
			if date.fromisoformat(x[3]) == date.fromisoformat(data):
				yield x
		except StopIteration:
			return

def novos_casos_dia_continente(continente, i):
	while True:
		try:
			x = next(i)
			if x[1] == continente:
				yield x
		except StopIteration:
			return

if __name__ == "__main__":
	print(sum([para_int(x[5]) for x in novos_casos_dia('2021-01-01', novos_casos_dia_continente('Asia', lerDados('owid-covid-data-topicos.csv')))]))
	print(sum([para_int(x[5]) for x in novos_casos_dia_continente('Europe', novos_casos_dia('2021-02-02', lerDados('owid-covid-data-topicos.csv')))]))