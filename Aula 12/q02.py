from functools import reduce
import operator

l = [4,6,1,3,8,6,9,0]

print(reduce(operator.add,l[0::2]))