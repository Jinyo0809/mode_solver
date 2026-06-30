"""
目的：
1. 利用 mask 建立折射率分布
"""


import numpy as np
import matplotlib.pyplot as plt

core_width = 0.8
core_height = 0.4
n_clad = 1.44
n_core = 3.48

x = np.arange(-2, 2, 0.05)
y = np.arange(-2, 2, 0.05)

X, Y = np.meshgrid(x, y)

# 利用mask的條件來篩選出需要更改折射率的區域
core_mask = (
    (np.abs(X) <= core_width / 2)
    & (np.abs(Y) <= core_height / 2)
)

n_profile = np.full(X.shape, n_clad)

n_profile[core_mask] = n_core




# 畫畫的部分
plt.figure(figsize=(7, 5))

image = plt.imshow(
    n_profile,
    extent=[x.min(), x.max(), y.min(), y.max()],
    origin="lower",
    aspect="equal",
    cmap="viridis",
)

plt.colorbar(image, label="Refractive index")

# 畫出核心與包覆層的介面
interface_level = (n_core + n_clad) / 2

plt.contour(
    X,
    Y,
    n_profile,
    levels=[interface_level],
    colors="white",
    linewidths=1.5,
)

plt.xlabel("x (um)")
plt.ylabel("y (um)")
plt.title("Refractive Index Profile")

plt.tight_layout()
plt.show()