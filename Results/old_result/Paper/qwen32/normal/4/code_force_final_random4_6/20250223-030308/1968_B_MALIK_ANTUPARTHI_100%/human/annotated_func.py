#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^5. a is a binary string of length n, and b is a binary string of length m. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5, and the sum of all m values across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: `i` is equal to `a`, `b`, `c`, `d`, and `e` are the values from the last iteration, `j` is the final index from the nested loop in the last iteration, and `k` is the final value determined by the nested loop's conditions in the last iteration.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it receives two integers `n` and `m`, and two binary strings `a` and `b` of lengths `n` and `m` respectively. It then calculates and prints a value `k` for each test case based on the presence of characters from string `a` in string `b` under specific conditions.

