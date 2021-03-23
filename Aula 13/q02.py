from ler_dados import lerDados

def so_no_Brasil(i):
	while True:
		try:
			x = next(i)
			if x[2] == "Brazil":
				yield x
		except StopIteration:
			return

if __name__ == "__main__":
	print([x for x in so_no_Brasil(lerDados('owid-covid-data-topicos.csv'))])