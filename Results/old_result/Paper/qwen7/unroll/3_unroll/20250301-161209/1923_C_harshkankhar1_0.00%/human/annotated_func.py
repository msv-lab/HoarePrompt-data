#State of the program right berfore the function call: t is a positive integer, and for each test case, n and q are positive integers such that 1 ≤ n, q ≤ 3 × 10^5. The array c is a list of n positive integers where each integer is between 1 and 10^9 inclusive. For each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n.
def func_1():
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: Output State: `t` is a positive integer, `n` is an input integer, `q` is an input integer, `a` is a list starting with 0 followed by integers from the input, `b` is a list of length `n + 1` where each element `b[i]` (for `i` from 1 to `n`) is equal to `x * i`, with `x` being 1 if `a[i] > 1` or 2 if `a[i] <= 1`.
    #
    #In this output state, the variable `b` is updated such that each element `b[i]` (for `i` from 1 to `n`) is the sum of the previous element `b[i-1]` and `x`, where `x` is 1 if the corresponding element `a[i]` is greater than 1, otherwise `x` is 2.
    a = list(accumulate(a))
    print(*a)
    #This is printed: [accumulated sums of the list up to each index]
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: Output State: t is a positive integer, n is an input integer, q is an input integer, a is a list where each element is the accumulated sum of the list up to that index, b is a list of length n + 1 where each element b[i] (for i from 1 to n) is the sum of the previous element b[i-1] and 1 if the corresponding element a[i] is greater than 1 or 2 if a[i] is less than or equal to 1, the loop has executed q times, and for each iteration, it reads two integers x and y from input, then prints 'NO' if a[y] - a[x - 1] is less than b[y] - b[x - 1] or if x equals y, otherwise it prints 'YES'.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it first reads the size of the array `n`, the number of queries `q`, and the array `c`. It then updates an auxiliary array `b` based on the values in `c`. After that, it prints the accumulated sums of `c` up to each index. Finally, for each query, it compares the difference between the accumulated sums at indices `y` and `x-1` with the corresponding differences in the auxiliary array `b`, and prints 'YES' if the condition is met or 'NO' otherwise.

