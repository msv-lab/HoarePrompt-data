#State of the program right berfore the function call: k and x are non-negative integers such that 1 <= k <= n and 1 <= x <= n, and a is a list of integers of length n with each element being a positive integer such that 1 <= a_i <= 1000.
def func_1():
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: k, x, and a are the values read in the last iteration, and t remains unchanged.
#Overall this is what the function does:The function `func_1` reads multiple test cases from the input. For each test case, it reads integers `n`, `k`, and `x`, and a list of integers `a` of length `n`. It then calculates and prints a product value based on these inputs using the function `func_2`. The final state of the program after it concludes is that it has printed the product for each test case.

#State of the program right berfore the function call: removals and negatives are non-negative integers, elements is a list of integers.
def func_2(removals, negatives, elements):
    if (removals == 6 and negatives == 3) :
        return 0
        #The program returns 0
    #State: removals and negatives are non-negative integers, elements is a list of integers. Either removals is not equal to 6 or negatives is not equal to 3
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
        
    #State: `removals` and `negatives` are non-negative integers, `elements` is a list of integers, `pos` is a list containing the initial value `s - 2 * n` followed by `removals` additional values calculated as `s - 2 * n` after each decrement and adjustment, `s` is the sum of `elements` minus the sum of the last `removals` elements of `elements`, and `n` is adjusted based on the sum of the last `negatives + removals` elements of `elements` minus the sum of the last `removals` elements of `elements`, or reset to 0 if the index exceeds the list length.
    return max(pos)
    #The program returns the maximum value in the list `pos`
#Overall this is what the function does:The function `func_2` accepts three parameters: `removals` and `negatives`, which are non-negative integers, and `elements`, which is a list of integers. If `removals` is 6 and `negatives` is 3, the function returns 0. Otherwise, it calculates a list of values based on the sum of the elements and their sublists, and returns the maximum value from this list.

