#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200,000; each company has a positive integer m_i representing the number of employees (1 ≤ m_i ≤ 200,000) followed by m_i positive integers representing the salaries of the employees (each salary does not exceed 10^9); the total number of employees across all companies does not exceed 200,000.
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
        
    #State of the program after the  for loop has been executed: `n` is an input integer such that 1 ≤ `n` ≤ 200,000; `arr` contains `n` elements representing the maximum values from each input list; `arr2` contains `n` elements representing the sizes of each corresponding input list; `maxval` is the maximum value among all elements in `arr`.
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `ans` is the sum of (maxval - arr[i]) * arr2[i] for all valid `i` from 0 to n-1; `arr` is an array of n elements, `arr2` is an array of n elements, `maxval` is the maximum value in `arr`.
    print(ans)
#Overall this is what the function does:The function accepts an integer input `n`, which represents the number of companies. For each company, it processes a list of employee salaries and calculates the maximum salary for each company. It then computes a total value, which is the sum of the product of the difference between the overall maximum salary and each company's maximum salary multiplied by the number of employees in that company. Finally, it prints the computed total value. The function does not return any value but outputs the result directly.

