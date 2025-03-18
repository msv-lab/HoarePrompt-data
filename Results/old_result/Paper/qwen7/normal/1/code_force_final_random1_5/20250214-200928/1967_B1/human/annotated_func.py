#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6. It is also guaranteed that the sum of n and the sum of m over all test cases does not exceed 2 ⋅ 10^6.
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
        
    #State: `t` must be greater than 0, `i` is equal to `t`, `n` is the integer value of the first input, `m` is the integer value of the second input, `count` is `m + 1`, `ans` is the sum of `n` plus the result of `int(g / count) + 1` added `m` times, `countmins` is `int(m)`, `g` is `int(n / (m + 1)) - 1`
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n` and `m`. For each test case, it calculates a result based on `n` and `m` using a specific algorithm involving a loop and arithmetic operations. The function prints the calculated result for each test case and returns nothing.

