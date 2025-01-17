#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 0 ≤ n, m ≤ 2⋅10^5 and 2 ≤ n + m + 1 ≤ 2⋅10^5. a_i and b_i are sequences of integers where 1 ≤ a_i, b_i ≤ 10^9 and a_i ≠ b_i for all i.
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
        
    #State of the program after the  for loop has been executed: \( t \) is an integer such that \( 1 \leq t \leq 10^4 \), \( n \) and \( m \) are integers such that \( 0 \leq n, m \leq 2 \times 10^5 \) and \( 2 \leq n + m + 1 \leq 2 \times 10^5 \), \( a \) is a list of two lists of integers, \( bad \) and \( badType \) are integers, \( types \) is a list of integers, \( ans \) is the sum of selected elements from \( a \) based on the loop logic, \( res \) is a list of length \( n + m + 1 \) containing the values of \( val \) for each iteration and the final \( ans \).
#Overall this is what the function does:The function processes `t` test cases, where for each test case, it accepts integers `n` and `m` along with two sequences `a_i` and `b_i`. It then calculates a series of values based on the relative ordering of elements in these sequences and stores them in a list `res`. After processing, the function prints the contents of `res`, which includes `n + m + 1` values: the final sum `ans` and `n + m` intermediate values calculated during the process. Specifically, the function identifies a "bad" element and its type, updates a running total `ans` based on the current type of elements, and adjusts the final values in `res` if the "bad" element is encountered before the point where it should be processed according to the loop logic.

