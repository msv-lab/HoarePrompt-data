#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n and k are integers such that 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100. The list of integers c represents the numbers written on the cards, where each c_i is an integer such that 1 ≤ c_i ≤ 100.
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
        
    #State: Output State: The output state will consist of a series of integers printed based on the conditions inside the loop. For each iteration of the loop (from 0 to t-1), if the maximum frequency of any number in the list `l` is greater than or equal to `k`, then `k - 1` will be printed; otherwise, `n` will be printed. The exact sequence of these integers depends on the inputs provided during each iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `t`. For each test case, it reads two integers `n` and `k`, followed by a list of integers `c`. It then determines the frequency of each unique number in the list `c` and checks if the highest frequency is greater than or equal to `k`. If true, it prints `k - 1`; otherwise, it prints `n`. The function outputs a series of integers based on these conditions for each test case.

