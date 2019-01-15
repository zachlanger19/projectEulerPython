from utils.number_theory import NumberTheory

result = 28
i = 8
while NumberTheory.number_of_divisors(result) < 500:
    result += i
    i += 1

print(result)
