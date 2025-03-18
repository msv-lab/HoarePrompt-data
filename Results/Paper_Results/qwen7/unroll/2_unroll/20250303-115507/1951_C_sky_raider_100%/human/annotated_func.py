#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n, m, and k are integers such that 1 ≤ n ≤ 3⋅10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(n⋅m, 10^9); a is a list of n integers such that 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n.
def func():
    for i in range(int(input())):
        n, m, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        l.sort()
        
        t = 0
        
        s = 0
        
        c = 0
        
        for i in range(n):
            s = min(m, k)
            c += s * (l[i] + t)
            t += s
            k -= s
        
        print(int(c))
        
    #State: Output State: t is an integer initialized to 0; n, m, and k are integers read from input; l is a list of n integers read from input and sorted; s and c are integers initialized to 0; after executing the loop, c is the sum of the products of elements of l with their corresponding accumulated t value, where s is the minimum of m and k, and t is incremented by s after each iteration, with k being decremented accordingly.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers t, n, m, k, and a list of n integers a. For each test case, it reads these values, sorts the list a, then iterates through its elements. During each iteration, it calculates a cumulative sum based on the minimum of m and k, updates a running total c, and adjusts m and k accordingly. Finally, it prints the computed total c for each test case.

