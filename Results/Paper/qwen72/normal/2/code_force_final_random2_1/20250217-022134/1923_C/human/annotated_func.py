#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4; for each test case, n and q are integers where 1 ≤ n, q ≤ 3 · 10^5; c is a list of n integers where 1 ≤ c_i ≤ 10^9; l_i and r_i are integers for each query where 1 ≤ l_i ≤ r_i ≤ n; the sum of n over all test cases does not exceed 3 · 10^5; the sum of q over all test cases does not exceed 3 · 10^5.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        p = []
        
        c = 0
        
        for x in l:
            c += x
            p.append(c)
        
        for _ in range(m):
            a, b = map(int, input().split())
            s = p[b - 1]
            if a - 2 >= 0:
                s -= p[a - 2]
            if b - a + 1 > 1 and s >= 2 * (b - a + 1):
                print('YES')
            else:
                print('NO')
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `n` and `m` are integers read from user input, `l` is a list of integers derived from user input, `p` is a list containing the cumulative sums of the elements in `l`, `c` is the sum of all integers in the list `l`, `x` is the last integer in the list `l`, `_` is the total number of iterations performed, which is the sum of the lengths of all lists `l` plus the total number of queries `m` across all test cases, `a` and `b` are integers read from user input, and `m` is 0. For each iteration, if `a - 2 >= 0`, `s` is the cumulative sum up to the (b-1)-th element in the list `l` minus the cumulative sum up to the (a-2)-th element in the list `l`. Otherwise, `s` remains the cumulative sum up to the (b-1)-th element in the list `l`. If `b - a + 1 > 1` and `s >= 2 * (b - a + 1)`, the program prints 'YES'. Otherwise, the program prints 'NO'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers and a series of queries. For each query, it determines whether the sum of a specified subarray is at least twice the length of the subarray. If so, it prints 'YES'; otherwise, it prints 'NO'. The function reads input values for the number of test cases, the length of the list, the list itself, and the queries. It maintains a cumulative sum list to efficiently compute subarray sums. After processing all queries for all test cases, the function completes without returning any value.

