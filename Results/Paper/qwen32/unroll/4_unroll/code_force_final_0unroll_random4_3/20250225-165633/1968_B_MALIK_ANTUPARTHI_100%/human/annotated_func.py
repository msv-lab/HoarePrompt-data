#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2 · 10^5. a is a binary string of length n, and b is a binary string of length m. The sum of all n values across test cases does not exceed 2 · 10^5, and the sum of all m values across test cases does not exceed 2 · 10^5.
def func():
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        d = input()
        
        e = input()
        
        k = 0
        
        for j in range(b):
            if d[j] in e[k:]:
                k = e[k:].index(d[j]) + 1 + k
                if k == c or j == b - 1:
                    k = j + 1
                    break
            else:
                k = j
                break
        
        print(k)
        
    #State: the final value of `k` after the last iteration of the outer loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads two integers `n` and `m`, and two binary strings `a` and `b` of lengths `n` and `m` respectively. It then calculates and prints an integer `k` for each test case, which is determined based on the matching characters between the strings `a` and `b`.

