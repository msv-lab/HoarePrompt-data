#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and each company is described by an integer m_i followed by m_i positive integers representing the salaries of the employees, where the total number of employees across all companies does not exceed 2 ⋅ 10^5 and each salary is a positive integer not exceeding 10^9.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `arr` contains the maximum values from each input list (one for each iteration), `arr2` contains the lengths of each input list, `maxval` is the maximum value from all elements in `arr`.
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `arr` contains the maximum values from each input list, `arr2` contains the lengths of each input list, `maxval` is the maximum value from all elements in `arr`, `ans` is the sum of `(maxval - arr[i]) * arr2[i]` for all `i` from 0 to `n-1`.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer `n` representing the number of companies. For each company, it reads a list of salaries and calculates the maximum salary in each list. It then determines the overall maximum salary across all companies and computes a total `ans`, which is the sum of the differences between this maximum salary and the maximum salary for each company, multiplied by the number of salaries in that company. Finally, it prints the computed total `ans`. The function does not handle cases where there are no companies or salaries, as it assumes `n` will always be at least 1.

