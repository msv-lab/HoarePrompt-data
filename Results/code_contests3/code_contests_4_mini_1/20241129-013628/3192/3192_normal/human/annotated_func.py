#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 200000. Each company is described by a positive integer m_i (the number of employees) followed by m_i positive integers representing the salaries of the employees, where the total number of employees across all companies does not exceed 200000 and all salaries are positive integers not exceeding 10^9.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 200000; `arr` contains the maximum values from each of the `n` lists; `maxval` is the maximum value in `arr`; `arr2` contains the sizes of each of the `n` lists; `i` is `n - 1`; `arr1` is the last list of integers processed; `temp` is the maximum value from the last `arr1` excluding the first element.
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 200000; `arr` contains the maximum values from each of the `n` lists; `maxval` is the maximum value in `arr`; `arr2` contains the sizes of each of the `n` lists; `i` is `n - 1`; `arr1` is the last list of integers processed; `temp` is the maximum value from the last `arr1` excluding the first element; `ans` is updated to the total sum of `(maxval - arr[i]) * arr2[i]` for all `i` from 0 to `n-1`.
    print(ans)
#Overall this is what the function does:The function accepts input for a number of companies, each defined by a number of employees and their respective salaries, and calculates a total based on the difference between the highest salary among all companies and the maximum salary of each company, weighted by the number of employees in each company. It prints this total. The function does not handle any edge cases for invalid input, such as non-positive integers or malformed salary data.

