from itertools import islice 
from ler_dados import lerDados

print([x for x in islice(lerDados('owid-covid-data-topicos.csv'),20)])