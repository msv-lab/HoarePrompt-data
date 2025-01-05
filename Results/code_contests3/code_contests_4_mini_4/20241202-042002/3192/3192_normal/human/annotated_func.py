#State of the program right berfore the function call: n is an integer representing the number of companies (1 ≤ n ≤ 200,000), and each company is described by a positive integer m_i followed by m_i positive integers representing the salaries of the employees (1 ≤ m_i ≤ 200,000), where all salaries do not exceed 10^9. The total number of employees across all companies does not exceed 200,000.
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
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `arr` contains `n` maximum values from each input list, `arr2` contains `n` sizes of the input lists, `maxval` is the maximum value found in `arr.`
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `ans` is the total of `(maxval - arr[i]) * arr2[i]` for all `i` from `0` to `n-1`, `n` is a non-negative integer, `arr` contains `n` maximum values, `arr2` contains `n` sizes, `maxval` is the maximum value found in `arr`.
    print(ans)
#Overall this is what the function does:The function accepts an integer `n` representing the number of companies, followed by `n` lists of employee salaries. It computes the maximum salary for each company and the overall maximum salary across all companies. Then, it calculates the total difference between the maximum salary and the maximum salary of each company, scaled by the number of employees in that company, and prints this total. The function does not return any value but outputs the computed total directly.

