#State of the program right berfore the function call: k and x are non-negative integers such that 1 <= k <= n and 1 <= x <= n, and a is a list of n integers where each integer is in the range 1 <= a_i <= 1000.
def func_1():
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: `i` is equal to `t`, and the loop has finished executing all `t` iterations. For each iteration, `n`, `k`, and `x` were read from the input, `a` was a sorted list of `n` integers, and `product` was calculated using `func_2(k, x, a)`.
#Overall this is what the function does:The function reads multiple test cases, each consisting of integers `n`, `k`, `x`, and a list `a` of `n` integers. For each test case, it sorts the list `a` and calculates a product using the function `func_2` with parameters `k`, `x`, and the sorted list `a`. It then prints the result of this product calculation for each test case.

#State of the program right berfore the function call: removals and negatives are non-negative integers such that 0 <= removals <= len(elements) and 0 <= negatives <= len(elements). elements is a list of integers.
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
        
    #State: `removals` remains the same, `negatives` remains the same, `elements` remains the same, `pos` contains `removals + 1` values, `s` is reduced by the sum of the last `removals` elements of `elements`, `s2` is adjusted based on the elements added or subtracted during the iterations.
    return max(pos)
    #The program returns the maximum value from the list `pos`, which contains `removals + 1` values.
#Overall this is what the function does:The function calculates and returns the maximum value from a list of computed sums based on the input parameters `removals` and `negatives`, and the list `elements`. The list `elements` remains unchanged after the function execution.

