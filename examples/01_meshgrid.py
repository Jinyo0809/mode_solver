"""
目的：
1. 如何建立mesh grid
2. mesh grid 的使用方式
3. mesh grid 的索引方式
"""

import numpy as np

x = np.arange(-1, 1, 0.5)
y = np.arange(-1, 1, 0.5)

X, Y = np.meshgrid(x, y)

print("X:")
print(X)
print("Y:")
print(Y)

# 在這個新座標中，點的座標為 (X[i,j], Y[i,j])，其中 i 和 j 分別是 X 和 Y 的索引。
print("Point coordinates:")
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        print(f"Point ({i}, {j}): ({X[i, j]}, {Y[i, j]})")

