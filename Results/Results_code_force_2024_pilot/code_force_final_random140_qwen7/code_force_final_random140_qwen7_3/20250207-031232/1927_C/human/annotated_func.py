#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^5; k is an even integer such that 2 ≤ k ≤ 2⋅min(n, m); a is a list of n integers such that 1 ≤ a_i ≤ 10^6; b is a list of m integers such that 1 ≤ b_j ≤ 10^6; the sum of values n and m over all test cases in a test does not exceed 4⋅10^5.
def func():
    for t in range(int(input())):
        n, m, k = map(int, input().split())
        
        a = frozenset(map(int, input().split()))
        
        b = frozenset(map(int, input().split()))
        
        leftOnes = 0
        
        aOnes = 0
        
        bOnes = 0
        
        newk = k // 2
        
        i = 1
        
        while i <= k:
            if i in a and i in b:
                leftOnes += 1
            elif i in a:
                aOnes += 1
            elif i in b:
                bOnes += 1
            else:
                break
            i += 1
        
        i = 0
        
        while i < leftOnes:
            if aOnes < bOnes:
                aOnes += 1
            else:
                bOnes += 1
            i += 1
        
        if aOnes == newk and bOnes == newk:
            print('yes')
        else:
            print('no')
        
    #State: Output State: After the loop executes all the iterations, `t` will be equal to the total number of test cases, `n`, `m`, and `k` will retain their initial values, `a` and `b` will be frozensets containing the respective integers from the inputs, `leftOnes` will be a non-negative integer representing the count of numbers present in both `a` and `b` within the range `[1, k]`, `aOnes` will be an integer representing the count of numbers present only in `a` within the range `[1, k]`, `bOnes` will be an integer representing the count of numbers present only in `b` within the range `[1, k]`, `newk` will be `k // 2`, and `i` will be equal to `leftOnes`.
    #
    #The final output will be 'yes' if `aOnes` equals `newk` and `bOnes` equals `newk`, and 'no' otherwise.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers t, n, m, k, a (a set of n integers), and b (a set of m integers). For each test case, it counts the number of integers present in both sets a and b within the range [1, k], the number of integers present only in set a, and the number of integers present only in set b within the same range. It then checks if the counts of integers present only in set a and only in set b are equal to half of k. If both counts match, it prints 'yes'; otherwise, it prints 'no'. The function does not return any value explicitly but prints the result for each test case.

