#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^5, and two binary strings a and b are provided where the length of a is n and the length of b is m. It is guaranteed that the sum of all n values does not exceed 2 ⋅ 10^5, and the sum of all m values does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4, a is an input integer, each iteration of the outer loop processes a pair of strings (d and e) and an integer (c) from user input, calculates the value of k based on the conditions given, and prints the final value of k after completing all iterations of the inner loop. The final state of t and a remains unchanged, while the values of d, e, c, and k are determined by the input during each iteration of the outer loop.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two binary strings `d` and `e`, and an integer `c`. For each test case, it finds the minimum index `k` such that the first `b` characters of string `d` can be found in string `e` starting from index `k`. If no such index exists, it prints `-1`. After processing all test cases, it outputs the value of `k` for each case. The function does not modify the input parameters `t`, `a`, `n`, `m`, `b`, `c`, `d`, and `e` except for calculating and printing `k`.

