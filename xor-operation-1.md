# Problem statement in short

Given an array, find the minimum value of:  
`(A[i] AND A[j]) XOR (A[i] OR A[j])` where `i =/= j`  

1st line: Number of test cases.  
Next line: Array size of first test case  
Next line: actual array  

### Example input
```
2
5
1 2 3 4 5
3
2 4 7
```

### Expected output
```
1
3
```

#### Explanation
For 1st array, min XOR value is for `(2 AND 3) XOR (2 OR 3)`. 
For 2nd array, min XOR value is for `(4 AND 7) XOR (4 OR 7)`.  

## Solution

https://www.youtube.com/watch?v=jmD5V4yRMsw  
2 concepts:
- `(a & b) ^ (a | b)` is same as simple XOR `a ^ b`
- For minimum XOR value, reverse sort the array, compare only XORs of two subsequent elements.

```python
results = []
arrays = []

t = int(input())

# input
for i in range(t):
    size = int(input()) # never used
    arr = [int(x) for x in input().split()]
    arrays.append(arr)

# find minimum xor
for arr in arrays:
    l = len(arr)
    arr.sort(reverse=True)
    lowestXor = 999999999999999
    for i in range(l-1):
        ptr = arr[i]
        ptrNxt = arr[i+1]

        xorValue = ptr ^ ptrNxt
        if (xorValue < lowestXor):
            lowestXor = xorValue

    results.append(lowestXor)

# output
for r in results:
    print(r, end = '\n')
    
```
