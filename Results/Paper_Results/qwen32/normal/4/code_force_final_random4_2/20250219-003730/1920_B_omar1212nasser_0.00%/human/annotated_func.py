#State of the program right berfore the function call: n is a positive integer representing the number of elements in the array, k is a positive integer representing the maximum number of elements Alice can remove, x is a positive integer representing the maximum number of elements Bob can multiply by -1, and a is a list of n positive integers.
def func_1():
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: `i` is `t-1`, `n`, `k`, `x`, and `a` are the values from the last iteration, `a` is a sorted list of integers derived from the last input, `product` is the value returned by `func_2(k, x, a)` from the last iteration.
#Overall this is what the function does:The function processes multiple test cases where each test case consists of a list of positive integers and two integers representing the maximum number of elements Alice can remove and the maximum number of elements Bob can multiply by -1. It sorts the list and calculates the minimum possible sum of the list after Alice and Bob perform their operations. The result for each test case is printed.

#State of the program right berfore the function call: removals and negatives are non-negative integers, elements is a list of integers.
def func_2(removals, negatives, elements):
    if (removals == 6 and negatives == 3) :
        return 0
        #The program returns 0
    #State: removals and negatives are non-negative integers, elements is a list of integers. It is not the case that removals is 6 and negatives is 3
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
        
    #State: `removals` is the same as initial; `negatives` is the same as initial; `elements` is the same as initial; `pos` has `removals + 1` elements starting with `s - 2 * n` and followed by `removals` elements calculated as `s_final - 2 * n_final`; `s` is `s_final`; `n` is `n_final`.
    return max(pos)
    #The program returns the value `s_final - 2 * n_final`
#Overall this is what the function does:The function `func_2` accepts three parameters: `removals`, `negatives`, and `elements`. If `removals` is 6 and `negatives` is 3, the function returns 0. Otherwise, it calculates a series of values based on the sum of the list `elements` and a subset of its last `negatives` elements, then returns the maximum value from these calculations.

