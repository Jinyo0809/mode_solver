"""
在計算finite difference mode solver時 通常會使用 sparse matrix 來儲存有限差分矩陣。
因為有限差分矩陣通常是三對角矩陣，只有少數元素是非零的，因此使用 sparse matrix 可以節省記憶體空間。
sparse matrix在儲存資料的時候只會儲存非零元素，並且使用壓縮的方式來儲存索引，因此可以大幅減少記憶體使用量。

目的：
1. 示範 dense matrix 與 sparse matrix 的差別
2. 學習使用 scipy.sparse.diags 建立三對角矩陣
3. 理解 shape、nnz 與記憶體使用量
4. 為什麼 finite-difference solver 應使用 sparse matrix
"""

import numpy as np
from scipy.sparse import diags


def main():
    # --------------------------------------------------
    # Part 1：建立一個小型三對角矩陣
    # --------------------------------------------------

    matrix_size = 6

    main_diagonal = np.full(matrix_size, -2.0)
    off_diagonal = np.ones(matrix_size - 1)

    sparse_matrix = diags(
        diagonals=[
            off_diagonal,
            main_diagonal,
            off_diagonal,
        ],
        offsets=[-1, 0, 1],
        format="csr",
    )

    print("Sparse matrix object:")
    print(sparse_matrix)

    print("\nMatrix shape:")
    print(sparse_matrix.shape)

    print("\nNumber of nonzero elements, nnz:")
    print(sparse_matrix.nnz)

    # 小矩陣可以轉成 dense，方便觀察
    dense_matrix = sparse_matrix.toarray()

    print("\nDense representation:")
    print(dense_matrix)

    # --------------------------------------------------
    # Part 2：建立一個較大的矩陣
    # --------------------------------------------------

    large_size = 10_000

    large_main = np.full(large_size, -2.0)
    large_off = np.ones(large_size - 1)

    large_sparse_matrix = diags(
        diagonals=[
            large_off,
            large_main,
            large_off,
        ],
        offsets=[-1, 0, 1],
        format="csr",
    )

    print("\nLarge sparse matrix shape:")
    print(large_sparse_matrix.shape)

    print("\nLarge sparse matrix nnz:")
    print(large_sparse_matrix.nnz)

    large_sparse_memory_bytes = (
        large_sparse_matrix.data.nbytes
        + large_sparse_matrix.indices.nbytes
        + large_sparse_matrix.indptr.nbytes
    )

    # 如果用 dense 儲存，總元素數是 N^2
    estimated_dense_memory_bytes = (
        large_size * large_size * 8
    )

    print("\nEstimated dense memory usage:")
    print(
        f"{estimated_dense_memory_bytes / 1024**2:.2f} MB"
    )

    print("\nActual sparse memory usage:")
    print(
        f"{large_sparse_memory_bytes / 1024**2:.2f} MB"
    )

    print(
        "\n在這個例子中，使用 sparse matrix 可以節省大量的記憶體空間，"
    )


if __name__ == "__main__":
    main()