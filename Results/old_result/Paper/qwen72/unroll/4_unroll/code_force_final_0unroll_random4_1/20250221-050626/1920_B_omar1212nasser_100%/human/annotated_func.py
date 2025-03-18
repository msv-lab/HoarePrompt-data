#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, n, k, and x are positive integers such that 1 <= n <= 2 * 10^5 and 1 <= k, x <= n, and a is a list of n positive integers such that 1 <= a_i <= 1000.
def func_1():
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: t is an input integer such that 1 <= t <= 10^4, n, k, and x are positive integers such that 1 <= n <= 2 * 10^5 and 1 <= k, x <= n, and a is a list of n positive integers such that 1 <= a_i <= 1000. The loop has executed t times, and for each iteration, the sorted list a and the product of func_2(k, x, a) have been printed. The variables n, k, x, and a are reinitialized for each iteration based on the input provided.
#Overall this is what the function does:The function `func_1` reads an integer `t` from the input, which represents the number of test cases. For each of the `t` test cases, it reads three integers `n`, `k`, and `x`, and a list of `n` integers `a`. It sorts the list `a` and then calls another function `func_2` with the parameters `k`, `x`, and the sorted list `a`. The result of `func_2` is printed for each test case. After all test cases are processed, the function concludes. The variables `n`, `k`, `x`, and `a` are reinitialized for each test case based on the input provided.

#State of the program right berfore the function call: removals and negatives are non-negative integers such that 0 <= removals, negatives <= len(elements), and elements is a list of integers where 1 <= elements[i] <= 1000.
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
        
    #State: `removals` and `negatives` are non-negative integers such that 0 <= `removals`, `negatives` <= len(`elements`), `elements` is a list of integers where 1 <= `elements[i]` <= 1000, `s` is the sum of all integers in `elements` except the last `removals` elements, `s2` is the sum of the last `negatives` elements of `elements` after removing the last `removals` elements, `pos` is a list containing the initial value and the value of `s` minus twice the sum of the last `negatives` elements of `elements` after each iteration of the loop.
    return max(pos)
    #The program returns the maximum value from the list `pos`, which contains the initial value of `s` and the value of `s` minus twice the sum of the last `negatives` elements of `elements` after each iteration of the loop.
#Overall this is what the function does:The function `func_2` accepts three parameters: `removals`, `negatives`, and `elements`. It calculates a series of values based on the sum of the elements in the list, adjusting for the removal of the last `removals` elements and the sum of the last `negatives` elements. The function returns the maximum value from this series. The final state of the program is that `removals` and `negatives` remain unchanged, `elements` is not modified, and the returned value is the maximum of the calculated series.

