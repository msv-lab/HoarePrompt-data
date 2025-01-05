#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200,000), and each company has a positive integer m_i (1 ≤ m_i ≤ 200,000) followed by m_i positive integers representing the salaries of the employees, where all salaries do not exceed 10^9. The total number of employees across all companies does not exceed 200,000.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `arr` contains `n` maximum values from each `arr1`, `arr2` contains `n` values corresponding to the first element of each `arr1`, `maxval` is the maximum value in `arr`.
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `arr` contains `n` maximum values from each `arr1`, `arr2` contains `n` values corresponding to the first element of each `arr1`, `maxval` is the maximum value in `arr`, `ans` is the accumulated result of `(maxval - arr[i]) * arr2[i]` for all `i` from `0` to `n-1`.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer `n`, processes salaries from `n` companies to find the maximum salary per company, calculates a total based on the differences between the overall maximum and each company's maximum salary multiplied by the number of employees, and prints the accumulated result.

