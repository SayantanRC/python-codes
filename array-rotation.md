# Problem statement in short

Rotate an array by a given amount.

1st line: Number of test case.
Next line: 2 integers, 1st integer - array size, 2nd integer - rotation amount.
Next line: Actual array to be rotated.

### Example input
```
1
5 2
1 2 3 4 5
```

### Expected output
```
4 5 1 2 3
```

## Solution

```python
results = []

# test case input
t = int(input())

for i in range(t):
    line = input().split()
    arrSize = int(line[0])
    rotationAmount = int(line[1])

    # eliminate case like arrSize = 4, rotation = 46
    # In this case correct rotation should be 46 % 4 = 2
    rotationAmount = rotationAmount % arrSize

    # array input
    arr = [int(x) for x in input().split()]

    divider = arrSize - rotationAmount  # rotated array is arr[divider -> end] + arr[0 -> divider]
    endPart = arr[divider:]
    startPart = arr[:divider]
    rotatedArr = endPart + startPart

    rotatedArrInString = " ".join( [str(x) for x in rotatedArr] )

    results.append(rotatedArrInString)

for r in results:
    print(r, end = '\n')
```
