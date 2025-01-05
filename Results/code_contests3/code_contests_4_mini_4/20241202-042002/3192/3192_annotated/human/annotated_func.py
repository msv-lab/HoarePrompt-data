#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200,000; each company has a positive integer m_i representing the number of employees (1 ≤ m_i ≤ 200,000), followed by m_i positive integers representing the salaries of the employees, all salaries do not exceed 10^9; the total number of employees across all companies does not exceed 200,000.
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
        
    #State of the program after the  for loop has been executed: `arr` is a list containing the maximum values from each `arr1` read during the loop iterations, `arr2` is a list containing the first element of each `arr1`, `maxval` is the maximum value among all elements in `arr` after the loop completes, and `n` is an integer such that 1 ≤ n ≤ 200,000.
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `ans` is the accumulated sum from all iterations, `i` is `n`, `arr` is unchanged, `arr2` is unchanged, `maxval` is the maximum value among all elements in `arr`.
    print(ans)
#Overall this is what the function does:The function reads the number of companies and their employees' salaries, calculates the maximum salary for each company, finds the overall maximum salary, and computes the total sum of differences between this overall maximum and each company's maximum salary multiplied by the number of employees in that company, then prints the result.

