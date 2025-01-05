#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200,000; each company has a positive number of employees m_i such that 1 ≤ m_i ≤ 200,000; and all salaries are positive integers not exceeding 10^9. The total number of employees across all companies does not exceed 200,000.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer within the range of 1 to 200,000; `arr` contains the maximum values from each input list, `arr2` contains the lengths of each input list, and `maxval` is the maximum value found in `arr`.
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `n` is an integer within the range of 1 to 200,000, `arr` contains the maximum values from each input list, `arr2` contains the lengths of each input list, `maxval` is the maximum value found in `arr`, `ans` is equal to the sum of `(maxval - arr[i]) * arr2[i]` for all `i` from 0 to `n-1`.
    print(ans)
#Overall this is what the function does:The function reads an integer `n` indicating the number of companies and then processes `n` lists of employee salaries. For each company, it finds the maximum salary and stores it. It then calculates the sum of the differences between the maximum salary across all companies and the maximum salary of each company multiplied by the number of employees in that company, returning this total as output. The function does not handle any exceptions or edge cases related to input validation; it assumes all inputs are valid according to the specified constraints.

