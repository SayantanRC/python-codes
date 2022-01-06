# Problem statement in short

Matrix M.  
Check for elements such that:  
`M[i][j] > M[p][q]` where `p>=i` and `q>=j`  

1st line: Test cases.  
Next line: Dimension N of square matrix for 1st case.  
Next N lines: matrix input.

### Example input:
```
2
3
1 2 3
4 5 6
7 8 9
2
4 3
1 4
```

### Expected output:
```
0
2
```

### Explanation:
In 2nd test case, `M[0][0] > M[0][1]` and `M[0][0] > M[1][0]`. So second output is 2.  
No such condition for 1st matrix where `M[i][j] > M[p][q]` where `p>=i` and `q>=j`.  

## Solution

```python
# Write your code here
matrices = []

# test case input
t = int(input())

# matrix input
for i in range(t):
    d = int(input())
    matrix = []
    for j in range(d):
        matrix.append([int(k) for k in input().split()])
    matrices.append(matrix)

results = []

# matrix check

for matrix in matrices:
    d = len(matrix)     # d for dimension
    result = 0
    for i in range(d):
        for j in range(d):      # i, j is row, column
            item = matrix[i][j]
            for _i in range(i, d):  # _i, _j is row, col, below and right side of i,j
                for _j in range(j, d):
                    _item = matrix[_i][_j]
                    if item > _item:
                        result = result + 1
    results.append(result)

for r in results:
    print(r, end='\n')

```
