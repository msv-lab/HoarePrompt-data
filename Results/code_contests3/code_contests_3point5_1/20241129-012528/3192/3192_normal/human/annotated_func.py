#State of the program right berfore the function call: n is a positive integer, and each company description contains a positive integer for the number of employees and positive integers for the salaries of those employees.**
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
        
    #State of the program after the  for loop has been executed: Output State: `n` is a positive integer, `arr` is a list with `n` elements, `maxval` is the maximum value in `arr`, `i` is `n-1`, `arr1` is a list of integers converted from the last input split by spaces, `temp` is the maximum value in `arr1`, `j` is `arr1[0] - 1`, `arr2` contains all elements of `arr1`, `maxval` is the maximum value in the final `arr`.
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `arr` is a list with `n` elements, `maxval` is the maximum value in `arr`, `i` is equal to `n-1`, `arr1` is a list of integers converted from the last input split by spaces, `temp` is the maximum value in `arr1`, `j` is `arr1[0] - 1`, `arr2` contains all elements of `arr1`, `maxval` is the maximum value in the final `arr`, `ans` is the sum of all calculations `(maxval - arr[i]) * arr2[i]` for each element in `arr`
    print(ans)
#Overall this is what the function does:The function `func` reads an integer `n` from input, then processes `n` company descriptions. Each description contains the number of employees and their salaries. It calculates the maximum salary of each company and the overall maximum salary across all companies. After that, it computes a value based on the salary differences and number of employees, and finally prints the result. The function does not have a return value. However, it seems like the annotations are not completely accurate, especially regarding the calculations and indexing in the loops. There might be potential issues in the code logic that need further verification.

