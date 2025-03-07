#State of the program right berfore the function call: n is a positive integer representing the number of elements in the array, k is a positive integer representing the maximum number of elements Alice can remove, x is a positive integer representing the maximum number of elements Bob can multiply by -1, and a is a list of n positive integers representing the elements of the array.
def func_1():
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: `n`, `k`, `x`, and `a` will hold the values from the last iteration, and `t` will be 0.
#Overall this is what the function does:The function reads multiple test cases from the input, where each test case consists of integers `n`, `k`, `x`, and a list `a` of `n` positive integers. For each test case, it calculates the maximum possible sum of the array after Alice can remove up to `k` elements and Bob can multiply up to `x` elements by -1. The result for each test case is printed.

#State of the program right berfore the function call: removals and negatives are non-negative integers, elements is a list of non-negative integers. The length of elements is at least the maximum of removals and negatives.
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
        
    #State: `removals` and `negatives` are non-negative integers, `elements` is a list of non-negative integers, the length of `elements` is at least the maximum of `removals` and `negatives`, `pos` is a list containing `removals + 1` elements, `s` is the sum of the first `len(elements) - removals` elements of `elements`, `s2` is adjusted as described above.
    return max(pos)
    #The program returns the maximum value from the list `pos`, which contains `removals + 1` elements.
#Overall this is what the function does:The function `func_2` calculates and returns the maximum value from a list of computed sums based on the input parameters `removals`, `negatives`, and `elements`. The list `pos` is constructed by iteratively adjusting the sum of the elements in `elements` according to the specified rules, and the function ultimately returns the highest value in this list.

