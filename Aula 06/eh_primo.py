def func(n:int) -> bool:
	''' Determina se n (>=0) é primo ''' 
	assert(n>=0)
	if n <= 1: return False
	if n == 2: return True
	if n % 2 == 0: return False
	i=3
	while i*i <= n:
		if n % i == 0: return False
		i+= 2
	return True