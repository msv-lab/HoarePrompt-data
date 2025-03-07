#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2·10^5, and a is a list of n integers where 1 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 2·10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        a, b = float('inf'), float('inf')
        
        c = 0
        
        for x in range(n):
            if a > b:
                a, b = b, a
            if l[x] <= a:
                a = l[x]
            elif l[x] <= b:
                b = l[x]
            else:
                a = l[x]
                c += 1
        
        print(c)
        
    #State: `t` is an integer such that 0 ≤ t ≤ 10^4, `n` is an input integer greater than 0, `l` is a list of integers input by the user, `x` is `n-1`. After the loop, `a` is the smallest integer in the list `l`, `b` is the second smallest integer in the list `l` (if it exists), and `c` is the count of integers in the list `l` that are greater than both `a` and `b`.
#Overall this is what the function does:The function processes `t` test cases, where for each test case, it reads an integer `n` and a list `l` of `n` integers. It then identifies the smallest and second smallest integers in the list `l`. The function counts how many integers in the list `l` are greater than both the smallest and second smallest integers. Finally, it prints the count for each test case. After processing all test cases, the function concludes, and the state of the program is that `t` is an integer such that 0 ≤ t ≤ 10^4, `n` is an input integer greater than 0, `l` is a list of integers input by the user, and `x` is `n-1`. The variables `a` and `b` hold the smallest and second smallest integers in the list `l` (if they exist), and `c` is the count of integers in the list `l` that are greater than both `a` and `b`.

