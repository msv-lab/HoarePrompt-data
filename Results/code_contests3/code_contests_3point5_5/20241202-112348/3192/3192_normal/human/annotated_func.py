#State of the program right berfore the function call: n is a positive integer representing the number of companies in the conglomerate. Each company description contains an integer m_i representing the number of employees in the company, followed by m_i integers representing the salaries of the employees. All salaries are positive and do not exceed 10^9. The total number of employees in all companies does not exceed 2 * 10^5.**
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
        
    #State of the program after the  for loop has been executed: `temp` is the maximum value in the last input list `arr1`, `n` is equal to the number of iterations of the loop, `arr` contains the maximum value from each input list, `maxval` is the maximum value from all the input lists, `arr2` contains the first element of each input list.
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `temp` is the maximum value in the last input list `arr1`, `n` is equal to the number of iterations specified, `arr` contains the maximum value from each input list, `maxval` is the maximum value from all the input lists, `arr2` contains the first element of each input list, `ans` is the sum of all products computed in the loop
    print(ans)
#Overall this is what the function does:The function `func` reads input data about multiple companies in a conglomerate. Each company's information includes the number of employees and their salaries. It calculates the difference between the maximum salary in all companies and each company's maximum salary, then multiplies this difference by the number of employees in that company. Finally, it prints the total sum of these calculated values. The function does not accept any parameters and does not return any value. The provided annotations describe the state of variables at different points in the code execution, ensuring accurate processing of the conglomerate's data.

