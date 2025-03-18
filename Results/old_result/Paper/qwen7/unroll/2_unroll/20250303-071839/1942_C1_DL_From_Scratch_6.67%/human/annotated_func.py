#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are positive integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and y = 0. The vertices Bessie has chosen are represented by x distinct integers from 1 to n. The sum of x over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: The value of `count` is determined by the differences between consecutive elements in the sorted list `list0`, starting from index `x-1` to the second last element, and also considering the difference between the last element of `list0` and `n`. Specifically, if the difference between two consecutive elements is exactly 1, then `count` is incremented by 1. Additionally, if the difference between `n` and the last element of `list0` is exactly 1, then `count` is incremented by 1. The final value of `count` plus `x-2` is printed for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers n, x, and y along with x distinct integers representing vertices. It calculates and prints the value of `count` plus `x-2`, where `count` is incremented by 1 for each pair of consecutive elements in the sorted list of vertices that have a difference of exactly 1, and also for the difference between the last vertex and n if it is exactly 1.

