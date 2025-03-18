#State of the program right berfore the function call: Each test case consists of three integers n, m, and k, where 1 ≤ n ≤ 3 · 10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9). The test case also includes a list of n integers a_1, a_2, ..., a_n, where 1 ≤ a_i ≤ 10^9. The total number of days n across all test cases does not exceed 3 · 10^5.
def func():
    for i in range(int(input())):
        n, m, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        l.sort()
        
        s = 0
        
        c = k * k / 2
        
        for i in range(n):
            s = min(m, k)
            k -= s
            c += l[i] * s - s * s / 2
        
        print(int(c))
        
    #State: the output state you calculate based on the provided input.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers `n`, `m`, and `k`, and a list of `n` integers. For each test case, it calculates and prints a specific value based on these inputs. The value is determined by sorting the list, iterating through it, and applying a series of arithmetic operations involving `m`, `k`, and the elements of the list.

