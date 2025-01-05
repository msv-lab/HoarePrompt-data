#State of the program right berfore the function call: n is a positive integer representing the number of companies. Each company description consists of an integer m_i representing the number of employees in the company, followed by m_i integers representing the salaries of the employees in that company. All salaries are positive integers and do not exceed 10^9. The total number of employees in all companies does not exceed 2 * 10^5.**
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer representing the number of companies, `arr` is a list containing the maximum salaries of employees in each company, `temp` holds the maximum value from each company, `maxval` is the overall maximum salary among all employees in all companies
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `arr` is a list containing maximum salaries of employees in each company, `temp` holds the maximum value from each company, `maxval` is the overall maximum salary among all employees in all companies, `ans` is updated by adding the result of `(maxval - arr[i]) * arr2[i]` for each company in the list.
    print(ans)
#Overall this is what the function does:The function `func` reads the number of companies as input and processes the information of each company, calculating the maximum salary among employees in each company and the overall maximum salary across all companies. It then computes a final result based on these values and prints the result. The function does not accept any parameters and is designed to handle the constraints related to the number of companies, employees, and salary values as mentioned in the annotations.

