#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4; n is an integer such that 2 <= n <= 2 * 10^5; a is a list of n integers where each integer a_i is such that 1 <= a_i <= 10^6; q is an integer such that 1 <= q <= 2 * 10^5; each query is represented by two integers l and r such that 1 <= l < r <= n.
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
        
    #State: Output State: `i` is equal to `N`, `N` is a valid positive integer, `num` is equal to `nums[N]`, `s` is `N`, and `arr` contains tuples starting from `(1 + s, 0, num)` up to `(N + s, N, nums[N])`.
    #
    #This means that after all iterations of the loop, the variable `i` will be equal to `N`, indicating that the loop has completed its execution. The variable `num` will hold the value of `nums[N]` since it gets updated to `nums[i]` on each iteration. The variable `s` will also be equal to `N`, as it gets updated to `i` whenever `nums[i]` is different from `num`. The list `arr` will contain all the necessary segments defined by the conditions inside the loop, starting from the initial segment `(1 + s, 0, num)` up to the final segment `(N + s, N, nums[N])`.
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
        
    #State: Output State: All input values have been processed through the loop, meaning the loop has executed a number of times equal to the integer input provided at the start. The final state of the variables `s` and `e` will depend on the last set of inputs (`l` and `r`) and the state of the sorted list `arr`.
    #
    #After all iterations of the loop have finished, the following conditions apply:
    #- `input_value` is the last positive integer input provided.
    #- `l` and `r` are the last integers from the input split by space and converted to int.
    #- `eli` is the index of the leftmost insertion point of the tuple `(l, 0, 0)` in the sorted list `arr`.
    #- `s` is the first element of the tuple at the minimum index between `eli` and `LA`.
    #- `e` is the second element of the tuple at the minimum index between `eli` and `LA`.
    #
    #Based on the logic within the loop:
    #- If `s` equals 1 or `s` is greater than `r`, or if `e >= r`, then `s` and `e` remain unchanged.
    #- Otherwise, `s` and `e` are updated according to the else part of the loop.
    #
    #Thus, the final output state will reflect the result of the last iteration of the loop, with `s` and `e` being either unchanged or updated based on the conditions specified in the else part of the loop.
#Overall this is what the function does:The function processes a list of integers `nums` and handles a series of queries. It first identifies segments in `nums` where the elements are the same and stores these segments along with their starting indices. Then, for each query defined by indices `l` and `r`, it determines the segment within the specified range and outputs the start and end indices of that segment, or `-1 -1` if no valid segment is found.

