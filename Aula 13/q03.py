from q02 import *

def para_int(s):
	return 0 if s == '' else int(s)

if __name__ == "__main__":
	result = [(x[3], para_int(x[5])) for x in so_no_Brasil(lerDados('owid-covid-data-topicos.csv'))]

	for x in result:
		print(f'{x[0]} ---> {x[1]}')
