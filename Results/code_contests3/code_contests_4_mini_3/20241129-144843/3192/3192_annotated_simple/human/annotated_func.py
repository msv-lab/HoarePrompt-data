#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 ⋅ 10^5), and each company contains a positive integer m_i (1 ≤ m_i ≤ 2 ⋅ 10^5) followed by m_i positive integers representing the salaries of employees, where each salary does not exceed 10^9. The total number of employees across all companies does not exceed 2 ⋅ 10^5.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `arr` contains the maximum values from each of the `arr1` lists, `maxval` is the maximum value found in `arr`, `arr2` contains the sizes of each `arr1` list, `i` is `n - 1`, `arr1` is the last list of integers processed, `temp` is the maximum value from the last `arr1[1]` to `arr1[arr1[0] - 1]`, `j` is `arr1[0] - 1`.
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `i` is `n`, `ans` is the accumulated sum of (maxval - arr[i]) * arr2[i] for all i from 0 to n-1, `arr` contains maximum values from each of the arr1 lists, `maxval` is the maximum value found in arr, `arr2` contains the sizes of each arr1 list.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer `n`, which represents the number of companies, and for each company, it reads a list of salaries. It calculates the maximum salary across all companies and then computes the total difference between this maximum and the highest salary in each company, multiplied by the number of employees in that company. Finally, it returns the accumulated sum of these differences, which reflects the total amount needed to equalize all salaries to the maximum salary found.

