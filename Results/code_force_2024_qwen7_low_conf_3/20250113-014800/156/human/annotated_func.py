#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers satisfying 1 ≤ n ≤ 3⋅10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9). Additionally, a list of n integers a_1, a_2, ..., a_n is given where 1 ≤ a_i ≤ 10^9 represents the price per ticket for each of the upcoming n days. The sum of n across all test cases does not exceed 3⋅10^5.
def func():
    n = int(input())
    for i in range(n):
        n, m, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        if k <= m:
            print(min(a) * k)
        else:
            if k % m == 0:
                s = set(sorted(a)[:k // m])
                b = []
                leng = 0
                for i in range(n):
                    if a[i] in s and leng < k // m:
                        b.append(a[i])
                        leng += 1
                c = 0
                res = 0
                for i in range(len(b)):
                    res += (b[i] + c) * m
                    c += m
            else:
                s = set(sorted(a)[:k // m + 1])
                b = []
                leng = 0
                for i in range(n):
                    if a[i] in s and leng < k // m + 1:
                        b.append(a[i])
                        leng += 1
                c = 0
                res = 0
                mx = max(b)
                mx_ind_lt = max(i for i in range(len(b)) if b[i] == mx)
                for i in range(len(b)):
                    if b[i] == mx and i == mx_ind_lt:
                        res += (b[i] + c) * (k % m)
                        c += k % m
                    else:
                        res += (b[i] + c) * m
                        c += m
            print(res)
        
    #State of the program after the  for loop has been executed: `t` is a positive integer such that \(1 \leq t \leq 10^4\); `m` is an integer satisfying \(1 \leq m \leq 10^9\); `k` is an integer satisfying \(1 \leq k \leq \min(nm, 10^9)\); `n` is the last input integer; `a` is a list of integers obtained from the inputs; `b` is a non-empty iterable where `n` is the number of elements in `b`; `mx` is the maximum value in `b`; `mx_ind_lt` is the index of the maximum value in `b` that equals `mx`; `leng` is `k // m + 1`; `c` is `n * m` if `k % m == 0` otherwise `k`; `res` is the sum of `(b[i] + (j-1)*m) * m` for all `i` in `range(len(b))` and `j` ranging from 1 to `n` if `k % m == 0` otherwise the sum of `(b[i] + c) * m` for all `i` in `range(leng)` where `b[i] != mx` and `(b[i] + c) * (k % m)` for the last occurrence of `mx`; the code prints `res`.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads integers `n`, `m`, and `k`, and a list of `n` integers `a`. It then calculates and prints the minimum total cost for purchasing `k` tickets over `n` days. The cost per ticket can vary daily according to the list `a`. If `k` is less than or equal to `m`, it simply prints the product of the minimum ticket price and `k`. Otherwise, it handles two cases: when `k` is exactly divisible by `m` and when it is not. In the first case, it selects the smallest `k // m` prices from `a`, and in the second case, it includes one additional smallest price if needed. It then calculates the total cost based on these selected prices and prints the result. The function supports up to 10,000 test cases, with constraints on `n`, `m`, and `k` ensuring efficient processing.

