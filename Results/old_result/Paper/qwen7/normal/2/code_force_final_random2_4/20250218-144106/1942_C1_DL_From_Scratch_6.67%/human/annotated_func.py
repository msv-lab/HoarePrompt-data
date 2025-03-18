#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2 ⋅ 10^5), and y = 0. The vertices are represented as x distinct integers from 1 to n, and the sum of x over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: After the loop executes all the iterations, `i` will be equal to `x - 2`, `num` will be equal to 1, and `count` will be equal to `x - 2`. The value of `n` will be as initially input by the user. The state of `T` will remain unchanged, and all other variables outside the loop will retain their initial or unchanged values from the preconditions.
    #
    #This conclusion is drawn based on the provided postconditions for the first three iterations. Since the loop runs `T` times, and given the postconditions, `count` increments by 1 each time the inner condition `num == 1` is met, which happens when `i` is `x - 2`. Therefore, after `T` iterations, `count` will be `x - 2`. The value of `i` will always be `x - 2` at the end of each iteration, and `num` will be 1, as per the last condition checked in the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \( T \), \( n \), and \( x \). For each test case, it reads a list of \( x \) distinct integers from 1 to \( n \), sorts this list, and then counts the number of gaps of size 1 between consecutive elements in the sorted list. If the gap between the last element and \( n \) is also 1, this is counted as well. The function returns the total count of such gaps plus \( x - 2 \) for each test case.

