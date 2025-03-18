#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, n, k, and x are positive integers such that 1 <= n <= 2 * 10^5 and 1 <= k, x <= n, and a is a list of positive integers such that 1 <= a_i <= 1000.
def func_1():
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: The loop has executed `t` times, and for each iteration, the values of `n`, `k`, and `x` have been read from input, the list `a` has been sorted, and the product of the function `func_2(k, x, a)` has been printed. The values of `n`, `k`, `x`, and `a` are not retained between iterations, so they will be reinitialized for each iteration. After the loop finishes, `t` remains the same, and the values of `n`, `k`, `x`, and `a` are undefined (or reset to their initial state before the loop started for the next iteration).
#Overall this is what the function does:The function `func_1` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads three integers `n`, `k`, and `x`, and a list `a` of `n` integers from the input. It sorts the list `a` and then calls another function `func_2` with the parameters `k`, `x`, and the sorted list `a`. The result of `func_2` is printed for each test case. After all test cases are processed, `t` remains the same, and the values of `n`, `k`, `x`, and `a` are undefined for the next iteration. The function does not return any value.

#State of the program right berfore the function call: removals and negatives are non-negative integers such that 0 <= removals, negatives <= len(elements), and elements is a list of integers where each element is in the range 1 <= a_i <= 1000.
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
        
    #State: `removals` and `negatives` remain non-negative integers such that 0 <= `removals`, `negatives` <= len(`elements`). `elements` is a list of integers where each element is in the range 1 <= a_i <= 1000. `pos` is a list containing the values of `s - 2 * s2` after each iteration of the loop. `s` is the sum of all elements in `elements` minus the sum of the last `removals` elements. `s2` is the sum of the last `negatives` elements in `elements` minus the sum of the last `removals` elements plus the sum of the `negatives` elements that are `removals` positions before the end of the list.
    return max(pos)
    #The program returns the maximum value from the list `pos`, which contains the results of the expression `s - 2 * s2` calculated after each iteration of the loop. `s` is the sum of all elements in `elements` minus the sum of the last `removals` elements. `s2` is the sum of the last `negatives` elements in `elements` minus the sum of the last `removals` elements plus the sum of the `negatives` elements that are `removals` positions before the end of the list.
#Overall this is what the function does:The function `func_2` accepts three parameters: `removals`, `negatives`, and `elements`. It returns the maximum value from a list `pos` that contains the results of the expression `s - 2 * s2` after each iteration of a loop. Here, `s` is the sum of all elements in `elements` minus the sum of the last `removals` elements, and `s2` is the sum of the last `negatives` elements in `elements` adjusted by subtracting the sum of the last `removals` elements and adding the sum of the `negatives` elements that are `removals` positions before the end of the list. The function does not modify the input parameters `removals`, `negatives`, or `elements`.

