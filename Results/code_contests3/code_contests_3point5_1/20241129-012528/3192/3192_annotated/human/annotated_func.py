#State of the program right berfore the function call: n is a positive integer representing the number of companies in the conglomerate. Each company description contains an integer m_i representing the number of employees in the company, followed by m_i positive integers representing the salaries of the employees. All salaries are positive and do not exceed 10^9. The total number of employees in all companies does not exceed 2 * 10^5.**
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `arr` contains the maximum value among all elements in all `arr1` lists, `maxval` is the maximum value among all elements in all `arr1` lists, `arr2` contains the first element of each `arr1` list, `i` is equal to `n - 1`, `arr1` is a list of integers created by mapping `int` function to input split by spaces with at least one element, `temp` is the maximum value among all elements in each `arr1` list, `j` is equal to the first element in each `arr1` list
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `arr` contains the maximum value among all elements in all `arr1` lists, `maxval` is the maximum value among all elements in all `arr1` lists, `arr2` contains the first element of each `arr1` list, `i` is equal to `n`, `arr1` is a list of integers created by mapping `int` function to input split by spaces with at least one element, `temp` is the maximum value among all elements in each `arr1` list, `j` is equal to the first element in each `arr1` list, `ans` is equal to the sum of each product of (maxval - arr[i]) and arr2[i] for all elements in `arr`
    print(ans)
#Overall this is what the function does:The function `func` reads input about the number of companies in a conglomerate, the number of employees in each company, and their salaries. It then calculates and prints the sum of the products of the differences between the maximum salary in each company and the salaries of the employees with the total number of employees in each company. The function does not accept any parameters and does not return any value.

