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
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 0, `arr` is a list of maximum values from each iteration of `arr1`, `maxval` is the maximum value in `arr`, `i` is equal to `n`, `j` is equal to the length of the last `arr1` in the loop, `temp` is the maximum value in the last `arr1`, `arr2` is a list of the first elements of each `arr1`.
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 0, `arr` is a list of maximum values from each iteration of `arr1`, `maxval` is the maximum value in `arr`, `i` is equal to `n`, `j` is equal to the length of the last `arr1`, `temp` is the maximum value in the last `arr1`, `arr2` is a list of the first elements of each `arr1`, `ans` is the sum of all the calculated values in the loop
    print(ans)
#Overall this is what the function does:The function reads an integer `n` from the user, then iterates `n` times to read lists of integers. For each list, it calculates the maximum value excluding the first element, stores it in `arr`, and adds the first element to `arr2`. It then calculates the sum of products of the difference between the maximum value and each element in `arr` multiplied by the corresponding element in `arr2`, and prints the result.

