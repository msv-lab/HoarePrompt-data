#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4; n is an integer such that 2 <= n <= 2 * 10^5; a is a list of n integers where each element is an integer between 1 and 10^6 inclusive; q is an integer such that 1 <= q <= 2 * 10^5; each query is represented by two integers l and r such that 1 <= l < r <= n.
def func_1():
    input = sys.stdin.readline
    N = int(input())
    nums = list(map(int, input().split()))
    s = 0
    e = 0
    num = nums[0]
    arr = []
    nums.append(-1)
    for i in range(N + 1):
        if nums[i] != num:
            arr.append((1 + s, i, num))
            s = i
        
        num = nums[i]
        
    #State: Output State: `s` is 0, `t` is an integer such that 1 <= t <= 10^4, `n` remains an integer such that 2 <= n <= 2 * 10^5, `a` remains a list of n integers where each element is an integer between 1 and 10^6 inclusive, `q` remains an integer such that 1 <= q <= 2 * 10^5, `arr` is a list of tuples, `N` remains an integer input from stdin, `nums` is a list of integers obtained from input split and mapped to integers, `e` is 0, `num` is the last element of `nums`.
    LA = len(arr) - 1
    for _ in range(int(input())):
        l, r = tuple(map(int, input().split()))
        
        eli = bisect_left(arr, (l, 0, 0))
        
        s, e, _ = arr[min(eli, LA)]
        
        if s > l:
            if s == 1 or s > r:
                print(-1, -1)
            else:
                print(s - 1, s)
        elif e >= r:
            print(-1, -1)
        elif e < N or e < l:
            print(s, e + 1)
        else:
            print(-1, -1)
        
    #State: The output state will consist of a series of pairs of integers (-1, -1) or (s, e+1), depending on the conditions inside the loop. Each pair represents the result of processing one input line given by the user, where each line provides two integers l and r. The actual values of s and e will vary based on the contents of the arr list and the positions determined by bisect_left function.
#Overall this is what the function does:The function processes a predefined set of variables: an integer `t` within the range 1 to 10^4, an integer `n` within the range 2 to 2 * 10^5, a list `a` of `n` integers where each element is between 1 and 10^6 inclusive, and an integer `q` within the range 1 to 2 * 10^5. Each query is represented by two integers `l` and `r` such that 1 <= l < r <= n. The function constructs an array `arr` that records changes in the elements of `nums`. It then handles `q` queries, each defined by `l` and `r`, to determine the start (`s`) and end (`e`) indices of a subarray within `a` that meets certain conditions. For each query, it outputs either a pair of indices `(s, e+1)` or `(-1, -1)` based on whether the subarray from `l` to `r-1` meets specific criteria.

