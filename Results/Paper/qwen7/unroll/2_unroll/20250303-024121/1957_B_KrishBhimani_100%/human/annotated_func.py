#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of two integers n and k such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9, and the sum of all n values across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: t test cases are processed. For each test case, if n is 1, the output is k. Otherwise, the output is a list containing two elements: (2^i - 1) and (k - (2^i - 1)), followed by enough zeros to make the list length equal to n.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of two integers \( n \) and \( k \). For each test case, if \( n = 1 \), it outputs \( k \). Otherwise, it calculates and outputs a list containing two elements: \( (2^i - 1) \) and \( (k - (2^i - 1)) \), followed by enough zeros to make the list length equal to \( n \). After processing all test cases, it outputs the results for each test case.

