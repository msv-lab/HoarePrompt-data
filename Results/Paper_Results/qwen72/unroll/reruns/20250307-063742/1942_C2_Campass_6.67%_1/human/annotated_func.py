#State of the program right berfore the function call: The function is expected to handle multiple test cases. For each test case, n is an integer representing the number of sides of the polygon (4 ≤ n ≤ 10^9), x is an integer representing the number of vertices Bessie has chosen (2 ≤ x ≤ min(n, 2 · 10^5)), and y is an integer representing the maximum number of other vertices you can choose (0 ≤ y ≤ n - x). The list of x vertices chosen by Bessie contains distinct integers from 1 to n. The sum of x over all test cases does not exceed 2 · 10^5.
def func():
    R = lambda : map(int, input().split())
    t, = R()
    while t:
        t -= 1
        
        n, x, y = R()
        
        sx = 0
        
        l = list(R())
        
        l.sort()
        
        l.append(n + l[0])
        
        val = []
        
        for i in range(1, x + 1):
            c = l[i] - l[i - 1] - 1
            if c == 1:
                sx += 1
            val.append(c)
        
        val.sort(key=lambda x: (1 - x & 1, x))
        
        for i in val:
            c = i // 2
            if y < c:
                sx += y * 2
                break
            sx += i
            y -= c
        
        cons = x + sx - 2
        
        cons = min(n - 2, cons)
        
        print(cons)
        
    #State: The loop iterates `t` times, and for each iteration, it processes the values of `n`, `x`, and `y` from the input. The variable `cons` is calculated based on the values in the list `l` and the variables `x` and `y`. After all iterations, the final value of `t` is 0, and the values of `n`, `x`, and `y` are the last set of values read from the input. The list `l` and the variable `cons` are reinitialized and recalculated for each iteration, so their final values are based on the last iteration.
#Overall this is what the function does:The function processes multiple test cases, each defined by the number of sides of a polygon `n`, the number of vertices Bessie has chosen `x`, and the maximum number of additional vertices you can choose `y`. For each test case, it calculates and prints the maximum number of non-adjacent vertices that can be chosen from the remaining vertices, ensuring that the total number of chosen vertices does not exceed `n - 2`. The function does not return any value; it only prints the result for each test case. After processing all test cases, the function ends with `t` set to 0, and the last processed values of `n`, `x`, and `y` are the final values of these variables.

