from utils.number_theory import NumberTheory

def find_in_list(lst, n):
    for i in lst:
        if i >= n:
            return False
        if n - i in lst:
            return True
    return False

abundant_numbers = []
for n in range(1, 28124):
    divisors = NumberTheory.get_divisors(n)[:-1]
    if sum(divisors) > n:
        abundant_numbers.append(n)

result = 0
for n in range(1, 28124):
    if find_in_list(abundant_numbers, n):
        result += n

print(result)
