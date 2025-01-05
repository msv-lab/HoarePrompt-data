#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200,000), and for each company, m_i is a positive integer (1 ≤ m_i ≤ 200,000) representing the number of employees in that company. Each employee's salary is a positive integer not exceeding 10^9, and the total number of employees across all companies does not exceed 200,000.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `arr` contains the maximum values from each of the `arr1` lists processed, `maxval` is the maximum value from all entries in `arr`, `arr2` contains the first elements of each `arr1` list processed, `i` is `n - 1`, `arr1` is a list of integers with at least one element from the last iteration, `temp` is the maximum value from the last `arr1` processed (from index 1 to `arr1[0] - 1` if `arr1[0] > 1`, otherwise `temp` is 0), `j` is equal to the last `arr1[0]`.
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `ans` is the sum of `(maxval - arr[i]) * arr2[i]` for all `i` from 0 to `n - 1`, `n` is a positive integer, `i` is equal to `n`, `arr` contains the maximum values from each of the `arr1` lists processed, `maxval` is the maximum value from all entries in `arr`, `arr2` contains the first elements of each `arr1` list processed.
    print(ans)
#Overall this is what the function does:The function reads a positive integer `n`, representing the number of companies, and then for each company, it reads a list of integers where the first integer indicates the number of employees, followed by the salaries of those employees. It calculates the maximum salary among all employees across the companies and then computes a total `ans`, which is the sum of the differences between the maximum salary and the maximum salary in each company multiplied by the number of employees in that company. Finally, it prints this total. The function does not return any value but prints the result instead.

