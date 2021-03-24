from q01 import *

def interval_datas_pais(init, fim, pais, data):
	return filter(lambda row: row.date > init and row.date < fim and row.location == pais, data)

if __name__ == "__main__":
	print([x for x in interval_datas_pais(date('2021-02-09'), date('2021-03-09'),'Brazil',rowdata())])