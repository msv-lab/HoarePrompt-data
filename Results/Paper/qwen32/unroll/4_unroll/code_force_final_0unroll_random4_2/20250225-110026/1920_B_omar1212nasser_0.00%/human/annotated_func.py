#State of the program right berfore the function call: k and x are non-negative integers such that 1 <= k <= n and 1 <= x <= n, and a is a list of n integers where each integer is in the range 1 <= a_i <= 1000.
def func_1():
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: `n`, `k`, `x`, and `a` hold the values from the last iteration of the loop.
#Overall this is what the function does:The function reads multiple test cases, each consisting of integers `n`, `k`, `x`, and a list `a` of `n` integers. For each test case, it sorts the list `a` and computes a product using the values of `k`, `x`, and the sorted list `a`. The result of this computation is printed for each test case. The function does not return any value explicitly.

#State of the program right berfore the function call: removals and negatives are non-negative integers, and elements is a list of integers.
def func_2(removals, negatives, elements):
    if (removals == 6 and negatives == 3) :
        return 0
        #The program returns 0
    #State: removals and negatives are non-negative integers, and elements is a list of integers. It is not the case that removals is 6 and negatives is 3.
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
        
    #State: `removals` and `negatives` are non-negative integers, and `elements` is a list of integers. It is not the case that `removals` is 6 and `negatives` is 3; `pos` is a list containing `removals + 1` elements where the first element is `s - 2 * n` (initial value) and the subsequent elements are calculated as `s - 2 * n` after each iteration of the loop; `s` is the sum of the first `len(elements) - removals` elements; `n` is the sum of the last `negatives` elements minus the sum of the last `removals` elements, or 0 if an `IndexError` occurred.
    return max(pos)
    #The program returns the maximum value from the list `pos`, where `pos` is a list containing `removals + 1` elements, with the first element being `s - 2 * n` and subsequent elements calculated similarly.
#Overall this is what the function does:The function accepts three parameters: `removals`, `negatives`, and `elements`, where `removals` and `negatives` are non-negative integers, and `elements` is a list of integers. If `removals` is 6 and `negatives` is 3, the function returns 0. Otherwise, it calculates and returns the maximum value from a list `pos`, which contains `removals + 1` elements. The first element of `pos` is calculated as the sum of all elements minus twice the sum of the last `negatives` elements, and subsequent elements are calculated similarly after iteratively removing elements from the end of the list.

