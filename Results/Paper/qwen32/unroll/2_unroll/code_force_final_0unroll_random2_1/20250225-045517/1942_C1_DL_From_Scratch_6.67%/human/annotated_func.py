#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 4 ≤ n ≤ 10^9, x is an integer such that 2 ≤ x ≤ min(n, 2 · 10^5), and y is 0. The second line of each test case consists of x distinct integers from 1 to n, representing the vertices Bessie has chosen. The sum of x over all test cases does not exceed 2 · 10^5.
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
        
    #State: The output state consists of T lines, where each line contains the result of the calculation `count + x - 2` for each test case, with `count` being the number of gaps of size 1 between the sorted vertices and the gap between the last vertex and `n`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a total number of vertices `n`, a number of chosen vertices `x`, and a list of `x` distinct chosen vertices. For each test case, it calculates and prints a result based on the number of gaps of size 1 between the sorted chosen vertices and the gap between the last chosen vertex and `n`.

