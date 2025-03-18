#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4; for each test case, n and q are integers where 1 ≤ n, q ≤ 3 × 10^5; c is a list of n integers where 1 ≤ c_i ≤ 10^9; l_i and r_i are integers for each query where 1 ≤ l_i ≤ r_i ≤ n. The sum of n over all test cases does not exceed 3 × 10^5, and the sum of q over all test cases does not exceed 3 × 10^5.
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
        
    #State: After all iterations of the loop, `t` is decremented by the number of test cases processed, `n` and `m` are updated to the values provided by the user input for the last test case, `l` remains the list of integers read from input for the last test case, `p` remains the list where each element is the cumulative sum of the elements in `l` up to that point for the last test case, `c` remains the sum of all elements in `l` for the last test case, `x` remains the last element in `l` for the last test case, `m` is now 0, and `s` is the cumulative sum of the elements in `l` up to the index `b - 1` for the last query of the last test case. If `a - 2 >= 0`, `s` is updated to `p[b - 1] - p[a - 2]` for the last query of the last test case. If the length of the subarray from index `a` to `b - 1` in `l` is greater than 1 and `s` is at least twice the length of this subarray, the condition within the if part is met for the last query of the last test case. Otherwise, the condition within the else part is met for the last query of the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers and a series of queries. For each test case, it reads the list of integers and computes a prefix sum array. For each query, it checks if the sum of a specified subarray is at least twice the length of the subarray. If so, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function has no return value, but it has printed the results of all queries.

