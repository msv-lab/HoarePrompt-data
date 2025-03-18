#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 4 ≤ n ≤ 10^9, x is an integer such that 2 ≤ x ≤ min(n, 2 · 10^5), and y is 0. Additionally, there are x distinct integers provided in the second line of each test case, each representing a vertex chosen by Bessie and ranging from 1 to n. The sum of x across all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `T` is 0; `n`, `x`, and `y` are integers read from the input in the last iteration; `list0` is a sorted list of integers read from the input in the last iteration; `count` is the number of times `list0[i + 1] - list0[i] - 1` equals 1 for `i` ranging from 0 to `x - 2` in the last iteration, and `count` has been incremented by 1 if `num` was 1 in the last iteration; `num` is `n - list0[-1]` in the last iteration. If `num` is 1, `count` has been incremented by 1.
#Overall this is what the function does:The function processes multiple test cases where each test case consists of an integer `n`, an integer `x`, and a list of `x` distinct integers. It calculates and prints a specific count for each test case based on the differences between consecutive integers in the sorted list and the difference between `n` and the largest integer in the list.

