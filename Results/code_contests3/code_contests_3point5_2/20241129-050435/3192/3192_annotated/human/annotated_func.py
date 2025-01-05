#State of the program right berfore the function call: n is a positive integer representing the number of companies. Each company description includes an integer m_i representing the number of employees in the company, followed by m_i integers representing the salaries of the employees. All integers are within the specified ranges.**
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
        
    #State of the program after the  for loop has been executed: `arr` is a list containing integers inputted from the user along with the maximum value among all elements in `arr1` added at the end, `maxval` is the maximum value among all elements in `arr`, `i` is equal to n-1, for the loop to execute the last time `n` is greater than 0, `temp` is the maximum value among all elements in `arr1`, `j` is equal to len(`arr1`), `arr2` contains the first element of `arr1`.
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `arr` is a list containing integers inputted from the user along with the maximum value among all elements in `arr1` added at the end, `maxval` is the maximum value among all elements in `arr`, `i` is equal to -1, `temp` is the maximum value among all elements in `arr1`, `j` is equal to len(`arr1`), `arr2` contains the last element of `arr1`, `ans` is the sum of all the calculations `(maxval - arr[i]) * arr2[i]` where i ranges from 0 to n-1
    print(ans)
#Overall this is what the function does:The function `func` reads input about multiple companies, each represented by the number of employees and their salaries. It then calculates and prints a value based on the data provided. The function does not accept any parameters and focuses on processing and analyzing the company data to derive a specific result.

