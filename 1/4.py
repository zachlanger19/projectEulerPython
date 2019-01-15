result = 0
for i in range(1000, 100, -1):
    for j in range(1000, 100, -1):
        ij = i * j
        if ij < result:
            break
        if str(ij) == str(ij)[::-1]:
            result = ij

print(result)
