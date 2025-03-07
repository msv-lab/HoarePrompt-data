#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each of the next t lines contains two positive integers n and m such that 1 ≤ n, m ≤ 2 ⋅ 10^6. The sum of all n and the sum of all m across all test cases do not exceed 2 ⋅ 10^6.
def func():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        
        count = 2
        
        ans = n
        
        while count <= m:
            countmins = int(count - 1)
            g = int(n / count)
            if g < countmins:
                break
            g -= countmins
            ans += int(g / count) + 1
            count += 1
        
        print(int(ans))
        
    #State: `i` is equal to `t`, `t` remains the same, `n` and `m` are the values from the last test case, `count` is `m + 1` for the last test case, `ans` is the final accumulated sum for the last test case.
#Overall this is what the function does:The function reads a positive integer `t` representing the number of test cases. For each test case, it reads two positive integers `n` and `m`. It then computes and prints a specific value `ans` for each test case based on the given logic involving `n` and `m`.

