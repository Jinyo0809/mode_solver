# Week 1：波導模態、Eigenvalue Problem 與有限差分推導

## 1. 本週目標

本週的目標是理解 mode solver 背後的物理與數學流程，並看懂連續的波動方程如何轉換成電腦可以求解的矩陣 eigenvalue problem。

完成本週內容後，應能：

* 說明波導、mode、mode profile 與傳播方向的基本意義
* 說明 propagation constant $\beta$ 與 effective index $n_\mathrm{eff}$
* 理解 scalar wave equation 的來源與適用限制
* 將 scalar wave equation 整理成 eigenvalue problem
* 使用 Taylor expansion 推導 central finite difference
* 寫出二維 five-point finite-difference equation
* 說明 $A^i , B$ 與完整 sparse matrix 的結構
* 說明 eigenvalue 與 eigenvector 在 mode solver 中的物理意義

---

## 2. 閱讀內容

請依序閱讀：

1. `notes/theory_notes.pdf`
2. README 中關於專題目標與 scalar approximation 的說明
3. 若對波導與 mode 沒有概念，再自行查閱簡單的 waveguide mode、TE/TM introductory material

閱讀時請特別注意以下流程：

```text
Maxwell equations
        ↓
scalar wave equation
        ↓
Helmholtz equation
        ↓
eigenvalue problem
        ↓
finite-difference approximation
        ↓
block sparse matrix
```

請特別確認：

* 波導沿哪一個方向傳播
* $U(x,y)$ 描述哪一個截面
* $k_0,\beta,n_\mathrm{eff}$ 的關係
* 為什麼 eigenvalue 是 $n_\mathrm{eff}^2$
* central finite difference 的來源
* 邊界條件設定在哪裡
* $A^i$ 與 $B$ 分別連接哪一個方向的鄰近網格點

---

## 3. 任務一：波導與模態的基本概念

請思考：

1. 什麼是光波導？
2. 在這個推導中，光沿哪一個方向傳播？
3. $x、y、z$ 三個方向分別代表什麼？
4. 什麼是 mode？
5. mode profile $U(x,y)$ 描述的是什麼？
6. 為什麼一個波導可能存在多個 mode？
7. fundamental mode 與 higher-order mode 的場型可能有什麼差別？
8. TE、TM 分別表示什麼？

---

## 4. 任務二：自己寫一個一維的 Finite Difference Matrix！

考慮一維 scalar wave equation：

```math
\left[
\frac{1}{k_0^2}\frac{d^2}{dx^2}
+
n^2(x)
\right]U(x)
=
n_\mathrm{eff}^2U(x)
```

將 $x$ 方向離散成均勻網格：

```math
x_i=x_0+i\Delta x
```

並使用 central finite difference：

```math
\frac{d^2U}{dx^2}\bigg|_{x_i}
\approx
\frac{
U_{i-1}-2U_i+U_{i+1}
}{
(\Delta x)^2
}
```

請將離散後的方程整理成：

```math
A\mathbf U
=
n_\mathrm{eff}^2\mathbf U
```

其中：

```math
\mathbf U
=
\begin{bmatrix}
U_1\\
U_2\\
\vdots\\
U_N
\end{bmatrix}
```

請完成以下內容：

1. 找出矩陣 $A$ 的主對角線元素
2. 找出矩陣 $A$ 的上、下對角線元素
3. 寫出完整的 tridiagonal matrix $A$
5. 說明折射率分布 $n_i$ 出現在矩陣的哪個位置
6. 說明邊界條件 $U=0$ 如何反映在矩陣中

可以先使用一個小型網格，例如：

```text
N = 3
```

手寫出完整的 $3\times3$ matrix。

---

## 5.本週作業

* 理解基本的波導與模態概念
* 能夠理解 $\beta, n_\mathrm{eff}$ 是什麼
* 能夠寫出一個1D finite difference的矩陣應該有什麼元素