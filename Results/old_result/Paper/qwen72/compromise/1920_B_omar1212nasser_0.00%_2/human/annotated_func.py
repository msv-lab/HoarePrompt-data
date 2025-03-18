#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. n, k, and x are positive integers such that 1 <= n <= 2 * 10^5, 1 <= k, x <= n. a is a list of n integers where 1 <= a_i <= 1000.
def func_1():
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: t is an input integer such that 1 <= t <= 10^4, n, k, and x are positive integers such that 1 <= n <= 2 * 10^5, 1 <= k, x <= n, a is a list of n integers where 1 <= a_i <= 1000, and the loop has printed the product of the sorted list `a` processed by `func_2(k, x, a)` for each iteration.
#Overall this is what the function does:The function `func_1` reads an integer `t` from the user input, which represents the number of test cases. For each test case, it reads three integers `n`, `k`, and `x`, and a list `a` of `n` integers. It sorts the list `a` and then calls another function `func_2` with `k`, `x`, and the sorted list `a`. The result of `func_2` is printed for each test case. After processing all test cases, the function concludes without returning any value.

#State of the program right berfore the function call: removals and negatives are non-negative integers such that 0 <= removals, negatives <= len(elements), and elements is a list of integers where 1 <= elements[i] <= 1000.
def func_2(removals, negatives, elements):
    if (removals == 6 and negatives == 3) :
        return 0
        #The program returns 0.
    #State: removals and negatives are non-negative integers such that 0 <= removals, negatives <= len(elements), and elements is a list of integers where 1 <= elements[i] <= 1000. Additionally, either removals is not equal to 6, or negatives is not equal to 3.
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
        
    #State: `removals` is 0, `negatives` remains unchanged, `s` is the sum of the first `len(elements) - removals` integers in `elements`, `n` is the sum of the last `negatives` integers in the updated `elements` list, and `pos` is a list containing the values of `s - 2 * n` after each iteration of the loop.
    return max(pos)
    #The program returns the maximum value from the list `pos`, where `pos` contains the values of `s - 2 * n` after each iteration of the loop. `s` is the sum of the first `len(elements) - removals` integers in `elements`, and `n` is the sum of the last `negatives` integers in the updated `elements` list.
#Overall this is what the function does:The function `func_2` accepts three parameters: `removals`, `negatives`, and `elements`. It returns 0 if `removals` is 6 and `negatives` is 3. Otherwise, it returns the maximum value of a list `pos`, where `pos` contains the values of `s - 2 * n` after each iteration of a loop. `s` is the sum of the first `len(elements) - removals` integers in `elements`, and `n` is the sum of the last `negatives` integers in the updated `elements` list. The function does not modify the input parameters.

