#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200000, and each company has an integer m_i representing the number of employees where 1 ≤ m_i ≤ 200000. The salaries of all employees are positive integers not exceeding 10^9, and the total number of employees across all companies does not exceed 200000.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `arr` contains the maximum values from each iteration's input, `arr2` contains the first elements of each input list, `maxval` is the maximum value from all elements of `arr`.
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `i` is `n`, `ans` is the sum of `(maxval - arr[i]) * arr2[i]` for all `i` from 0 to `n-1`, `arr` contains the maximum values from each iteration's input, `arr2` contains the first elements of each input list, `maxval` is the maximum value from all elements of `arr`.
    print(ans)
#Overall this is what the function does:The function reads an integer `n`, which represents the number of companies, and then for each company, it reads a list of integers where the first integer indicates the number of employees and the subsequent integers represent the employees' salaries. It calculates the maximum salary within each company's list, finds the overall maximum salary among all companies, and computes a total adjustment cost as the sum of the differences between this overall maximum salary and each company's maximum salary, multiplied by the number of employees in that company. Finally, it prints this total adjustment cost.

