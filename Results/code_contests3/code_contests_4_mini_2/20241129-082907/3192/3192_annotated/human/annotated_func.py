#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 200,000; each company has a number of employees m_i (1 ≤ m_i ≤ 200,000), with each employee's salary being a positive integer not exceeding 10^9; the total number of employees across all companies does not exceed 200,000.
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
        
    #State of the program after the  for loop has been executed: `arr` contains the maximum values from each of the `n` input lists, `arr2` contains the sizes of each of the `n` input lists, `maxval` is the maximum value among all elements in `arr`, and `n` is a positive integer such that 1 ≤ `n` ≤ 200,000.
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `arr` contains the maximum values from each of the `n` input lists; `arr2` contains the sizes of each of the `n` input lists; `maxval` is the maximum value among all elements in `arr; `n` is a positive integer such that 1 ≤ `n` ≤ 200,000; `ans` is the sum of the products of (maxval - arr[i]) and arr2[i] for all i from 0 to n-1.
    print(ans)
#Overall this is what the function does:The function accepts input for `n` companies, each with a varying number of employees and their respective salaries. It computes the maximum salary from each company, determines the overall maximum salary across all companies, and calculates the total salary adjustment needed to equalize all companies to the maximum salary by summing the differences between the maximum and each company's maximum salary, multiplied by the number of employees in that company. Finally, it outputs this total adjustment amount. No parameters are directly accepted by the function, as it relies on user input.

