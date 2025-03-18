#State of the program right berfore the function call: n is a positive integer representing the number of elements in the array, k is a positive integer representing the maximum number of elements Alice can remove, x is a positive integer representing the maximum number of elements Bob can multiply by -1, and a is a list of n positive integers representing the elements of the array.
def func_1():
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: `n`, `k`, `x`, and `a` will have the values they had in the last iteration of the loop.
#Overall this is what the function does:The function reads multiple test cases, where each test case consists of three integers `n`, `k`, and `x`, and a list of `n` positive integers. For each test case, it calculates and prints the maximum possible sum of the list after allowing Alice to remove up to `k` elements and Bob to multiply up to `x` elements by -1.

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
        
    #State: `removals` and `negatives` are non-negative integers such that 0 <= `removals` <= len(`elements`) and 0 <= `negatives` <= len(`elements`). `elements` is a list of integers. `pos` is a list with `removals + 1` elements, where the first element is `s - 2 * s2` (initial value) and the subsequent elements are calculated as `s - 2 * s2` after each iteration, with `s` and `s2` updated as described. `s` is the sum of `elements` after removing the last `removals` elements. `s2` is the sum of the last `negatives` elements in `elements` after the loop, considering the conditional additions and subtractions.`
    return max(pos)
    #The program returns the maximum value in the list `pos`, where each element in `pos` is calculated as `s - 2 * s2` after each iteration, with `s` being the sum of `elements` after removing the last `removals` elements, and `s2` being the sum of the last `negatives` elements in `elements` after the loop, considering the conditional additions and subtractions.
#Overall this is what the function does:The function calculates and returns the maximum value of a list `pos`, where each element in `pos` is computed as the difference between the sum of all elements in the input list `elements` minus twice the sum of the last `negatives` elements, after iteratively removing the last `removals` elements from `elements`.

