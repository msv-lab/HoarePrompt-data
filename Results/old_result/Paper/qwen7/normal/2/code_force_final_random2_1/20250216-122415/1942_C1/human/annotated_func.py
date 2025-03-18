#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2 ⋅ 10^5), and y = 0; the vertices are represented as x distinct integers from 1 to n; the sum of x over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: The loop has completed all its iterations, and the final value of `count` is the total number of times `num` equals 1 during the loop's execution plus any additional increments due to `n - list0[-1]` being 1. The variable `T` remains an integer such that \(1 \leq T \leq 10^4\), `n` is the last element of the sorted list `list0` plus the final value of `num`, and `x` is the total number of iterations the loop executed. The variable `y` remains unchanged, and `list0` is a sorted list of integers as input.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \(T\), \(n\), \(x\), and \(y\). For each test case, it reads a list of \(x\) distinct integers from 1 to \(n\), sorts the list, and calculates the number of gaps of size 1 between consecutive elements in the sorted list. It also considers the gap between the largest element in the list and \(n\). The function then prints the total count of these gaps plus \(x - 2\). After processing all test cases, it outputs the result for each case.

