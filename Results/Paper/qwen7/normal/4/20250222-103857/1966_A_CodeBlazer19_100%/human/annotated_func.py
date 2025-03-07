#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500; for each test case, n and k are integers such that 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100; the list of integers c contains n integers such that 1 ≤ c_i ≤ 100 for each c_i in c.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        p = [l.count(j) for j in set(l)]
        
        if max(p) >= k:
            print(k - 1)
        else:
            print(n)
        
    #State: Output State: `t` must be greater than or equal to the total number of test cases, `i` is equal to `t`, `n` is an input integer converted to an integer, `k` is an input integer converted to an integer, `l` is a list of integers obtained from splitting the input string and converting each element to an integer, `p` is a list of counts of each unique element in `l`. After all iterations of the loop, if the maximum value in `p` is greater than or equal to `k`, the output will be `k - 1`. Otherwise, the output will be `n`.
    #
    #In simpler terms, after all iterations of the loop have finished, the variable `t` will reflect the total number of test cases, `i` will be equal to `t`, and the final outputs will depend on whether the maximum count of any unique element in the list `l` is greater than or equal to `k`. If it is, the output will be `k - 1`; otherwise, the output will be the total number of elements in the list `l`.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `t` (number of test cases), a list of integers `c` with length `n`, and an integer `k`. For each test case, it counts the occurrences of each unique element in the list `c` and determines if the maximum count of any unique element is greater than or equal to `k`. If true, it prints `k - 1`; otherwise, it prints the length of the list `c`.

