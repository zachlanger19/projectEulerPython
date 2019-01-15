sum_of_squares = 0
sum = 0
for i in range(1, 101):
    sum_of_squares += i * i
    sum += i

result = (sum * sum) - sum_of_squares

print(result)