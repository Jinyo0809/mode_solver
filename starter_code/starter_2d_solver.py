import numpy as np
from scipy.sparse import diags, eye, bmat
from scipy.sparse.linalg import eigsh


def build_index_profile(
    X,
    Y,
    core_width,
    core_height,
    n_core,
    n_clad,
    core_center_x=0.0,
    core_center_y=0.0,
):
    pass


def build_scalar_fd_matrix(
    n_profile,
    wavelength,
    dx,
    dy,
):
    pass


def solve_modes(
    matrix,
    Ny,
    Nx,
    number_of_modes,
):
    pass

def main():
    wavelength = 1.55

    window_width = 3.0
    window_height = 3.0

    dx = 0.05
    dy = 0.05

    core_width = 0.50
    core_height = 0.22

    n_core = 3.48
    n_clad = 1.44

    x = np.arange(
        -window_width / 2,
        window_width / 2,
        dx,
    )

    y = np.arange(
        -window_height / 2,
        window_height / 2,
        dy,
    )

    X, Y = np.meshgrid(x, y)

    # TODO:
    # 1. 建立 n_profile
    # 2. 建立 matrix
    # 3. 求解 eigenmodes
    # 4. 畫出結果

if __name__ == "__main__":
    main()