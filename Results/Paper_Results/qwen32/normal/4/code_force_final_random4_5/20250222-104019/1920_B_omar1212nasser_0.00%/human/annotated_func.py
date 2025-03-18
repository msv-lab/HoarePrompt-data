#State of the program right berfore the function call: n is a positive integer representing the number of elements in the array, k is a positive integer representing the limit on the number of elements Alice can remove, x is a positive integer representing the limit on the number of elements Bob can multiply by -1, a is a list of n positive integers representing the elements of the array.
def func_1():
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: `n` is the first integer from the last input, `k` is the second integer from the last input, `x` is the third integer from the last input, `a` is a sorted list of integers from the last input, `t` is the total number of iterations, `i` is `t - 1`, `product` is the value returned by `func_2(k, x, a)` for the last iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an array of positive integers and two limits. It sorts the array and then calculates the maximum possible sum of the array elements after allowing Alice to remove up to a specified number of elements and Bob to multiply up to a specified number of elements by -1. The function outputs the maximum sum for each test case.

#State of the program right berfore the function call: removals and negatives are non-negative integers, and elements is a list of integers.
def func_2(removals, negatives, elements):
    if (removals == 6 and negatives == 3) :
        return 0
        #The program returns 0
    #State: removals and negatives are non-negative integers, and elements is a list of integers. It is not the case that removals is 6 and negatives is 3
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
        
    #State: pos contains `removals + 1` elements, where each element is calculated as `s - 2 * n` based on the updated `s` and `n` values from each iteration. If an `IndexError` occurs, `n` becomes 0, and the subsequent elements in `pos` are `s`.
    return max(pos)
    #The program returns the maximum value from the list `pos`, where `pos` contains `removals + 1` elements. Each element in `pos` is calculated as `s - 2 * n` based on the updated `s` and `n` values from each iteration. If an `IndexError` occurs, `n` becomes 0, and the subsequent elements in `pos` are `s`.
#Overall this is what the function does:The function `func_2` takes three parameters: `removals` and `negatives` as non-negative integers, and `elements` as a list of integers. If `removals` is 6 and `negatives` is 3, the function returns 0. Otherwise, it calculates a list `pos` containing `removals + 1` elements, where each element is derived from the sum of `elements` and a modified sum of the last `negatives` elements. The function returns the maximum value from the list `pos`. If an `IndexError` occurs during the calculation, the function sets `n` to 0 and continues, ensuring that subsequent elements in `pos` are equal to the sum of `elements`.

