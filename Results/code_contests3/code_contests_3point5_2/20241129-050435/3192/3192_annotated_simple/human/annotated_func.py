#State of the program right berfore the function call: n is a positive integer representing the number of companies. Each company description consists of an integer m_i representing the number of employees in the company (1 ≤ m_i ≤ 2 ⋅ 10^5) followed by m_i integers representing the salaries of the employees (positive and not exceeding 10^9). The total number of employees in all companies does not exceed 2 ⋅ 10^5.**
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `arr` contains the maximum values from each `arr1`, `maxval` is the maximum value between all elements in `arr`, `arr2` contains the number of elements in each `arr1`, `arr1` is a list of integers created by mapping the input to integers, `temp` is the maximum value in the last `arr1`
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `arr` contains the maximum values from each `arr1`, `maxval` is the maximum value between all elements in `arr`, `arr2` contains the number of elements in each `arr1`, `arr1` is a list of integers created by mapping the input to integers, `temp` is the maximum value in the last `arr1`, and `ans` is the sum of each iteration of the formula `(maxval - arr[i]) * arr2[i]` for all values of `i` from 0 to `n-1`.
    print(ans)
#Overall this is what the function does:The function reads the number of companies and their employee data. It then calculates the total sum of differences between the maximum salary in each company and the salaries of all employees within each company. Finally, it prints the total sum. The function ensures that the total number of employees across all companies does not exceed 2 ⋅ 10^5.

