#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200,000), and each company has a positive number of employees (m_i) such that the total number of employees across all companies does not exceed 200,000. Each salary of the employees is a positive integer and does not exceed 10^9.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `arr` is a list containing the maximum values found in each of the `n` input lists, `maxval` is the maximum value among all elements in `arr`, `arr2` is a list containing the sizes of each of the `n` input lists.
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `ans` is the sum of (maxval - arr[i]) * arr2[i] for all i from 0 to n-1, `n` is a positive integer, `arr` is a list of maximum values, `maxval` is the maximum value among all elements in `arr`, `arr2` is a list containing the sizes of each of the `n` input lists.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer `n`, which represents the number of companies, and processes salary data by reading `n` lists of employee salaries. It calculates the maximum salary for each company, then determines the total adjustment needed to equalize all salaries to the maximum salary across all companies, weighted by the number of employees in each company. Finally, it prints the total adjustment needed. The function does not handle cases where `n` is 0, nor does it validate the input sizes or salaries against the stated constraints.

