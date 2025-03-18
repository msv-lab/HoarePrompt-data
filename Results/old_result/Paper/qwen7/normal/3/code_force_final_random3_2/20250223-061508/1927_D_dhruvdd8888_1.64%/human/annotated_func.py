#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4; n is an integer such that 2 <= n <= 2 * 10^5; a is a list of n integers such that 1 <= a_i <= 10^6; q is an integer such that 1 <= q <= 2 * 10^5; for each query, l and r are integers such that 1 <= l < r <= n.
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
        
    #State: Output State: `N` is a non-negative integer, `i` is `N + 1`, `s` is `N`, `num` is equal to `nums[N]`, and `arr` contains tuples starting from (2, 0, `nums[0]`), followed by (1, 1, `nums[0]`), and ending with a tuple (1 + `s`, `N`, `nums[N]`).
    #
    #This means that after all iterations of the loop, `i` will be `N + 1` because the loop runs from `0` to `N`. The variable `s` will be `N` since it is updated to `i` whenever `nums[i]` changes. The variable `num` will be set to the last element of the list `nums`, which is `nums[N]`. The list `arr` will contain all the transitions where `num` changes, starting from the first element and ending with the last transition before the loop exits.
    LA = len(arr) - 1
    if (ppp == 23) :
        print(nums)
        #This is printed: [nums[0], nums[1], ..., nums[N]]
    #State: `N` is a non-negative integer, `i` is `N + 1`, `s` is `N`, `num` is equal to `nums[N]`, `arr` contains tuples starting from (2, 0, `nums[0]`), followed by (1, 1, `nums[0]`), and ending with a tuple (1 + `s`, `N`, `nums[N]`), and `LA` is the length of `arr` minus one. If `ppp` equals 23, no changes are made to the variables.
    for _ in range(int(input())):
        l, r = tuple(map(int, input().split()))
        
        if tc > 5:
            if ppp == 23:
                print(l, r)
            continue
        
        eli = bisect_left(arr, (l, 0, 0))
        
        s, e, _ = arr[min(eli, LA)]
        
        if s > l:
            if s == 1:
                print(-1, -1)
            else:
                print(s - 1, s)
        elif e >= r:
            print(-1, -1)
        elif e < N:
            print(s, e + 1)
        else:
            print(-1, -1)
        
    #State: Output State: `N` is a non-negative integer, `i` is `N + 1`, `s`, `e`, and `_` are assigned the values from the tuple at the minimum index between `eli` and `LA`, and `tc` is greater than 5 after all iterations. The variable `l` and `r` will contain the last values obtained from the input split and converted to integers. The variable `eli` will hold the final index found by `bisect_left(arr, (l, 0, 0))`. The state of the other variables (`arr`, `LA`, `ppp`) remains unchanged as they are not modified within the loop.
#Overall this is what the function does:The function processes an input list of integers and handles a series of queries. It first identifies transitions in the list where the value changes and stores these transitions in a list. Then, for each query, it finds the relevant transition and determines the range within the query bounds. Based on this range, it outputs either the start and end indices or -1, -1 if the query cannot be fully satisfied.

