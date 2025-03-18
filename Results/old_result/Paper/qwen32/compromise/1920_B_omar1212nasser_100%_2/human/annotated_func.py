#State of the program right berfore the function call: n, k, and x are integers such that 1 <= n, k, x <= 2 * 10^5, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 1000.
def func_1():
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: `n`, `k`, `x`, and `a` are the values read and processed in the last iteration of the loop.
#Overall this is what the function does:The function reads multiple test cases, each consisting of integers `n`, `k`, `x`, and a list `a` of `n` integers. For each test case, it sorts the list `a` and computes a product using the values of `k`, `x`, and the sorted list `a`. The computed product is then printed.

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
        
    #State: `removals` and `negatives` are non-negative integers such that 0 <= `removals` <= len(`elements`) and 0 <= `negatives` <= len(`elements`). `elements` is a list of integers. `pos` is a list containing `removals + 1` elements, starting with `s - 2 * sum(elements[-negatives:])` and followed by values calculated as `s - 2 * s2` after each iteration of the loop. `s` is the sum of the integers in `elements` minus the sum of the last `removals` elements. `s2` is the sum of the last `negatives` elements in `elements` adjusted by the last `removals` elements.
    return max(pos)
    #The program returns the maximum value from the list `pos`.
#Overall this is what the function does:The function calculates and returns the maximum value from a list of computed sums based on the input list of integers (`elements`), the number of elements to remove from the end (`removals`), and the number of elements to consider as negative (`negatives`).

