#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and q are integers such that 1 ≤ n, q ≤ 3 · 10^5. c is a list of n integers where each element c_i satisfies 1 ≤ c_i ≤ 10^9. For each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n. The sum of n over all test cases does not exceed 3 · 10^5, and the sum of q over all test cases does not exceed 3 · 10^5.
def func_1():
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` and `q` are integers such that 1 ≤ n, q ≤ 3 · 10^5; `c` is a list of n integers where each element c_i satisfies 1 ≤ c_i ≤ 10^9; `a` is a list where the first element is 0 and the next n elements are the integers read from the input; `b` is a list of n + 1 integers where b[i] is the cumulative sum of 1s and 2s based on whether a[i] > 1.
    a = list(accumulate(a))
    print(*a)
    #This is printed: a[0] a[1] a[2] ... a[n-1] (where each a[i] is the cumulative sum of the first i+1 elements of the list c)
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: the loop has executed q times, printing "YES" or "NO" based on the conditions specified, with t, n, q, c, a, and b remaining unchanged.
#Overall this is what the function does:The function `func_1` processes multiple test cases, where each test case consists of a list of integers and a series of queries. For each test case, it calculates cumulative sums of the list and answers queries about sublists, printing "YES" or "NO" based on specific conditions. The function handles up to 10,000 test cases, with constraints on the total number of elements and queries across all test cases.

