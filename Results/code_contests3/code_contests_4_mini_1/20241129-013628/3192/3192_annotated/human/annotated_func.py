#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 200,000; each company has a positive integer m_i representing the number of its employees (1 ≤ m_i ≤ 200,000), followed by m_i positive integers representing the salaries of the employees, where each salary does not exceed 10^9; the total number of employees across all companies does not exceed 200,000.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 200,000; `arr` contains the maximum values from each `arr1`, `arr2` contains the first elements from each `arr1`, `maxval` is the maximum value in `arr`, `i` is `n - 1`.
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `ans` is the sum of (maxval - arr[i]) * arr2[i] for all i in range(n), `i` is n, `n` is a positive integer such that 1 ≤ `n` ≤ 200,000, `arr` contains maximum values, `arr2` contains first elements from each `arr1`, `maxval` is the maximum value in `arr`.
    print(ans)
#Overall this is what the function does:The function reads input data for `n` companies, each with a number of employees and their corresponding salaries. It calculates the maximum salary for each company and determines the sum of differences between the maximum salary of all companies and each company's maximum salary, multiplied by the number of employees in that company. Finally, it prints this sum. The function does not accept any parameters directly.

