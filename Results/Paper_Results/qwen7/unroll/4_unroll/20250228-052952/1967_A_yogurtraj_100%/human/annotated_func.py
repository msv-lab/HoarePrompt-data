#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^{12}, and for each test case, a list of n integers a_1, a_2, ..., a_n is provided where 1 ≤ a_i ≤ 10^{12}.
def func():
    for ii in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        r = a[0]
        
        rem = 0
        
        y = 0
        
        for i in range(0, n - 1):
            if (i + 1) * (a[i + 1] - a[i]) > k:
                r = a[i] + k // (i + 1)
                rem = k % (i + 1)
                y = n - 1 - i
                k = 0
                break
            else:
                k -= (i + 1) * (a[i + 1] - a[i])
                r = a[i + 1]
        
        if k != 0:
            r = a[n - 1] + k // n
            print((r - 1) * n + 1 + k % n)
        else:
            print((r - 1) * n + 1 + rem + y)
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 100, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^{12}, and for each test case, a list of n integers a_1, a_2, ..., a_n is provided where 1 ≤ a_i ≤ 10^{12}. After executing the loop, r is an integer representing the final value calculated based on the given conditions, rem is an integer representing the remaining value of k after the loop, and y is an integer representing the number of elements from the sorted list that satisfy the condition (i + 1) * (a[i + 1] - a[i]) > k.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer \( n \), an integer \( k \), and a list of \( n \) integers \( a_1, a_2, \ldots, a_n \). For each test case, it calculates a final value \( r \) based on the given constraints and prints the result. If \( k \) is completely consumed during the process, it calculates \( r \) using the last element of the sorted list and the remaining value of \( k \). Otherwise, it finds the maximum possible value of \( r \) by adjusting the elements of the list according to the value of \( k \) and the differences between consecutive elements. The function outputs the final calculated value for each test case.

