#State of the program right berfore the function call: n is a positive integer representing the number of companies in the conglomerate. Each company description includes an integer m_i representing the number of employees in the company, followed by m_i integers representing the salaries of the employees in that company. All integers are within the specified constraints.**
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `arr` contains the maximum value in each `arr1` entered by the user, `maxval` is the maximum value among all maximum values in `arr`, `arr2` contains the first element of each `arr1` entered by the user, `i` is equal to `n`, `temp` is the maximum value in the last `arr1`, `j` is equal to the length of the last `arr1`
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `arr` contains the maximum value in each `arr1`, `maxval` is the maximum value among all maximum values in `arr`, `arr2` contains the first element of each `arr1`, `i` is equal to `n`, `temp` is the maximum value in the last `arr1`, `j` is equal to the length of the last `arr1`, `ans` is the sum of all `(maxval - arr[i]) * arr2[i]` for each iteration of the loop.
    print(ans)
#Overall this is what the function does:The function `func` reads input about a conglomerate's structure, including the number of companies, the number of employees in each company, and their salaries. It calculates a value 'ans' based on the maximum salaries in each company and the number of employees in each company. The function then prints the final value of 'ans'. The function does not return any value but is used for analyzing conglomerate data.

