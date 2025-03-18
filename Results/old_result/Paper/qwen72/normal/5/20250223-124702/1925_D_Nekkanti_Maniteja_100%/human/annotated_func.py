#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4, n is an integer such that 2 ≤ n ≤ 10^5, m is an integer such that 0 ≤ m ≤ min(10^5, n(n-1)/2), k is an integer such that 1 ≤ k ≤ 2 · 10^5, and for each of the m lines, a_i, b_i, and f_i are integers where a_i ≠ b_i, 1 ≤ a_i, b_i ≤ n, and 1 ≤ f_i ≤ 10^9. The sum of n and m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2 · 10^5.
def func():
    for i in range(int(input())):
        n, m, k = map(int, input().split())
        
        M = 10 ** 9 + 7
        
        c = pow(n * (n - 1) // 2, -1, M)
        
        s = 0
        
        a = 0
        
        for i in range(m):
            u, v, f = map(int, input().split())
            a += f
        
        for i in range(k):
            s = s + c * i * c * m + c * a
        
        print(s % M)
        
    #State: The value of `t` is unchanged. For each iteration, the values of `n`, `m`, and `k` are updated based on the input. The variable `s` is the final result of the loop, which is the sum of all calculated values modulo \(10^9 + 7\). The variable `a` is the sum of all `f` values from the input. The variable `c` is the modular inverse of \( \frac{n(n-1)}{2} \) modulo \(10^9 + 7\).
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads the number of nodes `n`, the number of edges `m`, and a threshold `k`. It then reads `m` lines of input, each containing three integers `u`, `v`, and `f`, and calculates a final result `s` based on these inputs. The result `s` is the sum of a specific formula applied `k` times, modulo \(10^9 + 7\). The function prints the result `s` for each test case. After processing all test cases, the function concludes, and the value of `t` remains unchanged. The variables `n`, `m`, and `k` are updated for each test case, and `a` is the sum of all `f` values from the input for each test case, while `c` is the modular inverse of \( \frac{n(n-1)}{2} \) modulo \(10^9 + 7\).

