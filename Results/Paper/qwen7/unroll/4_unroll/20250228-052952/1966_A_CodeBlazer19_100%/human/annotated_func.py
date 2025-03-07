#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500; for each test case, n and k are integers such that 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100; the list of integers c represents the numbers written on the cards, where each c_i is an integer such that 1 ≤ c_i ≤ 100.
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
        
    #State: Output State: The output state will consist of a series of integers printed based on the conditions within the loop. For each iteration defined by `i` in the range of `t`, the program checks if the maximum frequency of any number in the list `l` is greater than or equal to `k`. If true, it prints `k - 1`; otherwise, it prints `n`. The output will be a list of these integers corresponding to each iteration.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads two integers \( n \) and \( k \), followed by a list of integers \( c \). It then determines the maximum frequency of any number in the list \( c \). If this maximum frequency is greater than or equal to \( k \), it outputs \( k - 1 \); otherwise, it outputs \( n \). The function returns nothing but prints the results for each test case.

