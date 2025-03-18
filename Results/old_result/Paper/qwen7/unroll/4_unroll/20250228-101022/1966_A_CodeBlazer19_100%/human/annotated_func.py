#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n and k are integers such that 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100. Additionally, a list of n integers c_1, c_2, ..., c_n is provided, where 1 ≤ c_i ≤ 100 for each i.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        p = [l.count(j) for j in set(l)]
        
        if max(p) >= k:
            print(k - 1)
        else:
            print(n)
        
    #State: Output State: The output state will consist of a series of integers printed based on the conditions inside the loop for each iteration from `i` in `range(t)`. For each iteration, if the maximum count of any number in the list `l` is greater than or equal to `k`, then `k - 1` will be printed; otherwise, `n` will be printed. The sequence of these integers will depend on the inputs provided within each iteration of the loop.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads two integers \( n \) and \( k \), followed by a list of \( n \) integers. It then determines whether the maximum frequency of any number in the list is at least \( k \). If so, it prints \( k - 1 \); otherwise, it prints \( n \). This process is repeated for each of the \( t \) test cases, where \( t \) is the first input integer.

