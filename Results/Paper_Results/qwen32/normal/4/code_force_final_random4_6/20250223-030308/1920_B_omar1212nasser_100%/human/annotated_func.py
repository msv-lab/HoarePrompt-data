#State of the program right berfore the function call: n is a positive integer representing the number of elements in the array, k is a positive integer representing the limit on the number of elements Alice can remove, x is a positive integer representing the limit on the number of elements Bob can multiply by -1, and a is a list of n positive integers representing the elements of the array.
def func_1():
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: `i` is `t-1`; `n`, `k`, and `x` are the values read in the last iteration; `a` is the sorted list of integers read in the last iteration; `product` is the value returned by `func_2(k, x, a)` from the last iteration; `t` is the total number of iterations.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n`, integers `k` and `x`, and a list `a` of `n` positive integers. For each test case, it sorts the list `a` and computes the maximum possible sum of the array after allowing Alice to remove up to `k` elements and Bob to multiply up to `x` elements by -1. It then prints the computed sum for each test case.

#State of the program right berfore the function call: removals and negatives are non-negative integers, elements is a list of integers such that 0 <= removals <= len(elements) and 0 <= negatives <= len(elements).
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
        
    #State: - `removals`: Remains unchanged.
    #- `negatives`: Remains unchanged.
    #- `elements`: Remains unchanged.
    #- `pos`: Contains `removals + 1` elements, starting with the initial value and followed by `removals` additional values calculated as `s - 2 * s2` after each iteration.
    #- `s`: Decremented by the sum of the last `removals` elements of `elements`.
    #- `s2`: Adjusted based on the elements added and removed during the loop.
    #
    #Output State:
    return max(pos)
    #The program returns the maximum value in the `pos` list, which contains `removals + 1` elements starting with an initial value and followed by `removals` additional values calculated as `s - 2 * s2` after each iteration.
#Overall this is what the function does:The function calculates and returns the maximum value from a list of `removals + 1` elements. This list is generated based on the input list `elements` and the integers `removals` and `negatives`. The first element of the list is derived from the sum of `elements` and the subsequent elements are calculated by iteratively adjusting the sum of `elements` and a subset of its last elements.

