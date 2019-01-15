from utils.number_theory import NumberTheory


def is_amicable(n):
    n2 = sum(NumberTheory.get_divisors(n)[:-1])
    if n2 != n and sum(NumberTheory.get_divisors(n2)[:-1]) == n:
        return True

amicable_numbers = []
for n in range(1, 10001):
    if is_amicable(n):
        amicable_numbers.append(n)

print(sum(amicable_numbers))
