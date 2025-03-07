#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, n and k are integers for each test case where 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100, and c is a list of n integers where 1 ≤ c_i ≤ 100.
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
        
    #State: t is an input integer such that 1 ≤ t ≤ 500, n and k are integers for each test case where 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100, and c is a list of n integers where 1 ≤ c_i ≤ 100. The loop has executed t times, and for each iteration, the output is either k - 1 or n, depending on the condition max(p) >= k.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two integers `n` and `k`, and a list `l` of `n` integers. It then calculates the frequency of each unique integer in `l` and checks if the maximum frequency is greater than or equal to `k`. If the condition is met, it prints `k - 1`; otherwise, it prints `n`. After processing all `t` test cases, the function concludes. The final state of the program is that `t` test cases have been processed, and for each test case, the appropriate value (`k - 1` or `n`) has been printed to the output.

