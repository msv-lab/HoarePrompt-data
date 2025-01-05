#State of the program right berfore the function call: n is a positive integer representing the number of companies. Each company is described by the number of employees (m_i) and their salaries, where m_i is a positive integer and the salaries are positive integers not exceeding 10^9. The total number of employees in all companies does not exceed 2 * 10^5.**
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
        
    #State of the program after the  for loop has been executed: `arr` contains the maximum value from each `arr1` appended to it, `arr2` contains the value at index 0 of each `arr1`, `maxval` is the maximum value among all elements in `arr`
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `arr` contains the maximum value from each `arr1` appended to it, `arr2` contains the value at index 0 of each `arr1`, `maxval` is the maximum value among all elements in `arr1`, `ans` is the summation of each `(maxval - arr[i]) * arr2[i]` for every element in `arr`
    print(ans)
#Overall this is what the function does:The function reads the number of companies `n`, each described by the number of employees and their salaries. It then calculates the maximum salary among employees in each company, stores it in `arr`, and the number of employees in each company in `arr2`. It finds the maximum salary across all companies in `maxval`. Finally, it calculates and prints the average salary across all companies by summing `(maxval - arr[i]) * arr2[i]` for each company.

