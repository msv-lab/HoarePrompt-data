#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. n, k, and x are positive integers such that 1 <= n <= 2 * 10^5, 1 <= k, x <= n. a is a list of n integers such that 1 <= a_i <= 1000.
def func_1():
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: `t` is an input integer such that 1 <= t <= 10^4, `i` is `t-1`, `n` is the last input integer, `k` is the last input integer, `x` is the last input integer, `a` is a sorted list of integers provided by the user, `product` is the result of `func_2(k, x, a)`.
#Overall this is what the function does:The function `func_1` reads an integer `t` from the input, where `1 <= t <= 10^4`. For each of the `t` test cases, it reads three integers `n`, `k`, and `x` (where `1 <= n <= 2 * 10^5` and `1 <= k, x <= n`), followed by a list `a` of `n` integers (each between 1 and 1000). It sorts the list `a` and then calls another function `func_2` with parameters `k`, `x`, and the sorted list `a`. The result of `func_2` is printed. After processing all `t` test cases, the function concludes.

#State of the program right berfore the function call: elements is a list of integers, removals and negatives are non-negative integers such that 0 <= removals <= len(elements) and 0 <= negatives <= len(elements).
def func_2(removals, negatives, elements):
    pos = []
    s = sum(elements)
    pos.append(s - 2 * sum(elements[-negatives:]))
    s2 = sum(elements[-negatives:])
    for i in range(1, removals + 1):
        s -= elements[-i]
        
        s2 -= elements[-i]
        
        if negatives + i <= len(elements):
            s2 += elements[-(negatives + i)]
        
        pos.append(s - 2 * s2)
        
    #State: `elements` is a list of integers, `removals` is a non-negative integer such that `removals` <= len(`elements`), `negatives` is a non-negative integer such that 0 <= `negatives` <= len(`elements`), `pos` is a list containing `removals + 1` elements. Each element in `pos` is the result of `s - 2 * s2` after each iteration of the loop. `s` is the sum of all integers in `elements` minus the sum of the last `removals` integers in `elements`. If `negatives + removals` is less than or equal to the length of `elements`, `s2` is the sum of the last `negatives` integers in `elements` minus the sum of the last `removals` integers in `elements` plus the sum of the `removals` integers starting from `-(negatives + removals)`. Otherwise, `s2` is the sum of the last `negatives` integers in `elements` minus the sum of the last `removals` integers in `elements`.
    return max(pos)
    #The program returns the maximum value from the list `pos`, which contains `removals + 1` elements. Each element in `pos` is calculated as `s - 2 * s2`, where `s` is the sum of all integers in `elements` minus the sum of the last `removals` integers in `elements`. `s2` is determined based on the condition: if `negatives + removals` is less than or equal to the length of `elements`, `s2` is the sum of the last `negatives` integers in `elements` minus the sum of the last `removals` integers in `elements` plus the sum of the `removals` integers starting from `-(negatives + removals)`. Otherwise, `s2` is the sum of the last `negatives` integers in `elements` minus the sum of the last `removals` integers in `elements`.
#Overall this is what the function does:The function `func_2` accepts three parameters: `removals`, `negatives`, and `elements`. `removals` and `negatives` are non-negative integers, and `elements` is a list of integers. The function calculates a series of values, each representing the sum of all integers in `elements` minus the sum of the last `removals` integers, minus twice the sum of the last `negatives` integers, adjusted for the removal of the last `removals` integers. It returns the maximum value from this series. The final state of the program includes the original `elements` list, the unchanged `removals` and `negatives` parameters, and the calculated maximum value.

