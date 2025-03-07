#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n, k, and x are positive integers such that 1 ≤ n ≤ 2⋅10^5, 1 ≤ x, k ≤ n. a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 1000.
def func_1():
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: Output State: `t` must be equal to the total number of test cases, `i` is `t-1`, `k` is the last input integer among all test cases, `x` is the corresponding last input integer, `a` is a list of integers sorted in ascending order for the last test case, `product` is the result of `func_2(k, x, a)`.
    #
    #This means that after the loop has executed all its iterations, `t` will hold the exact count of test cases, `i` will be `t-1` since the loop runs from `0` to `t-1`, and for the last test case, `k` and `x` will be the integers obtained from the last input, `a` will be the sorted list of integers for that last test case, and `product` will be the result of applying the function `func_2(k, x, a)` to that list.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads three integers \( n \), \( k \), and \( x \), and a list \( a \) of \( n \) integers. It sorts the list \( a \) in ascending order and then calls another function `func_2(k, x, a)` to compute a product based on these inputs. Finally, it prints the computed product for each test case. After processing all test cases, the function outputs the results for each one.

#State of the program right berfore the function call: removals is an integer representing the maximum number of elements Alice can remove, negatives is an integer representing the maximum number of elements Bob can multiply by -1, and elements is a list of integers representing the array elements.
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
        
    #State: Output State: The loop will execute `removals` times. After all iterations, `i` will be equal to `removals`, `s2` will be updated to include the sum of the last `negatives + removals` elements of `elements`, provided `negatives + removals` is less than or equal to the length of `elements`. The list `pos` will contain `removals` elements, each calculated as `s - 2 * s2`.
    #
    #In simpler terms, after the loop completes all its iterations, the variable `i` will be equal to the original value of `removals`. The variable `s2` will be the sum of the last `negatives + removals` elements of the `elements` list. The list `pos` will contain `removals` elements, each computed as `s - 2 * s2`.
    return max(pos)
    #The program returns the maximum value among `removals` elements in the list `pos`, where each element is calculated as `s - 2 * s2`, and `s2` is the sum of the last `negatives + removals` elements of the `elements` list.
#Overall this is what the function does:The function accepts three parameters: `removals` (the maximum number of elements Alice can remove), `negatives` (the maximum number of elements Bob can multiply by -1), and `elements` (a list of integers representing the array elements). It calculates a series of values based on these parameters and the elements list, storing them in a list called `pos`. Each value in `pos` is computed as `s - 2 * s2`, where `s` is the initial sum of the elements list and `s2` is the sum of the last `negatives + i` elements of the list, with `i` ranging from 1 to `removals`. Finally, the function returns the maximum value found in the `pos` list.

