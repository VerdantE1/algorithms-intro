# algorithms-intro

实现《算法导论》（CLRS）中的核心算法，统一整理成可复用的 Python 库，并提供与书本对应的课后习题代码与解题思路（problems）。

- 语言：Python 3.10+
- 目标：学习、复现与测试经典算法；在工程代码中可直接 import 使用

## 项目结构

```
algorithms-intro/
├─ algorithms/                 # 可复用算法库
│  ├─ search/                  # 查找
│  │  ├─ __init__.py
│  │  ├─ binary_search.py
│  │  └─ linear_search.py
│  ├─ sorting/                 # 排序
│  │  ├─ bubble_sort.py
│  │  └─ insert_sort.py
│  └─ array/                   # 数组与分治
│     └─ maxSubArraySum.py
├─ problems/                   # 课后习题（按章节）
│  └─ ch02/
│     ├─ p2_3_4.py
│     ├─ p2_3_5.py
│     └─ p2_3_7.py
└─ README.md
```

## 快速开始

推荐在仓库根目录运行代码，或将仓库根目录加入 PYTHONPATH 以便全局导入。

- 临时添加（当前终端会话有效）：
  - PowerShell
    ```powershell
    $env:PYTHONPATH = "$PWD"
    ```
  - CMD
    ```cmd
    set PYTHONPATH=%CD%
    ```
- 永久添加（建议管理员终端执行）：
  - PowerShell
    ```powershell
    setx PYTHONPATH "$PWD"
    ```
  - CMD
    ```cmd
    setx PYTHONPATH %CD%
    ```

### 作为库使用

```python
from algorithms.search.binary_search import binary_search, binary_search_recursive
from algorithms.search.linear_search import linear_search, linear_search_recursive
from algorithms.sorting.bubble_sort import bubble_sort, bubble_sort_recursive
from algorithms.sorting.insert_sort import insert_sort_recursive
from algorithms.array.maxSubArraySum import (
    max_sub_array_sum_brute_force,
    max_sub_array_sum,          # 分治
    max_sub_array_sum_kadane,   # Kadane
)

A = [1, 3, 5, 7, 9]
print(binary_search(A, 0, len(A)-1, 7))  # 3

W = [5, 2, 9, 1, 5, 6]
bubble_sort_recursive(W, 0, len(W)-1)
print(W)  # 已排序

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(max_sub_array_sum_kadane(arr))  # 6
```

### 运行习题代码

- 若 problems 代码中使用库导入，直接在仓库根目录运行：
  ```powershell
  python problems/ch02/p2_3_7.py
  ```
- 或使用模块方式（需要确保 problems 为包结构并从根目录运行）：
  ```powershell
  python -m problems.ch02.p2_3_7
  ```

## 已实现与复杂度

- 查找
  - 线性查找：O(n)
  - 二分查找（递归/迭代）：O(log n)，要求有序数组
- 排序
  - 冒泡排序（迭代/递归）：O(n^2)
  - 插入排序（迭代/递归）：O(n^2)，运行时间与逆序对数 I 成正比，整体为 Θ(n + I)
- 数组与分治
  - 最大子数组和
    - 暴力：O(n^2)
    - 分治：O(n log n)
    - Kadane：O(n)
  - 逆序对数量
    - 分治: O(n log n)

## 常见问题

- ModuleNotFoundError: No module named 'algorithms'
  - 确认在仓库根目录运行，或按“快速开始”添加 PYTHONPATH
- 递归/原地排序返回值
  - 排序函数多为原地修改列表（in-place），返回值通常不必接收

## 开发与测试建议

- 使用 VS Code：
  - 推荐安装 Python 扩展，启用 Test Explorer 组织单元测试
  - 在仓库根目录打开终端，确保 PYTHONPATH 指向根目录
- 单元测试（建议逐步补充到 tests/ 目录）

## 参考

- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein. Introduction to Algorithms.

## 许可证

MIT（可按需修改）
