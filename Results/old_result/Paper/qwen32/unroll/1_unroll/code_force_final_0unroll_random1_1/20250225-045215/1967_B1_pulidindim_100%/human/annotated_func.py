#State of the program right berfore the function call: Each test case consists of two positive integers n and m (1 ≤ n, m ≤ 2 ⋅ 10^6). The number of test cases t satisfies 1 ≤ t ≤ 10^4, and the sum of n and the sum of m over all test cases do not exceed 2 ⋅ 10^6.
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
        
    #State: The final printed `ans` values for each of the `t` test cases.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers `n` and `m`. For each test case, it calculates and prints a specific value `ans` based on the provided integers `n` and `m`. The function handles up to `t` test cases, where `t` is the number of test cases provided as input.

