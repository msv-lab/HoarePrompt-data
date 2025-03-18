#State of the program right berfore the function call: n is a positive integer representing the number of elements in the array, k is a positive integer representing the maximum number of elements Alice can remove, x is a positive integer representing the maximum number of elements Bob can multiply by -1, and a is a list of n positive integers.
def func_1():
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: Output State:
#Overall this is what the function does:The function reads multiple test cases, each consisting of integers `n`, `k`, and `x`, and a list `a` of `n` positive integers. For each test case, it calculates and prints the maximum possible sum of the remaining elements in the array `a` after allowing Alice to remove up to `k` elements and Bob to multiply up to `x` elements by -1.

#State of the program right berfore the function call: removals and negatives are non-negative integers, and elements is a list of integers.
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
    #   - `negatives`: Remains unchanged.
    #   - `elements`: Remains unchanged.
    #   - `pos`: Contains `removals + 1` elements, with the last `removals` elements calculated as `s - 2 * s2` after each iteration.
    #   - `s`: Reduced by the sum of the last `removals` elements.
    #   - `s2`: Adjusted based on the removal of the last `removals` elements and the inclusion of new elements if applicable.
    #
    #Output State:
    return max(pos)
    #The program returns the maximum value in the list `pos`.
#Overall this is what the function does:The function calculates and returns the maximum value from a list of computed values based on the input list `elements`, the number of `removals`, and the count of `negatives`. The original list `elements` and the integers `removals` and `negatives` remain unchanged.

