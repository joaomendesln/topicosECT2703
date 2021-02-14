def embaralhar_rec(s1:str, s2:str) -> str:
	if len(s1) == 1:
		return s1[0] + s2[0] + s2[1:]
	if len(s2) == 1:
		return s1[0] + s2[0] + s1[1:]
	return s1[0] + s2[0] + embaralhar_rec(s1[1:],s2[1:])

def embaralhar(s1:str, s2:str) -> str:
	result = ""
	men = len(s1) if len(s1) <= len(s2) else len(s2)

	for x in range(0, men):
		result += s1[x] + s2[x]

	if len(s1) == len(s2):
		return result
	if len(s1) < len(s2):
		return result + s2[men:]
	return result + s1[men:]


print(embaralhar_rec("natal", "ola"))
print(embaralhar("natal", "ola"))