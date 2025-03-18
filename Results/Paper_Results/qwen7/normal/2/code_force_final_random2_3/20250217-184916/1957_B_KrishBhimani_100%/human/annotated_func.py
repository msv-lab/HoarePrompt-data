#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of two positive integers n and k such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9, and the sum of all n values across all test cases does not exceed 2⋅10^5.
def func():
    for _ in range(int(input())):
        l1 = input().split()
        
        n, k = list(map(int, l1))
        
        if n == 1:
            print(k)
        else:
            arr = []
            k0 = k
            i = 0
            ans = []
            temp = 1
            while True:
                if temp * 2 < k:
                    temp *= 2
                    i += 1
                else:
                    break
            ans.append((1 << i) - 1)
            ans.append(k - sum(ans))
            ans += [0] * (n - len(ans))
            print(*ans)
        
    #State: Output State: The loop will have executed all iterations based on the input provided. For each test case, the variable `ans` will contain a list of integers where the first element is \((1 << i) - 1\), the second element is \(k - (1 << i) - 1\), and the rest of the elements are 0s to make the total length of the list equal to `n`. Here, `i` is determined as the number of times `temp * 2` is less than `k` before it is no longer true, with `temp` being the largest power of 2 less than or equal to `k`. If `n` is 1, `ans` will simply be `[k]`.
    #
    #The state of other variables such as `l1`, `n`, `k`, `k0`, `arr`, and `temp` will be as described for the last iteration of the loop. Specifically, `l1` will be the list of strings obtained from the last input, `n` and `k` will be the integers obtained from the last input, `k0` will be equal to `k`, `arr` will be an empty list, and `temp` will be the largest power of 2 less than or equal to `k` if `n` is not 1. If `n` is 1, these variables will retain their values from the last input without further changes.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers \( n \) and \( k \). For each test case, it calculates a list of integers \( ans \) based on the value of \( k \) and the length \( n \). If \( n = 1 \), the list contains only \( k \). Otherwise, the list starts with \((1 << i) - 1\) followed by \( k - (1 << i) - 1\), and is padded with zeros to reach a length of \( n \). The function prints the resulting list for each test case.

