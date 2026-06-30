"""
示範如何檢查與操作 SciPy sparse matrix。
"""

import numpy as np
from scipy.sparse import csr_matrix


def main():
    dense_matrix = np.array(
        [
            [4.0, 1.0, 0.0, 0.0],
            [1.0, 4.0, 1.0, 0.0],
            [0.0, 1.0, 4.0, 1.0],
            [0.0, 0.0, 1.0, 4.0],
        ]
    )

    matrix = csr_matrix(dense_matrix)

    # 1. 基本資訊
    print("Matrix shape:")
    print(matrix.shape)

    print("\nNumber of nonzero elements:")
    print(matrix.nnz)

    # 2. 小矩陣才能使用 toarray() 觀察
    print("\nDense representation:")
    print(matrix.toarray())

    # 3. 取得單一元素 在python中index從 0 開始
    print("\nElement at row 1, column 2:")
    print(matrix[1, 2])

    # 4. 取得一個 row 或 column
    print("\nSecond row:")
    print(matrix[1, :].toarray())

    print("\nThird column:")
    print(matrix[:, 2].toarray())

    # 5. 取得子矩陣
    submatrix = matrix[0:2, 0:2]

    print("\nTop-left 2 x 2 submatrix:")
    print(submatrix.toarray())

    # 6. 轉置矩陣
    transpose = matrix.T

    print("\nTranspose:")
    print(transpose.toarray())

    # 7. 檢查矩陣是否對稱
    difference = matrix - matrix.T

    is_symmetric = (
        difference.nnz == 0
        or np.allclose(difference.data, 0.0)
    )

    print("\nIs the matrix symmetric?")
    print(is_symmetric)

    # 8. 矩陣乘上一個 vector
    vector = np.array([1.0, 2.0, 3.0, 4.0])

    result = matrix @ vector

    print("\nVector:")
    print(vector)

    print("\nMatrix-vector multiplication:")
    print(result)

    # 9. 和 dense 計算結果比較
    dense_result = dense_matrix @ vector

    print("\n兩者計算結果相同嗎？")
    print(np.allclose(result, dense_result))


if __name__ == "__main__":
    main()