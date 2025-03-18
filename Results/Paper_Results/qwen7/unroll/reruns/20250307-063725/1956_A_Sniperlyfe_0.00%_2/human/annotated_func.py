#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100, and p is a list of k positive integers where 1 <= p[0] < p[1] < ... < p[k-1] <= 100.
def func_1(n, p):
    while n >= min(p):
        n -= sum(1 for x in p if x <= n)
        
    #State: Output State: n is 0 and p remains a list of k positive integers where 1 <= p[0] < p[1] < ... < p[k-1] <= 100.
    #
    #Explanation: The loop continues as long as `n` is greater than or equal to the minimum value in the list `p`. In each iteration, `n` is decreased by the count of elements in `p` that are less than or equal to `n`. Since `p` is a strictly increasing list of positive integers, eventually `n` will become less than the smallest element in `p`, at which point the condition `n >= min(p)` will no longer be true, and the loop will terminate. At this point, `n` will be 0, and `p` will remain unchanged because it is not modified within the loop.
    return n
    #n is 0 and p remains a list of k positive integers where 1 <= p[0] < p[1] < ... < p[k-1] <= 100.
#Overall this is what the function does:The function accepts two parameters: `n`, a positive integer between 1 and 100 (inclusive), and `p`, a list of k positive integers in strictly increasing order between 1 and 100 (inclusive). It decreases the value of `n` by the count of elements in `p` that are less than or equal to `n`, until `n` becomes less than the smallest element in `p`. After the loop terminates, the function returns `n`, which will be 0, and the list `p` remains unchanged.

#State of the program right berfore the function call: k and q are positive integers such that 1 <= k, q <= 100. p is a list of k positive integers where 1 <= p[0] < p[1] < ... < p[k-1] <= 100. qs is a list of q positive integers where 1 <= qs[i] <= 100 for all 0 <= i < q.
def func_2():
    t = int(input())
    for _ in range(t):
        k, q = map(int, input().split())
        
        p = list(map(int, input().split()))
        
        qs = list(map(int, input().split()))
        
        res = []
        
        for n in qs:
            res.append(func_1(n, p))
            print(' '.join(map(str, res)))
        
    #State: After executing the loop for t iterations, the output state will consist of t lists, each containing q elements. Each element in these lists is the result of calling `func_1(n, p)` for each `n` in `qs`, where `p` is a list of k sorted integers provided in each iteration. The output is formatted as a series of lines, with each line containing q space-separated integers representing the results of `func_1` for that particular iteration.
#Overall this is what the function does:The function processes multiple test cases (determined by the variable `t`). For each test case, it reads two positive integers `k` and `q`, followed by a list `p` of `k` sorted positive integers and a list `qs` of `q` positive integers. It then calls another function `func_1` for each element in `qs`, checking if each element is present in `p`. The results are stored in a list `res` and printed for each test case, forming a series of lines, each containing `q` space-separated boolean values indicating the presence of each element in `qs` within `p`.

