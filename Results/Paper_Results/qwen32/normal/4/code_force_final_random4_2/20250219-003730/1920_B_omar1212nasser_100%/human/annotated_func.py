#State of the program right berfore the function call: n is a positive integer representing the number of elements in the array, k is a positive integer representing the maximum number of elements Alice can remove, x is a positive integer representing the maximum number of elements Bob can multiply by -1, and a is a list of n positive integers representing the elements of the array.
def func_1():
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: `n` is the first input integer from the last iteration, `k` is the second input integer from the last iteration, `x` is the third input integer from the last iteration, `a` is the sorted list of integers from the last iteration, `t` is the original number of iterations, `product` is the value returned by `func_2(k, x, a)` from the last iteration.
#Overall this is what the function does:The function reads multiple test cases, where each test case consists of an integer `n`, integers `k` and `x`, and a list `a` of `n` positive integers. For each test case, it sorts the list `a`, then calculates and prints the maximum possible sum of the list after allowing Alice to remove up to `k` elements and Bob to multiply up to `x` elements by -1.

#State of the program right berfore the function call: removals is a non-negative integer, negatives is a non-negative integer, elements is a list of integers. It is assumed that removals and negatives are such that 0 <= removals, negatives <= len(elements).
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
        
    #State: `removals` is a non-negative integer, `negatives` is a non-negative integer, `elements` is a list of integers, `s` is `sum(elements) - sum(elements[-removals:])`, `s2` is adjusted based on the condition `negatives + i <= len(elements)` for each `i` from 1 to `removals`, and `pos` is a list with `removals + 1` elements, where the first element is `s - 2 * sum(elements[-negatives:])` and the subsequent elements are `s - 2 * s2` after each iteration.
    return max(pos)
    #The program returns the maximum value from the list `pos`, where the first element of `pos` is `s - 2 * sum(elements[-negatives:])` and subsequent elements are `s - 2 * s2` adjusted based on the condition `negatives + i <= len(elements)` for each `i` from 1 to `removals`.
#Overall this is what the function does:The function calculates a list of values based on the sum of elements in the list, adjusting for a specified number of removals and considering the last few negative elements. It returns the maximum value from this list.

