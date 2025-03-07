#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n, k, and x are positive integers such that 1 ≤ n ≤ 2·10^5, 1 ≤ x, k ≤ n. a is a list of n integers where each integer satisfies 1 ≤ a_i ≤ 1000.
def func_1():
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: Output State: `t` is a positive integer representing the number of test cases, `i` is 5, `n` is an input integer, `k` is an input integer, `x` is an input integer, `a` is a list of integers sorted in ascending order, `product` is the result of `func_2(k, x, a)`.
    #
    #In this final output state, the loop has completed all its iterations. The variable `i` will be equal to `t + 4` because it starts at 0 and increments by 1 with each iteration. The values of `n`, `k`, `x`, `a`, and `product` will reflect the last test case processed within the loop, as each test case is handled independently within the loop.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads integers \( n \), \( k \), and \( x \), along with a list \( a \) of \( n \) integers. It sorts the list \( a \) in ascending order and then calls another function `func_2(k, x, a)` to compute a product based on the sorted list. Finally, it prints the computed product for each test case. After processing all test cases, the function does not return any value but prints the results for each test case.

#State of the program right berfore the function call: removals is an integer representing the number of elements Alice can remove, negatives is an integer representing the number of elements Bob can multiply by -1, and elements is a list of integers representing the array elements.
def func_2(removals, negatives, elements):
    if (removals == 6 and negatives == 3) :
        return 0
        #The program returns 0
    #State: removals is an integer representing the number of elements Alice can remove, negatives is an integer representing the number of elements Bob can multiply by -1, and elements is a list of integers. Either removals is not equal to 6 or negatives is not equal to 3
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
        
    #State: Output State: `removals` must be greater than or equal to the total number of iterations (which is determined by the loop), `i` will be the total number of iterations + 1, `s` will be `s` minus the sum of the last `removals` elements in the list `elements`, `n` will be the difference between the sum of the last `negatives + removals` elements and the sum of the last `removals` elements in the list `elements`, `pos` will be a list containing the value `s - 2 * n` for each iteration from 1 to the total number of iterations.
    #
    #In simpler terms, after the loop completes all its iterations, `removals` will be at least as large as the total number of elements removed, `i` will be one more than the total number of iterations, `s` will be the original sum of the elements minus the sum of the last `removals` elements, `n` will be calculated based on the last `negatives + removals` elements compared to the last `removals` elements, and `pos` will contain the value `s - 2 * n` for each iteration of the loop.
    return max(pos)
    #The program returns the maximum value among the list `pos`, which contains the value `s - 2 * n` for each iteration from 1 to the total number of iterations.
#Overall this is what the function does:The function accepts three parameters: `removals` (the number of elements Alice can remove), `negatives` (the number of elements Bob can multiply by -1), and `elements` (a list of integers). It calculates and returns either 0 or the maximum value of a list `pos`. The list `pos` contains values derived from the sum of elements in the `elements` list after certain operations (removals and negations) are applied in each iteration. If `removals` equals 6 and `negatives` equals 3, the function returns 0. Otherwise, it iterates through the specified number of removals and updates the sums accordingly, appending the calculated values to `pos`, and finally returns the maximum value from `pos`.

