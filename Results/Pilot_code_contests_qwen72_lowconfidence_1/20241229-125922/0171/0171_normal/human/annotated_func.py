#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), representing the number of test cases. Each test case consists of an integer n (1 ≤ n ≤ 2⋅10^5) and an array a of n integers (a_0, a_1, …, a_{n-1}) where each a_i satisfies -10^9 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2⋅10^5.
def func():
    input = sys.stdin.readline
    for _ in xrange(int(input())):
        n = int(input())
        
        seq = [int(x) for x in input().split()]
        
        s = sorted([(i + seq[i % n]) for i in xrange(2 * n)])
        
        ans = 'YES'
        
        for i in xrange(1, len(s)):
            if s[i] == s[i - 1]:
                ans = 'NO'
                break
        
        print(ans)
        
    #State of the program after the  for loop has been executed: `t` is a positive integer (1 ≤ t ≤ 10^4), `input` is assigned to `sys.stdin.readline`, for each test case, `n` is an integer read from the input and must be at least 1, `seq` is a list of integers from the input split by spaces, `s` is a sorted list of integers computed as `sorted([(i + seq[i % n]) for i in range(2 * n)])` and must have at least 2 * n elements, `ans` is 'YES' if no duplicates are found in `s`, otherwise `ans` is 'NO', and the value of `ans` has been printed for each test case.
#Overall this is what the function does:The function reads multiple test cases from standard input. Each test case consists of an integer `n` and a list of `n` integers. For each test case, the function computes a new list `s` by adding each element of the list to its index (considering wrap-around using modulo `n`). It then checks if there are any duplicate values in the sorted list `s`. If duplicates are found, the function prints "NO" for that test case; otherwise, it prints "YES". The function processes all test cases and prints the result for each one. The state after the function concludes is that all test cases have been processed and the results have been printed to standard output. The function does not return any value. Potential edge cases include handling the maximum limits of `t` and `n`, and ensuring that the input values are within the specified ranges.

