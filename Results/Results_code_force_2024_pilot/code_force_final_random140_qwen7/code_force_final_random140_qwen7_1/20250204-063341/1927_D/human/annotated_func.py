#State of the program right berfore the function call: t is a positive integer; n is an integer such that 2 <= n <= 2 * 10^5; the array a is a list of n integers where each integer is in the range [1, 10^6]; q is an integer such that 1 <= q <= 2 * 10^5; each query is represented by two integers l and r such that 1 <= l < r <= n.
def func():
    R = lambda : map(int, input().split())
    t, = R()
    while t:
        t -= 1
        
        R()
        
        a = [0]
        
        p = i = j = 0
        
        for x in R():
            j = (j, i)[x != p]
            a += j,
            p = x
            i += 1
        
        q, = R()
        
        while q:
            q -= 1
            l, r = R()
            print(*((a[r], r), [-1] * 2)[a[r] < l])
        
    #State: Output State: `t` is 0, `a` is a list containing the sum of `j` for each iteration, where `j` is the value of `i` from the last iteration, `p` is the last value returned by `R()` before the assignment, `i` is equal to the total number of iterations, `q` is 0, `l` is the last value returned by `R()` during the final query, `r` is the last value returned by `R()` during the final query.
    #
    #Explanation: After the loop has executed all its iterations, the variable `t` will be decremented to 0 because the loop continues as long as `t` is greater than 0. The variable `q` will also be 0 since it is decremented by 1 after each query, and there are no more queries to process once `q` reaches 0. The variable `a` will contain the sum of `j` for each iteration, with `j` being the value of `i` from the last iteration, as this value is used to append to the list `a` in each iteration. The variable `p` will hold the last value returned by `R()` before the assignment, and `i` will be equal to the total number of iterations, which is the same as the final value of `i` after the loop completes. The values of `l` and `r` will be the last values returned by `R()` during the final query, as these values are updated each time through the loop.
#Overall this is what the function does:The function processes a series of queries on an array `a`. It first reads the number of test cases `t`, and for each test case, it reads additional parameters and constructs an array `a` based on certain rules. Then, it processes `q` queries, each defined by two integers `l` and `r`. For each query, it checks if the element at index `r` in array `a` is greater than or equal to `l`. If so, it prints the element at index `r` and the index `r`. Otherwise, it prints `-1` twice. After processing all queries, the function outputs the results of these queries.

