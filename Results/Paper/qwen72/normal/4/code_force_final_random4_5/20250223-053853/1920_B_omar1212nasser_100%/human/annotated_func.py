#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, n, k, and x are positive integers such that 1 <= n <= 2 * 10^5 and 1 <= k, x <= n, and a is a list of n positive integers such that 1 <= a_i <= 1000.
def func_1():
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: The loop has executed `t` times, and for each iteration, the values of `n`, `k`, and `x` have been read from input, a list `a` of `n` positive integers has been read, sorted, and then the product of the first `k` elements of the sorted list `a` that are less than or equal to `x` has been calculated and printed. The variables `n`, `k`, `x`, and `a` are reset in each iteration, so their final values after the loop are the values from the last iteration.
#Overall this is what the function does:The function `func_1` reads a positive integer `t` from the input, indicating the number of test cases. For each test case, it reads three positive integers `n`, `k`, and `x`, and a list `a` of `n` positive integers. It sorts the list `a` and then calculates the product of the first `k` elements in the sorted list that are less than or equal to `x` using the function `func_2`. The product is printed for each test case. After all test cases are processed, the function has no return value, but the variables `n`, `k`, `x`, and `a` retain the values from the last test case.

#State of the program right berfore the function call: removals and negatives are non-negative integers such that 0 <= removals, negatives <= len(elements), and elements is a list of integers.
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
        
    #State: `removals` and `negatives` remain non-negative integers such that 0 <= `removals`, `negatives` <= len(`elements`), `elements` is a list of integers, `pos` is a list containing `removals + 1` elements, where the last element is `s - 2 * s2`, `s` is the sum of all integers in `elements` except the last `removals` integers, `s2` is the sum of the last `negatives` integers in `elements` except the last `removals` integers.
    return max(pos)
    #The program returns the maximum value from the list `pos`, which contains `removals + 1` elements, with the last element being `s - 2 * s2`, where `s` is the sum of all integers in `elements` except the last `removals` integers, and `s2` is the sum of the last `negatives` integers in `elements` except the last `removals` integers.
#Overall this is what the function does:The function `func_2` accepts three parameters: `removals`, `negatives`, and `elements`. It returns the maximum value from a list `pos` of `removals + 1` elements. Each element in `pos` represents the sum of the integers in `elements` up to the point where `removals` elements have been removed from the end, minus twice the sum of the last `negatives` elements (also adjusted for the removed elements). The final state of the program is such that `removals` and `negatives` remain unchanged, `elements` is not modified, and `pos` contains `removals + 1` elements, with the last element being the result of the final adjustment.

