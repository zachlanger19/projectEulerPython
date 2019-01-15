from datetime import datetime
import numpy as np

start = datetime.now()

triangle = []
f = open("../files/p018_triangle.txt", "r")
for x in f:
    triangle.append(list(map((lambda n: int(n)), x.split(' '))))

paths = np.array(triangle[0])
triangle = triangle[1:]

for row in triangle:
    new_paths_1 = np.array(row[:-1]) + paths
    new_paths_2 = np.array(row[1:]) + paths
    paths = np.concatenate(
        (new_paths_1[:1],
         list(map((lambda x: max(x)), list(zip(new_paths_1[1:], new_paths_2[:-1])))),
         new_paths_2[-1:]))

print(max(paths))
print((datetime.now() - start).total_seconds())
