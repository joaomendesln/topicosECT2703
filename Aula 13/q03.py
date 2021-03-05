def mais_quatro_car(s:str) -> bool:
	return len(s) > 4

l1 = ["lorem", "ipsum", "dolor", "sit", "amet"]
l2 = ["lorem", "ipsum", "dolor"]

print(all(map(mais_quatro_car, l1)))
print(all(map(mais_quatro_car, l2)))