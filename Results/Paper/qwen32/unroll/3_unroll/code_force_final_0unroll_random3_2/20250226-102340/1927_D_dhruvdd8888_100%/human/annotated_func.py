#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 2 <= n <= 2 * 10^5, a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^6, q is an integer such that 1 <= q <= 2 * 10^5, and for each query, l and r are integers such that 1 <= l < r <= n. The sum of n across all test cases does not exceed 2 * 10^5, and the sum of q across all test cases does not exceed 2 * 10^5.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `N` is an integer read from input; `n` is an integer such that 2 <= n <= 2 * 10^5, `a` is a list of `n` integers where each integer `a_i` satisfies 1 <= `a_i` <= 10^6, `q` is an integer such that 1 <= `q` <= 2 * 10^5, and for each query, `l` and `r` are integers such that 1 <= `l` < `r` <= `n`. The sum of `n` across all test cases does not exceed 2 * 10^5, and the sum of `q` across all test cases does not exceed 2 * 10^5; `input` is `sys.stdin.readline`; `nums` is a list of integers read from input with an additional -1 appended to it; `s` is `N` (the last index of the `nums` list); `e` is 0; `num` is `-1` (the last element of the `nums` list); `arr` is a list of tuples representing segments of consecutive identical numbers in the `nums` list.
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
        
    #State: The output state after the loop executes all the iterations will be that the variables `l` and `r` will hold the values of the last query processed, and the variables `eli`, `s`, `e`, and the print outputs will reflect the result of the last query. The state of other variables such as `t`, `N`, `n`, `a`, `q`, `nums`, `s`, `e`, `num`, `arr`, and `LA` will remain unchanged from their last known states before the loop started processing the queries.
#Overall this is what the function does:The function reads an integer `N` and a list of `N` integers `nums`. It then processes a series of queries, each defined by two integers `l` and `r`. For each query, it determines and prints a pair of indices `(s, e + 1)` based on the segments of consecutive identical numbers in `nums`. If no valid segment is found, it prints `(-1, -1)`.

