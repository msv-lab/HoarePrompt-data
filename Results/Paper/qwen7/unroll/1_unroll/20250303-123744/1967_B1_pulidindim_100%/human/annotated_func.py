#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6. It is also guaranteed that the sum of n and the sum of m over all test cases do not exceed 2 ⋅ 10^6.
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
        
    #State: Output State: The value of `t` test cases where for each test case, `n` is incremented based on the given logic inside the loop, and the final value of `ans` is printed for each test case. Specifically, for each test case, `ans` is updated by adding the integer division of `(g / count) + 1` where `g` is calculated as `n // count` and `countmins` is `count - 1`. The loop continues until `count` exceeds `m` or the condition `g < countmins` is met.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `t`, `n`, and `m`. For each test case, it calculates and prints an updated value of `n` based on a specific algorithm. The algorithm involves incrementing `n` by a value derived from dividing `n` by a counter `count`, adjusted by `count - 1`, until the counter exceeds `m` or the division result is less than `count - 1`. The function outputs the final calculated value of `n` for each test case.

