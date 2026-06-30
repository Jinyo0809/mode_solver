# Week 4：模態判讀與數值驗證

## 1. 本週目標

本週使用 Week 3 完成的二維 solver，判斷計算結果是否具有合理的物理意義，並檢查數值結果是否收斂。

完成後，應能：

* 分辨 fundamental、higher-order 與 box-like modes
* 利用 $n_\mathrm{eff}$、mode profile 與 node 判讀模態
* 進行 grid convergence test
* 進行 computational-window convergence test
* 說明 scalar approximation 的限制

---

## 2. 本週使用的檔案

請使用：

* Week 3 完成的 `2d_solver.py`
* Week 3 產生的 mode profiles
* `notes/theory_notes.pdf`

本週不需要重寫 solver，主要工作是改變參數、整理結果並解釋其物理意義。

---

## 3. 任務一：判讀前六個 eigenmodes

整理前六個 eigenpairs：

| Mode | $n_\mathrm{eff}$ | 場集中於核心？ | 有無 node？ | 邊界場大小 | 初步判斷 |
| ---: | ---------------: | :------ | :------- | :---- | :--- |
|    0 |              ... | ...     | ...      | ...   | ...  |
|    1 |              ... | ...     | ...      | ...   | ...  |
|    2 |              ... | ...     | ...      | ...   | ...  |
|    3 |              ... | ...     | ...      | ...   | ...  |
|    4 |              ... | ...     | ...      | ...   | ...  |
|    5 |              ... | ...     | ...      | ...   | ...  |

對均勻 cladding 的簡單波導，可先利用：

```math
n_\mathrm{clad}
<
n_\mathrm{eff}
<
n_\mathrm{core}
```

篩選 guided-mode candidates。

判讀時請同時觀察：

* $n_\mathrm{eff}$
* 場是否集中在核心
* 是否有 node 或 nodal line
* 場是否在計算邊界附近衰減

通常：

* fundamental-mode candidate 沒有明顯 node，且場集中在核心
* higher-order guided-mode candidate 具有一條或多條 node
* box-like mode 的場通常延伸到大部分計算視窗，且容易受到邊界影響

請注意，`Mode 0`、`Mode 1` 只是排序後的編號，不是固定的物理名稱。

---

## 4. 任務二：比較 amplitude 與 intensity

選擇至少兩個 modes，同時畫出：

```math
U(x,y)
```

與：

```math
|U(x,y)|^2
```

請回答：

1. 為什麼 amplitude 有正值與負值？
2. 為什麼 intensity 不會有負值？
3. node 在兩種圖中有什麼差異？
4. 為什麼只看 intensity 無法判斷場的正負相位？
5. 哪一個 mode 沒有 node？
6. 哪一個 mode 具有明顯 nodal line？

---

## 5. 任務三：Grid convergence test

固定：

* wavelength
* core width
* core height
* core index
* cladding index
* computational-window size

只改變：

```text
dx = dy = 0.08 um
dx = dy = 0.06 um
dx = dy = 0.05 um
dx = dy = 0.04 um
dx = dy = 0.03 um
```

每次記錄 fundamental-mode candidate 的 $n_\mathrm{eff}$。

| $dx=dy$ | $N_x$ | $N_y$ | Matrix size | $n_\mathrm{eff}$ |
| ------: | ----: | ----: | ----------: | ---------------: |
|     ... |   ... |   ... |         ... |              ... |

並畫出 $n_\mathrm{eff}$ 隨 grid spacing 的變化。

請回答：

1. 網格變細後， $n_\mathrm{eff}$ 是否逐漸穩定？
2. matrix size 與執行時間如何改變？
3. 最粗網格是否足以描述波導核心？
4. mode profile 是否逐漸穩定？

---

## 6. 任務四：Computational-window convergence test

固定：

* `dx`
* `dy`
* wavelength
* 波導核心尺寸
* 折射率

只改變計算視窗，例如：

```text
2 um x 2 um
3 um x 3 um
4 um x 4 um
5 um x 5 um
```

每次記錄 fundamental-mode candidate 的 $n_\mathrm{eff}$ 與 edge ratio。

```math
\text{edge ratio}
=
\frac{\max_{\mathrm{boundary}}|U|}
{\max_{\mathrm{all}}|U|}
```

參考程式：

```python
mode_abs = np.abs(mode_2d)

edge_max = max(
    np.max(mode_abs[0, :]),
    np.max(mode_abs[-1, :]),
    np.max(mode_abs[:, 0]),
    np.max(mode_abs[:, -1]),
)

edge_ratio = edge_max / np.max(mode_abs)
```

整理成表格：

| Window size | $N_x$ | $N_y$ | $n_\mathrm{eff}$ | Edge ratio |
| ----------: | ----: | ----: | ---------------: | ---------: |
|         ... |   ... |   ... |              ... |        ... |

請回答：

1. 視窗增大後，$n_\mathrm{eff}$ 是否逐漸穩定？
2. edge ratio 是否降低？
3. guided mode 是否比 box-like mode 穩定？
4. 為什麼 box-like mode 會受到計算視窗影響？
5. 目前使用的計算視窗是否足夠大？

請注意，edge ratio 沒有適用於所有問題的固定門檻，主要用來比較不同視窗與不同 modes。

---

## 7. Scalar approximation 的限制

在這裡，我們求解：

```math
\left[
\frac{1}{k_0^2}\nabla_t^2+n^2(x,y)
\right]U
=
n_\mathrm{eff}^2U
```

其中 $U$ 是單一 scalar field。

因此此模型沒有完整描述：

* $E_x$ 、 $E_y$ 、 $E_z$
* $H_x$ 、 $H_y$ 、 $H_z$
* 不同場分量之間的耦合
* 高折射率介面的完整 Maxwell boundary conditions
* 真正的 quasi-TE / quasi-TM hybrid modes

因此

```math
\text{numerical convergence}
\neq
\text{physical-model accuracy}
```

也就是說，grid 與 window convergence 良好，只代表數值結果收斂到 scalar model 的解，不代表它一定等於 full-vector Maxwell solver 的結果。

---

## 8. 本週作業

* 更新後的 `2d_solver.py`
* 前六個 eigenmodes 的 summary table
* amplitude 與 intensity 圖
* grid convergence 表格與圖
* window convergence 表格與圖
* edge ratio 結果


問題：

1. 哪一個 mode 是 fundamental-mode candidate？
2. 哪些 modes 可能是 higher-order guided modes？
3. 哪些 modes 可能是 box-like modes？
4. grid convergence 的結果如何？
5. window convergence 的結果如何？
6. scalar approximation 的主要限制是什麼？

---

## 9. 選做：修改波導幾何

將 rectangular core 改成 circular、rib、ridge、coupled waveguides 或其他簡單結構。

只修改 `core_mask` 或 `n_profile`，不要重寫 matrix builder 與 eigensolver。

比較新結構與矩形波導的：

* mode profile
* $n_\mathrm{eff}$
* 模態對稱性
* higher-order modes
