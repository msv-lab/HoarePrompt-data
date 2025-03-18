#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n and k are positive integers such that 1 ≤ n ≤ 2 \cdot 10^5 and 1 ≤ k ≤ 10^9; the sum of all n over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: Output State: All test cases have been processed; `t` is now the total number of test cases; for each test case, `n` is the first element of `l1` converted to an integer; `k` is the second element of `l1` converted to an integer; `k0` is equal to the original `k` for each test case; `arr` is either an empty list or a list of length `n` depending on the value of `n`; `ans` is a list containing either two or three elements depending on the value of `n`, where the elements are calculated based on the logic inside the loop; `temp` is a power of 2 (either 1, 2, 4, 8, 16, etc.) for each test case; `i` is either 0, 1, 2, or 3 for each test case, indicating the number of times `temp` was doubled before breaking the loop.
    #
    #This output state describes the final conditions after all iterations of the loop have completed, with each variable reflecting its state after processing all test cases according to the given logic.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \( n \) and \( k \). For each test case, it calculates a list \( ans \) based on the value of \( n \) and \( k \). If \( n = 1 \), it simply prints \( k \). Otherwise, it constructs \( ans \) such that it contains two or three elements, where the elements are derived from the binary representation of \( k \). Finally, it prints the constructed list \( ans \) for each test case. After processing all test cases, the function implicitly returns nothing, but the printed output represents the final state of the program.

