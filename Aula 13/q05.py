from q04 import *

def novos_casos_dias_por_mes(i):
	while True:
		try:
			x = next(i)
			if date.fromisoformat(x[3]).month == date.today().month and date.fromisoformat(x[3]).year == date.today().year:
				yield x
		except StopIteration:
			return

if __name__ == "__main__":
	result = [(date.fromisoformat(x[3]), para_int(x[5])) for x in novos_casos_dias_por_mes(so_no_Brasil(lerDados('owid-covid-data-topicos.csv')))]

	for x in result:
		print(f'{x[0]} ---> {x[1]}')