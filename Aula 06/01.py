import eh_primo

n = 10

fat = [x for x in range(n) if eh_primo.func(x) and n % x == 0]

print(fat)