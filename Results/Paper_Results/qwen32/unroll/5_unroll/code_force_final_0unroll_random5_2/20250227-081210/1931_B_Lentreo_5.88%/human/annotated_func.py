#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, there are two lines: the first line contains an integer n (1 ≤ n ≤ 2 \cdot 10^5) representing the number of containers, and the second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ 10^9) representing the amounts of water in the containers. It is guaranteed that the sum of a_i for each test case is divisible by n and does not exceed 2 \cdot 10^9. The sum of n over all test cases does not exceed 2 \cdot 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().strip().split()))
        
        last = nums[-1]
        
        curr = 0
        
        for i in nums:
            if i != 0:
                curr += i - last
        
        if curr == 0:
            print('YES')
        else:
            print('NO')
        
    #State: The variable `t` remains unchanged as it represents the number of test cases. For each test case, the program reads an integer `n` and a list of integers `nums`. It calculates a value `curr` by iterating through `nums` and adding the difference between each non-zero element and the last element of `nums`. If `curr` is 0 after processing all test cases, it prints 'YES'; otherwise, it prints 'NO'. The specific values of `n`, `nums`, `last`, and `curr` are not preserved across test cases and are determined anew for each iteration of the outer loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of containers and the amounts of water in those containers. For each test case, it determines if it's possible to redistribute the water such that all containers have the same amount by only moving water from non-zero containers to the last container. It prints 'YES' if such redistribution is possible, otherwise 'NO'.

