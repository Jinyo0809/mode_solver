import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh


def build_index_profile(
    x,
    core_width,
    n_core,
    n_clad,
    core_center=0.0,
):
    """建立一維 slab waveguide 的折射率分布。"""

    # TODO:
    # 1. 建立 core mask
    # 2. 建立 n_profile

    pass


def build_fd_matrix(
    n_profile,
    wavelength,
    dx,
):
    """建立一維 scalar finite-difference matrix。"""

    # TODO:
    # 1. 計算 k0
    # 2. 計算 finite-difference coefficient
    # 3. 建立 main diagonal
    # 4. 建立 off diagonal
    # 5. 回傳 sparse matrix

    pass


def solve_modes(
    matrix,
    number_of_modes,
):
    """求解 eigenvalues 與 eigenvectors。"""

    # TODO:
    # 1. 使用 eigsh
    # 2. 排序 eigenvalues
    # 3. 計算 neff

    pass


def main():
    wavelength = 1.55
    core_width = 0.5
    n_core = 1.50
    n_clad = 1.45
    dx = 0.02

    x = np.arange(-2.0, 2.0, dx)

    # TODO:
    # 完成 solver flow


if __name__ == "__main__":
    main()