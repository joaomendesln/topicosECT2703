from functools import reduce
import operator

l = [1,2,3,4,5]

print(reduce(operator.add, map(lambda x:1,l)))