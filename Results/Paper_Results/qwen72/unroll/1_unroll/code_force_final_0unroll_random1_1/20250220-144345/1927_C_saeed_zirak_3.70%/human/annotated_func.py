#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n, m, and k are integers such that 1 ≤ n, m ≤ 2·10^5, 2 ≤ k ≤ 2·min(n, m), and k is even; a is a list of n integers such that 1 ≤ a_i ≤ 10^6; b is a list of m integers such that 1 ≤ b_j ≤ 10^6.
def func():
    for t in range(int(input())):
        n, m, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        b = list(map(int, input().split()))
        
        aOnes = 0
        
        bOnes = 0
        
        newk = k // 2
        
        i = 1
        
        while i <= k:
            if i in a and i in b:
                if aOnes < bOnes:
                    aOnes += 1
                else:
                    bOnes += 1
            elif i in a and aOnes <= newk:
                aOnes += 1
            elif i in b and bOnes <= newk:
                bOnes += 1
            else:
                break
            i += 1
        
        if aOnes == newk and bOnes == newk:
            print('yes')
        else:
            print('no')
        
    #State: For each test case, the loop will output 'yes' if it is possible to select exactly k/2 elements from list a and k/2 elements from list b such that all selected elements are unique and within the range 1 to k, otherwise it will output 'no'. The values of t, n, m, k, a, and b remain unchanged after the loop execution.
#Overall this is what the function does:The function processes `t` test cases, where each test case involves integers `n` and `m` (the lengths of lists `a` and `b`), an even integer `k` (with constraints 2 ≤ k ≤ 2·min(n, m)), and lists `a` and `b` of integers (with elements between 1 and 10^6). For each test case, the function checks if it is possible to select exactly `k/2` unique elements from list `a` and `k/2` unique elements from list `b` such that all selected elements are within the range 1 to `k`. If this condition is met, the function prints 'yes'; otherwise, it prints 'no'. The values of `t`, `n`, `m`, `k`, `a`, and `b` remain unchanged after the function execution.

