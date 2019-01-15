from utils.number_theory import NumberTheory

result = 0
result_chain_length = 0

for i in range(1, 1000000):
    if NumberTheory.collatz_distance(i) > result_chain_length:
        result = i
        result_chain_length = NumberTheory.collatz_distance(i)

print(result)
