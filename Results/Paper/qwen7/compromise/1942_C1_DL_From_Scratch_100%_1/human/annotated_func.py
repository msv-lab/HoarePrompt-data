#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and y = 0; the sum of x over all test cases does not exceed 2⋅10^5; the first line of each test case contains three integers n, x, and y; the second line of each test case contains x distinct integers from 1 to n, representing the vertices Bessie has chosen.
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
        
    #State: Output State: After the loop executes all iterations, `count` will be equal to the total number of times `num` equals 1 across all iterations, plus `x - 2` for each iteration. `T` will be 0 since all test cases have been processed. The values of `n`, `x`, and `y` will be as per the last test case's input, and `list0` will be the sorted list of integers from the last test case's input. The variable `i` will be `x - 1` for the last iteration, and `num` will be calculated based on the last `list0` but will not affect the final `count` value since the loop has completed.
    #
    #In simpler terms, after all iterations, `count` will sum up all instances where the difference between consecutive elements in `list0` is exactly 1, plus `x - 2` for each test case. `T` will be 0 because there are no more test cases to process. The other variables (`n`, `x`, `y`, `list0`, `i`, and `num`) will reflect the state of the last test case.
#Overall this is what the function does:The function processes multiple test cases, each containing integers n, x, and y, followed by x distinct integers from 1 to n. It calculates and prints the total number of times the difference between consecutive elements in the list of integers is exactly 1, plus (x - 2) for each test case. After processing all test cases, the function outputs the results for each case.

