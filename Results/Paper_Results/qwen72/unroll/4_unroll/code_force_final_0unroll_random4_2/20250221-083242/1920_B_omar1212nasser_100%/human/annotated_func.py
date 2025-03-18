#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, n, k, and x are positive integers such that 1 <= n <= 2 * 10^5, 1 <= k, x <= n, and a is a list of n positive integers such that 1 <= a_i <= 1000.
def func_1():
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: t is an input integer such that 1 <= t <= 10^4, n, k, and x are positive integers such that 1 <= n <= 2 * 10^5, 1 <= k, x <= n, and a is a list of n positive integers such that 1 <= a_i <= 1000. The loop has executed t times, and for each iteration, the sorted list a and the product of func_2(k, x, a) have been printed. The values of n, k, x, and a are reset for each iteration based on the input provided.
#Overall this is what the function does:The function `func_1` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads three integers `n`, `k`, and `x`, and a list `a` of `n` integers. It sorts the list `a` and then calls another function `func_2` with the parameters `k`, `x`, and the sorted list `a`. The result of `func_2` is printed for each test case. The function does not return any value, but it processes and prints the results for `t` test cases. After the function concludes, `t` test cases have been processed, and the output for each case is the result of `func_2` applied to the sorted list `a` and the integers `k` and `x`.

#State of the program right berfore the function call: elements is a list of integers where 1 <= len(elements) <= 2 * 10^5, and each element a_i satisfies 1 <= a_i <= 1000. removals and negatives are non-negative integers such that 1 <= removals, negatives <= len(elements).
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
        
    #State: `elements` is a list of integers where 1 <= len(elements) <= 2 * 10^5, and each element a_i satisfies 1 <= a_i <= 1000. `removals` and `negatives` are non-negative integers such that 1 <= removals, negatives <= len(elements). `pos` is a list with `removals + 1` elements, where the last element is `s - 2 * s2`, and `s` is the sum of all integers in `elements` except the last `removals` integers. `s2` is the sum of the last `negatives` integers in `elements` after the first `removals` integers have been removed.
    return max(pos)
    #The program returns the maximum value from the list `pos`, which has `removals + 1` elements. The last element of `pos` is calculated as `s - 2 * s2`, where `s` is the sum of all integers in `elements` except the last `removals` integers, and `s2` is the sum of the last `negatives` integers in `elements` after the first `removals` integers have been removed. The other elements in `pos` are not specified but are part of the list.
#Overall this is what the function does:The function `func_2` accepts three parameters: `removals`, `negatives`, and `elements`. It returns the maximum value from a list `pos` that has `removals + 1` elements. Each element in `pos` represents the sum of the remaining elements in `elements` after removing the last `i` elements (for `i` ranging from 0 to `removals`), adjusted by subtracting twice the sum of the last `negatives` elements in the modified list. The function does not modify the input list `elements`.

