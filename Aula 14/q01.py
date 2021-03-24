import csv
from datetime import date
from collections import namedtuple

def para_int(s):
	return 0 if s == '' else int(s)

def rowdata():
	url = "./owid-covid-data-topicos.csv"

	with open(url) as cvsfile:
		cr = csv.reader(cvsfile)
		# Utilizar a primera linha com os nomes das colunas
		Dado = namedtuple("Dado", next(cr))
		for l in cr:
			yield Dado(l[0],l[1],l[2],date.fromisoformat(l[3]),para_int(l[4]),para_int(l[5]),para_int(l[6]),para_int(l[7]))

if __name__ == "__main__":
	it = ( (d.date, d.location, d.new_deaths) for d in rowdata() if d.new_deaths >= 1500 and d.continent == "Europe")

	print(list(it))