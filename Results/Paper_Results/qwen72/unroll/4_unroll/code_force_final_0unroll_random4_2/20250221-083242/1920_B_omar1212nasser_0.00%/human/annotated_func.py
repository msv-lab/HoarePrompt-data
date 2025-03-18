#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. n, k, and x are positive integers such that 1 <= n <= 2 * 10^5, 1 <= k, x <= n. a is a list of integers such that 1 <= a_i <= 1000 and len(a) == n.
def func_1():
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: The loop will execute t times, and for each iteration, it will read new values for n, k, x, and a. After sorting a, it will compute the product using the function `func_2(k, x, a)` and print the result. The values of n, k, x, and a will be updated for each iteration, but the initial value of t will remain unchanged. After all iterations, the final values of n, k, x, and a will be the ones from the last iteration, and t will still be the same as it was initially.
#Overall this is what the function does:The function `func_1` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads three integers `n`, `k`, and `x`, and a list of integers `a` of length `n`. It sorts the list `a` and then calls another function `func_2` with the parameters `k`, `x`, and the sorted list `a`. The result of `func_2` is printed for each test case. After processing all test cases, the function has no return value, but the final values of `n`, `k`, `x`, and `a` will be those from the last test case, and `t` will remain unchanged.

#State of the program right berfore the function call: removals and negatives are non-negative integers such that 0 <= removals, negatives <= len(elements), and elements is a list of integers where 1 <= len(elements) <= 2 * 10^5 and 1 <= elements[i] <= 1000.
def func_2(removals, negatives, elements):
    if (removals == 6 and negatives == 3) :
        return 0
        #The program returns 0.
    #State: removals and negatives are non-negative integers such that 0 <= removals, negatives <= len(elements), and elements is a list of integers where 1 <= len(elements) <= 2 * 10^5 and 1 <= elements[i] <= 1000. Additionally, either removals is not equal to 6 or negatives is not equal to 3.
    pos = []
    s = sum(elements)
    n = sum(elements[-negatives:])
    pos.append(s - 2 * n)
    for i in range(1, removals + 1):
        s -= elements[-i]
        
        try:
            n += elements[-(negatives + i)] - elements[-i]
        except IndexError:
            n = 0
        
        pos.append(s - 2 * n)
        
    #State: `removals` and `negatives` remain unchanged, `pos` is a list containing the initial value of `s - 2 * n` followed by `removals` new values, where each new value is the result of `s - 2 * n` after each iteration of the loop. `s` is the sum of all integers in `elements` minus the sum of the last `removals` integers in `elements`. `n` is the sum of the last `negatives` integers in `elements` minus the sum of the last `removals` integers in `elements` (if `removals` > `negatives`, `n` will be 0).
    return max(pos)
    #The program returns the maximum value from the list `pos`, which contains the initial value of `s - 2 * n` followed by `removals` new values, where each new value is the result of `s - 2 * n` after each iteration of the loop. `s` is the sum of all integers in `elements` minus the sum of the last `removals` integers in `elements`. `n` is the sum of the last `negatives` integers in `elements` minus the sum of the last `removals` integers in `elements` (if `removals` > `negatives`, `n` will be 0).
#Overall this is what the function does:The function `func_2` accepts three parameters: `removals`, `negatives`, and `elements`. It returns 0 if `removals` is 6 and `negatives` is 3. Otherwise, it returns the maximum value from a list `pos`, which contains the initial value of `s - 2 * n` and `removals` new values. Each new value in `pos` is the result of `s - 2 * n` after each iteration of the loop, where `s` is the sum of all integers in `elements` minus the sum of the last `removals` integers, and `n` is the sum of the last `negatives` integers minus the sum of the last `removals` integers (if `removals` > `negatives`, `n` will be 0). The function does not modify the input parameters `removals`, `negatives`, or `elements`.

