#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200,000) representing the number of companies, and each company has a positive integer m_i (1 ≤ m_i ≤ 200,000) followed by m_i positive integers representing the salaries of the employees in that company (salaries do not exceed 10^9). The total number of employees across all companies does not exceed 200,000.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 200,000), `i` is `n - 1`, `arr` contains the maximum values from each of the `n` lists read, `arr2` contains the counts of each list, `maxval` is the maximum value in `arr`.
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `ans` is the total sum of `(maxval - arr[i]) * arr2[i]` for all `i` in the range of `n`, `n` is a positive integer (1 ≤ n ≤ 200,000), `i` is n - 1 after the loop has executed, `arr` and `arr2` are unchanged.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer `n` representing the number of companies, followed by `n` lists of employee salaries. It computes the maximum salary from each list and calculates the total sum needed to equalize all employee salaries to the maximum salary across all companies. The function then prints this total sum.

