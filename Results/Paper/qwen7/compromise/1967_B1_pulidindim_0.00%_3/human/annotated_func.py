#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6. It is also guaranteed that the sum of n and the sum of m over all test cases does not exceed 2 ⋅ 10^6.
def func():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        
        count = 2
        
        ans = n
        
        while count <= m:
            countmins = count - 1
            g = n / count
            if g < countmins:
                break
            g -= countmins
            ans += g / count + 1
            count += 1
        
        print(int(ans))
        
    #State: Output State: `t` is the value read from `int(input())`, `i` is `t + 1`, `n` is the last integer input split from `input().split()` after all iterations, `m` is the last value of `m` read from `input().split()` after all iterations, `count` is `m + 1`, `ans` is the final accumulated sum calculated by the loop, `countmins` is `m`, `g` is `n / ((m + 1) * (m + 1)) - m / (m + 1) + 1`.
    #
    #Explanation: After the loop has executed all its iterations, the variable `i` will be equal to `t + 1` because the loop runs `t` times, incrementing `i` from 0 to `t - 1`, and then `i` is incremented one more time after the loop finishes. The variable `count` will be equal to `m + 1` because the loop increments `count` until it is greater than `m`. The variable `ans` will contain the final accumulated sum, which is calculated by adding `g / count + 1` for each iteration from `count = 3` to `count = m + 1`. The variable `countmins` will be `m` when the loop ends. The variable `g` will be updated in the last iteration as `n / ((m + 1) * (m + 1)) - m / (m + 1) + 1`.
#Overall this is what the function does:The function processes a series of test cases, each defined by integers `n` and `m`. For each test case, it calculates a cumulative sum based on `n` and `m`, iterating from 3 up to `m` and updating the sum accordingly. Finally, it prints the computed sum for each test case.

