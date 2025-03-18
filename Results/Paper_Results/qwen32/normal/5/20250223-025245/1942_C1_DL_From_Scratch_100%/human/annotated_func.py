#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 4 ≤ n ≤ 10^9, x is an integer such that 2 ≤ x ≤ min(n, 2 * 10^5), and y is 0. The sum of x over all test cases does not exceed 2 * 10^5. The second line of each test case consists of x distinct integers from 1 to n, representing the vertices Bessie has chosen.
def func():
    T = int(input())
    for _ in range(T):
        n, x, y = map(int, input().split())
        
        list0 = list(map(int, input().split()))
        
        list0 = sorted(list0)
        
        count = 0
        
        for i in range(x - 1):
            num = list0[i + 1] - list0[i] - 1
            if num == 1:
                count += 1
        
        num = list0[0] + n - list0[-1] - 1
        
        if num == 1:
            count += 1
        
        print(count + x - 2)
        
    #State: T is 0, t is an integer such that 1 ≤ t ≤ 10^4, n is the first integer from the last input, x is the second integer from the last input, y is the third integer from the last input, list0 is the sorted list from the last input, and the final output is the cumulative sum of `count + x - 2` for all T iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`, an integer `x`, and a list of `x` distinct integers. It calculates and prints a value for each test case based on the given inputs, which appears to represent the number of certain conditions met by the list of integers relative to `n`.

