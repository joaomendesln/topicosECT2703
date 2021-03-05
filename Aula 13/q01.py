from typing import List
import operator
from functools import reduce

def list_n_to_1(n:int) -> List[int]:
	return list(x + 1 for x in range(n))

print(reduce(operator.mul, list_n_to_1(5)))