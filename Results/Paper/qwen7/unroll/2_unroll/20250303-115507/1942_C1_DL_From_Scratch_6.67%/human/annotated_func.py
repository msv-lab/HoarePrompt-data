#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and y = 0. The input also includes a list of x distinct integers from 1 to n representing the vertices Bessie has chosen, and the sum of x over all test cases does not exceed 2⋅10^5.
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
        
        num = n - list0[-1]
        
        if num == 1:
            count += 1
        
        print(count + x - 2)
        
    #State: Output State: The value of `count` is determined by the differences between consecutive elements in the sorted list `list0` for each test case, plus one additional count for the difference between the last element of `list0` and `n`. The final output is the sum of these counts plus `x - 2` for each test case.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads integers n, x, and y along with a list of x distinct integers from 1 to n. It calculates the number of gaps (where the difference between consecutive elements in the sorted list is exactly 1) and adds one more gap for the difference between the last element of the list and n. Finally, it outputs the total count of these gaps plus x - 2 for each test case.

