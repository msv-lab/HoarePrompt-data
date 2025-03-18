#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2·10^5, and a is a list of n integers where each element a_i satisfies 1 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 2·10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        *inp, = map(int, input().split())
        
        x = y = n + 1
        
        ans = 0
        
        for a in inp:
            if a <= x:
                x = a
            elif a <= y:
                y = a
            else:
                x == y
                y = a
                ans += 1
        
        print(ans)
        
    #State: t is unchanged, n is the number of elements in the last test case, a is the list of integers from the last test case, x and y are the smallest and second smallest elements from the last test case or n + 1, ans is the count of new pairs formed in the last test case.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of an integer `n` and a list `a` of `n` integers. For each test case, it calculates and prints the number of times a new pair of smallest and second smallest elements is formed as it iterates through the list `a`.

