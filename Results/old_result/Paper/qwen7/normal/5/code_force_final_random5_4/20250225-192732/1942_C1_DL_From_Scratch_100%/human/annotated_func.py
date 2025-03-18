#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and y = 0. The vertices Bessie has chosen are represented by x distinct integers from 1 to n. The sum of x over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: After the loop executes all iterations, `count` will be the total number of times `num` equals 1 across all iterations, plus `(x - 2)` for each iteration. `T` will be 0 since all iterations have been completed. `n`, `x`, and `y` will retain their values from the last iteration. `list0` will be the sorted list of integers from the last input. `i` will be `x-2` for the last iteration, and `num` will be calculated as `list0[0] + n - list0[-1] - 1` for the last iteration, potentially equaling 1 if the condition is met.
    #
    #In summary, `count` accumulates the number of times `num` equals 1 over all iterations, and `T` becomes 0 indicating the end of the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \( n \), \( x \), and \( y \). For each test case, it reads \( x \) distinct integers representing vertices and calculates the number of gaps of length 1 between consecutive vertices. Additionally, it checks the gap between the first and last vertex. The function returns the total count of such gaps for all test cases.

