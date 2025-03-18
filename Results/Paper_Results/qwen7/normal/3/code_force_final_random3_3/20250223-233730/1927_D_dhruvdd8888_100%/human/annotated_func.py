#State of the program right berfore the function call: t is a positive integer; n is an integer such that 2 <= n <= 2 * 10^5; a is a list of n integers where each integer is in the range [1, 10^6]; q is an integer such that 1 <= q <= 2 * 10^5; each query is represented by two integers l and r such that 1 <= l < r <= n.
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
        
    #State: Output State: `t` is a positive integer, `N` is an input integer, `n` is an integer such that 2 <= n <= 2 * 10^5, `a` is a list of n integers where each integer is in the range [1, 10^6], `q` is an integer such that 1 <= q <= 2 * 10^5, `nums` is a list of integers obtained from the input split and converted to integers with an additional element -1 appended to it, `s` is `N + 1`, `e` is 0, `num` is the value of `nums[N]`, `arr` is a list containing up to `N` tuples, each of the form `(1 + i, i, num_i)` where `num_i` is the value of `nums[i]` if `nums[i]` is not equal to `num`, and `i` ranges from 2 to `N`.
    #
    #This means that after all iterations of the loop, the variable `s` will be set to `N + 1` because the loop increments `s` on every iteration until it reaches `N`. The variable `num` will be the last element of `nums`, which is `nums[N]`. The list `arr` will contain all the positions where the elements in `nums` change, starting from index 2 up to `N`, capturing the transitions where `nums[i]` is different from `nums[i-1]`.
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
        
    #State: All iterations of the loop have been executed. The variable `n` remains a positive integer as initially inputted. The variable `s` is the first element of the tuple at the index found by `bisect_left(arr, (l, 0, 0))` in `arr`, and `e` is the third element of the same tuple. The variable `eli` is the index found by `bisect_left(arr, (l, 0, 0))`. The variables `l` and `r` are updated to the values of the integers inputted via `input().split()` and converted to integers using `map(int)` at each iteration.
#Overall this is what the function does:The function processes a list of integers `nums` and handles a series of queries. It identifies the positions where the elements in `nums` change and then, for each query defined by indices `l` and `r`, determines if the subarray from `l` to `r-1` contains any changes. If the subarray contains a change, it outputs the start and end indices of the first change within the subarray. If no change is found or the subarray is invalid, it outputs `-1 -1`. The function does not return any value but prints the results of each query.

