#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n, k, and x are positive integers such that 1 ≤ n ≤ 2⋅10^5, 1 ≤ x, k ≤ n. a is a list of n integers where each integer satisfies 1 ≤ a_i ≤ 1000.
def func_1():
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: Output State: `t` is a positive integer, `i` is equal to `t`, `n` is an input integer, `k` is an input integer, `x` is an input integer, `a` is a sorted list of integers obtained from splitting the input string and converting each element to an integer, `product` is the result of the final call to `func_2(k, x, a)` after the loop has completed all its iterations.
    #
    #This means that after all iterations of the loop have finished, the variable `i` will be equal to `t` (since the loop runs from `0` to `t-1`), and the `product` variable will hold the result of the last call to `func_2(k, x, a)` executed within the loop. The values of `t`, `n`, `k`, `x`, and the list `a` will remain as they were after the last iteration of the loop.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads three integers \( n \), \( k \), and \( x \), and a list \( a \) of \( n \) integers. It sorts the list \( a \) and then calls another function `func_2(k, x, a)` to compute a product value. After processing all test cases, it prints the computed product for each case. The final state includes the number of test cases processed (`t`), the index `i` set to `t`, and the computed product for the last test case.

#State of the program right berfore the function call: removals is an integer representing the maximum number of elements Alice can remove, negatives is an integer representing the maximum number of elements Bob can multiply by -1, and elements is a list of integers representing the array.
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
        
    #State: Output State: The final state of the loop will be as follows:
    #
    #- `s` will be the original value of `s` minus the sum of the last `removals` elements of the list `elements`.
    #- `s2` will be the original value of `s2` minus the sum of the last `removals` elements of the list `elements`.
    #- If `negatives + removals` is less than or equal to the length of `elements`, then `s2` will also include the addition of the element at the index `-(negatives + removals)` from the end of the list `elements`.
    #- `pos` will be a list containing the values of `s - 2 * s2` after each iteration of the loop, starting from the first iteration up to the last iteration where `i` equals `removals`.
    #
    #In simpler terms, after all iterations of the loop, `s` and `s2` will reflect the cumulative effect of removing the last `removals` elements and optionally adjusting `s2` based on the condition involving `negatives`. The list `pos` will contain the computed values of `s - 2 * s2` for each iteration of the loop.
    return max(pos)
    #The program returns the maximum value among the list `pos`, which contains the computed values of `s - 2 * s2` for each iteration of the loop, starting from the first iteration up to the last iteration where `i` equals `removals`.
#Overall this is what the function does:The function accepts three parameters: `removals` (the maximum number of elements Alice can remove), `negatives` (the maximum number of elements Bob can multiply by -1), and `elements` (a list of integers). It calculates a series of values based on removing elements and optionally negating some elements, storing these values in a list. Finally, it returns the maximum value from this list.

