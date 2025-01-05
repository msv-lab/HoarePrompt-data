#State of the program right berfore the function call: **
def func():
    n = int(raw_input())
    arr = []
    maxval = 0
    arr2 = []
    for i in xrange(n):
        arr1 = list(map(int, raw_input().split()))
        
        temp = 0
        
        for j in xrange(1, arr1[0]):
            temp = max(temp, arr1[j])
        
        arr.append(temp)
        
        arr2.append(arr1[0])
        
        maxval = max(arr[i], maxval)
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `arr` contains the maximum values in each `arr1`, `maxval` is the maximum value among all `arr1`, `arr2` contains the first elements of all `arr1`, `i` is equal to `n-1`, `arr1` is a list of integers created by mapping input values to integers after splitting, `temp` is the maximum value in the last `arr1`, `j` is increased by 1 until it reaches the last element of `arr1`, `temp` is updated to be the maximum value in the last `arr1`, `arr` contains the appended maximum values, `arr2` contains the first elements of all `arr1`.
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `ans` is the sum of the products of `(maxval - arr[i]) * arr2[i]` for each `i` in the range of `n`.
    print(ans)
#Overall this is what the function does:The function `func` reads an integer `n` from input, then iterates `n` times to read input values and calculate the maximum values within those inputs. It then calculates a final result `ans` based on the maximum values and their corresponding first elements. Finally, it prints the sum of these calculated values. The function does not accept any parameters or return any value.

