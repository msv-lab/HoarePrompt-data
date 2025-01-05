#State of the program right berfore the function call: n is a positive integer representing the number of companies in the conglomerate. Each company description includes an integer m_i representing the number of employees in the company, followed by m_i integers representing the salaries of the employees. Salaries are positive integers and do not exceed 10^9. The total number of employees in all companies does not exceed 2 * 10^5.**
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
        
    #State of the program after the  for loop has been executed: `arr` is a list containing maximum values entered by the user in each iteration, `temp` is the maximum value in the current `arr1`, `arr1` is a list containing integers entered by the user with at least 1 element, `arr2` is a list containing the total number of elements in `arr1` for each iteration, `maxval` is the maximum value in `arr`, `i` is equal to the total number of iterations, `n` is greater than or equal to the total number of iterations
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `arr` is a list containing maximum values entered by the user, `temp` is the maximum value in the current `arr1`, `arr1` is a list containing integers entered by the user with at least 1 element, `arr2` is a list containing the total number of elements in `arr1` for each iteration, `maxval` is the maximum value in `arr`, `i` is equal to the total number of iterations, `n` is greater than or equal to the total number of iterations, `ans` is the sum of all the calculated values in the loop
    print(ans)
#Overall this is what the function does:The function reads the number of companies in a conglomerate, then iterates through each company to find the maximum salary among employees. It calculates a value based on the maximum salary difference across all companies and the number of employees in each company, and finally prints the total value calculated. The function handles scenarios where the input data may not adhere to the provided constraints.

