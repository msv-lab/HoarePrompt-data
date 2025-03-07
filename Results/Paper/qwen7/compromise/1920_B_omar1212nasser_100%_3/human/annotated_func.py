#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n, k, and x are positive integers such that 1 ≤ n ≤ 2⋅10^5, 1 ≤ x, k ≤ n. a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 1000.
def func_1():
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: After executing the loop for each test case, the output will be a series of lines, each containing the result of the `func_2(k, x, a)` function call for the respective test case, where `a` is the sorted list of integers provided as input for that test case.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads in values for \( n \), \( k \), and \( x \), followed by a list of \( n \) integers. It then sorts the list of integers and calls another function `func_2(k, x, a)` with these parameters. The result of `func_2` is printed for each test case. The function does not return any value but outputs the results of `func_2` for each test case.

#State of the program right berfore the function call: removals is an integer representing the maximum number of elements Alice can remove, negatives is an integer representing the maximum number of elements Bob can multiply by -1, and elements is a list of integers where each element is between 1 and 1000 inclusive.
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
        
    #State: Output State: `pos` is a list containing the values calculated by the formula `s - 2 * s2` for each iteration of the loop, where `s` is the sum of all elements in the `elements` list and `s2` is the sum of the last `negatives + i` elements of `elements`. `removals` is the maximum number of elements Alice can remove, and `negatives` is the maximum number of elements Bob can multiply by -1.
    return max(pos)
    #The program returns the maximum value among the list `pos`, which contains values calculated by the formula `s - 2 * s2` for each iteration of the loop, where `s` is the sum of all elements in the `elements` list and `s2` is the sum of the last `negatives + i` elements of `elements`.
#Overall this is what the function does:The function accepts three parameters: `removals`, `negatives`, and `elements`. `removals` represents the maximum number of elements Alice can remove, `negatives` represents the maximum number of elements Bob can multiply by -1, and `elements` is a list of integers between 1 and 1000. It calculates a series of values using the formula `s - 2 * s2` for each iteration, where `s` is the sum of all elements in `elements`, and `s2` is the sum of the last `negatives + i` elements of `elements`. Finally, it returns the maximum value among these calculated values.

