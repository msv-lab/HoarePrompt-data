#State of the program right berfore the function call: n is a positive integer representing the number of companies in the conglomerate. Each company description consists of an integer m_i representing the number of employees in the company, followed by m_i integers representing the salaries of the employees. Salaries are positive and do not exceed 10^9. The total number of employees in all companies does not exceed 2*10^5.**
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `arr` is a list containing the maximum values of each input list `arr1`, `temp` is the maximum value among all elements in all input lists, `maxval` is the maximum value among all maximum values in `arr`, `arr2` is a list containing the lengths of each input list `arr1`, `i` is equal to `n-1`, `j` is the length of the last `arr1`
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `arr` is a list containing the maximum values of each input list `arr1`, `temp` is the maximum value among all elements in all input lists, `maxval` is the maximum value among all maximum values in `arr`, `arr2` is a list containing the lengths of each input list `arr1`, `i` is equal to `n`, `j` is the length of the last `arr1`, `ans` is equal to the sum of all `(maxval - arr[i]) * arr2[i]` for each `i` in the range of `len(arr)`.
    print(ans)
#Overall this is what the function does:The function `func` takes no parameters and reads information about a conglomerate consisting of multiple companies. It calculates the average salary of all employees in the conglomerate based on the maximum salary in each company and the number of employees in each company. The function then prints the average salary. However, the code does not explicitly calculate the average salary as indicated in the annotations. Instead, it calculates a different metric involving the maximum salary and the number of employees in each company. Therefore, the functionality of the function is to compute a metric related to salaries in the conglomerate and print the result.

