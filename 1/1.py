# result = 0
# for i in range(1, 1001):
#     result += i if i % 3 == 0 or i % 5 == 0 else 0
# print(result)

print(sum([i for i in range(1, 1001) if i % 3 == 0 or i % 5 == 0]))
