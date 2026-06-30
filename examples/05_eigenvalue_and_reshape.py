"""
示範：
1. 如何取得 eigenvalues 與 eigenvectors
2. eigenvectors 如何儲存在矩陣的各個 columns
3. 如何排序 eigenpairs
4. 如何將一維 eigenvector reshape 成二維陣列
"""

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigsh


def main():
    # --------------------------------------------------
    # Part 1：用小型對稱矩陣理解 eigenpair
    # --------------------------------------------------

    dense_matrix = np.array(
        [
            [2.0, 1.0, 0.0],
            [1.0, 2.0, 1.0],
            [0.0, 1.0, 2.0],
        ]
    )

    eigenvalues, eigenvectors = np.linalg.eigh(
        dense_matrix
    )

    print("Eigenvalues returned by np.linalg.eigh:")
    print(eigenvalues)

    print("\nEigenvector matrix:")
    print(eigenvectors)

    print("\nShape of eigenvalues:")
    print(eigenvalues.shape)

    print("\nShape of eigenvectors:")
    print(eigenvectors.shape)

    # eigenvectors[:, i] 是第 i 個 eigenvalue 對應的 eigenvector
    for index in range(len(eigenvalues)):
        eigenvalue = eigenvalues[index]
        eigenvector = eigenvectors[:, index]

        print(f"\nEigenpair {index}")
        print("Eigenvalue:")
        print(eigenvalue)

        print("Eigenvector:")
        print(eigenvector)

        # 驗證 A v = lambda v
        left_side = dense_matrix @ eigenvector
        right_side = eigenvalue * eigenvector

        print("A @ v:")
        print(left_side)

        print("lambda * v:")
        print(right_side)

        print(
            "Eigenpair is valid:",
            np.allclose(left_side, right_side),
        )

    # --------------------------------------------------
    # Part 2：依 eigenvalue 由大到小排序
    # --------------------------------------------------

    sort_indices = np.argsort(eigenvalues)[::-1]

    sorted_eigenvalues = eigenvalues[sort_indices]
    sorted_eigenvectors = eigenvectors[:, sort_indices]

    print("\nEigenvalues sorted from largest to smallest:")
    print(sorted_eigenvalues)

    print("\nEigenvector corresponding to largest eigenvalue:")
    print(sorted_eigenvectors[:, 0])

    # --------------------------------------------------
    # Part 3：使用 eigsh 只求部分 eigenpairs
    # --------------------------------------------------

    sparse_matrix = csr_matrix(dense_matrix)

    # which="LA" 表示求最大的 eigenvalues, k=2 表示求前兩個
    partial_values, partial_vectors = eigsh(
        sparse_matrix,
        k=2,
        which="LA",
    )

    # eigsh 不保證以我們想要的順序回傳
    partial_sort_indices = np.argsort(
        partial_values
    )[::-1]

    partial_values = partial_values[
        partial_sort_indices
    ]

    partial_vectors = partial_vectors[
        :,
        partial_sort_indices,
    ]

    print("\nTwo largest eigenvalues from eigsh:")
    print(partial_values)

    print("\nCorresponding eigenvectors:")
    print(partial_vectors)

    # --------------------------------------------------
    # Part 4：reshape 的概念
    # --------------------------------------------------

    Ny = 3
    Nx = 4

    vector = np.arange(1, Ny * Nx + 1)

    print("\nOriginal 1D vector:")
    print(vector)

    # order="C" 表示 row-major order，先填滿 row 再換 row
    matrix_c_order = vector.reshape(
        (Ny, Nx),
        order="C",
    )

    # order="F" 表示 column-major order，先填滿 column 再換 column
    matrix_f_order = vector.reshape(
        (Ny, Nx),
        order="F",
    )

    print("\nReshape with order='C':")
    print(matrix_c_order)

    print("\nReshape with order='F':")
    print(matrix_f_order)

    # 還原回原始 vector
    restored_vector = matrix_f_order.ravel(
        order="F"
    )

    print("\nRestored vector using order='F':")
    print(restored_vector)

    print(
        "\nRestored vector agrees with original:",
        np.array_equal(vector, restored_vector),
    )


if __name__ == "__main__":
    main()