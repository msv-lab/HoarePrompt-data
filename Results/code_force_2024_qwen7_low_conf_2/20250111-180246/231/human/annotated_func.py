#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 0 ≤ n, m ≤ 2⋅10^5 and 2 ≤ n + m + 1 ≤ 2⋅10^5. a is a list of n + m + 1 integers where 1 ≤ a_i ≤ 10^9, and b is a list of n + m + 1 integers where 1 ≤ b_i ≤ 10^9 and b_i ≠ a_i.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        bounds = [n, m]
        
        a = []
        
        a.append(list(map(int, input().split())))
        
        a.append(list(map(int, input().split())))
        
        bad = -1
        
        badType = -1
        
        cur = [0, 0]
        
        ans = 0
        
        types = [(0) for i in range(n + m + 1)]
        
        for i in range(n + m):
            curType = 0
            if a[0][i] < a[1][i]:
                curType = 1
            if cur[curType] == bounds[curType]:
                curType = 1 - curType
                if bad == -1:
                    bad = i
                    badType = 1 - curType
            types[i] = curType
            ans += a[types[i]][i]
            cur[types[i]] += 1
        
        res = []
        
        for i in range(n + m):
            val = ans - a[types[i]][i]
            if bad != -1 and i < bad and types[i] == badType:
                val = val + a[badType][bad] - a[1 - badType][bad] + a[1 - badType][
                    n + m]
            else:
                val = val + a[types[i]][n + m]
            res.append(val)
        
        res.append(ans)
        
        print(*res)
        
    #State of the program after the  for loop has been executed: `res` is a list of `n + m` elements where each element `res[i]` is calculated based on the given conditions, `t` is the final value after all iterations, `n` and `m` are the final values after all iterations, `bounds` is `[n, m]`, `bad` and `badType` are the final values after all iterations, `cur` is `[n, m]`, `ans` is the final value after all iterations, `types` is the final list after all iterations, and `curType` is the final value after all iterations.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads in two integers \( n \) and \( m \), and two lists \( a \) and \( b \) of length \( n + m + 1 \). It then calculates a list of \( n + m \) values based on specific conditions involving the elements of \( a \) and \( b \). The function identifies the largest values in both lists, determines a type (either 0 or 1) for each position based on the comparison of corresponding elements in \( a \) and \( b \), and adjusts the final result if a particular condition is met. The function outputs the calculated list along with the final value of the sum.

