from itertools import groupby

l = [1,2,3,2,1,4,1]

result = [key for key, elements in groupby(sorted(l))]

print(result)