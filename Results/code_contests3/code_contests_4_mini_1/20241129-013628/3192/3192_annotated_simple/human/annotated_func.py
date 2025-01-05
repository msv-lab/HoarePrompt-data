#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200,000), and each company description consists of a positive integer m_i (1 ≤ m_i ≤ 200,000) followed by m_i positive integers representing salaries, where each salary is a positive integer not exceeding 1,000,000,000. The total number of employees across all companies does not exceed 200,000.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `i` is `n - 1`, `arr` contains the maximum values from each `arr1` processed, `maxval` is the maximum value among all elements in `arr`, `arr2` is a list of the sizes of each `arr1`, `arr1` is a list of integers from the last iteration, `temp` is the maximum value among the last `arr1` elements from index 1 to `arr1[0] - 1 or 0 if `arr1[0]` is 1.
    ans = 0
    for i in range(n):
        ans += (maxval - arr[i]) * arr2[i]
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `i` is `n - 1`, `ans` is the sum of `(maxval - arr[i]) * arr2[i]` for all `i` from `0` to `n-1`.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer input representing the number of companies, followed by salary data for each company, and calculates the total difference in salaries compared to the maximum salary across all companies, then prints the result. It does not handle cases of invalid input or zero companies.

