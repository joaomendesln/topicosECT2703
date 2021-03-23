from q03 import *
from datetime import date

if __name__ == "__main__":
	result = [(date.fromisoformat(x[3]), para_int(x[5])) for x in so_no_Brasil(lerDados('owid-covid-data-topicos.csv'))]

	for x in result:
		print(f'{x[0]} ---> {x[1]}')
