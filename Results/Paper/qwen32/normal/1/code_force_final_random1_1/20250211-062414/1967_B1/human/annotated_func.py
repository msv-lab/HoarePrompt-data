#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. For each test case, n and m are positive integers such that 1 <= n, m <= 2 * 10^6. The sum of all n values and the sum of all m values across all test cases do not exceed 2 * 10^6.
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
        
    #State: The final `ans` value printed for the last iteration of the outer loop, with `i` equal to `t-1`, and `count` being `m + 1` if the inner loop completed all iterations without breaking, otherwise, it will be the value of `count` when the loop broke.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of two positive integers `n` and `m`. For each test case, it calculates and prints a specific value `ans` based on the given logic. The value `ans` is derived by iteratively adjusting `n` and `m` according to the rules defined within the function until a certain condition is met.

