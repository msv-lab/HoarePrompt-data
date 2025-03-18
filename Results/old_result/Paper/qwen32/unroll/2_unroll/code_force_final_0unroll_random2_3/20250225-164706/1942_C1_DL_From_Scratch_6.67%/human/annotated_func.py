#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, for each test case, n is an integer such that 4 ≤ n ≤ 10^9, x is an integer such that 2 ≤ x ≤ min(n, 2 · 10^5), y is 0, and the second line of each test case consists of x distinct integers from 1 to n representing the vertices Bessie has chosen. The sum of x over all test cases does not exceed 2 · 10^5.
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
        
    #State: T is an input integer, t is an integer such that 1 ≤ t ≤ 10^4, for each test case, n is an integer such that 4 ≤ n ≤ 10^9, x is an integer such that 2 ≤ x ≤ min(n, 2 · 10^5), y is 0, and the second line of each test case consists of x distinct integers from 1 to n representing the vertices Bessie has chosen. The sum of x over all test cases does not exceed 2 · 10^5.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of vertices `n`, a number of chosen vertices `x`, and a list of `x` distinct vertices. It calculates and prints a result for each test case based on the gaps between the chosen vertices and their positions relative to the total number of vertices.

