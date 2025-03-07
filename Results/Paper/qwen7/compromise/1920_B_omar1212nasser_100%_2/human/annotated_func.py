#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n, k, and x are positive integers such that 1 ≤ n ≤ 2 ⋅ 10^5, 1 ≤ x, k ≤ n. a is a list of n integers where 1 ≤ a_i ≤ 1000 for all 1 ≤ i ≤ n.
def func_1():
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: After executing the loop for each test case, the output will be a series of lines, each containing the result of the `func_2(k, x, a)` function call for that test case, where `a` is a sorted list of integers provided as input for that test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads three integers \( n \), \( k \), and \( x \), followed by a list of \( n \) integers \( a \). It sorts the list \( a \) and then calls another function `func_2(k, x, a)` to compute a product based on the sorted list. Finally, it prints the result of `func_2(k, x, a)` for each test case.

#State of the program right berfore the function call: removals is an integer representing the maximum number of elements Alice can remove, negatives is an integer representing the maximum number of elements Bob can multiply by -1, and elements is a list of integers representing the array.
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
        
    #State: Output State: `pos` is a list of integers where each element is calculated as `s - 2 * s2` for each iteration of the loop, `removals` remains the same as its initial value, `negatives` remains the same as its initial value, and `elements` is the same list of integers as in the initial state but with the last `i` elements removed for each iteration of the loop.
    return max(pos)
    #The program returns the maximum value from the list `pos`, which is composed of elements calculated as `s - 2 * s2` for each iteration of the loop, with the last `i` elements removed from the original `elements` list for each iteration.
#Overall this is what the function does:The function accepts three parameters: `removals`, `negatives`, and `elements`. `removals` represents the maximum number of elements Alice can remove, `negatives` represents the maximum number of elements Bob can multiply by -1, and `elements` is a list of integers. The function calculates a series of values based on the sum of the elements and their subsets, removing elements in each iteration and adjusting sums accordingly. It then returns the maximum value from this series of calculated values.

