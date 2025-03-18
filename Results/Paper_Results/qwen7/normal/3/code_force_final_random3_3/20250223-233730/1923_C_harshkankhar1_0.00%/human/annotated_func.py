#State of the program right berfore the function call: t is a positive integer; for each test case, n and q are positive integers such that 1 ≤ n, q ≤ 3 × 10^5; c is a list of n positive integers where each integer is between 1 and 10^9 inclusive; for each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n.
def func_1():
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: Output State: After the loop executes all the iterations, `i` will be equal to `n`, `x` will be 1 (since `a[i]` will always be greater than 1 for `i >= 2`), and `b[n]` will be `b[n-1] + 1`.
    #
    #In simpler terms, after the loop completes all its iterations, `i` will be the same as the value of `n`, `x` will always be 1 because `a[i]` starts from the second element of the list `a` which is guaranteed to be greater than 1, and `b[n]` will be the sum of all `x` values, which is essentially `n`.
    a = list(accumulate(a))
    print(*a)
    #This is printed: [accumulated sum of the original list a]
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: After the loop executes all its iterations, `q` will be equal to 0, `x` and `y` will be the last integers entered by the user for each iteration, and the program will print either 'NO' or 'YES' based on the condition `a[y] - a[x - 1] < b[y] - b[x - 1] or x == y'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of positive integers and a set of queries. For each query, it compares the sum of elements in a specified subarray with a calculated value and prints 'YES' if the sum of elements is less than or equal to the calculated value, or 'NO' otherwise. The function does not return any value but prints the results for each query.

