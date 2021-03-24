from rowdata import *

from itertools import groupby
from operator import attrgetter

lp = [x for x in rowdata()]

l = sorted(lp, key = attrgetter('continent'))

for k, elems in groupby(l, key = attrgetter("continent")):
	if k != '':
		print(f'Continente: {k}: {sum([x.new_cases for x in elems])}')