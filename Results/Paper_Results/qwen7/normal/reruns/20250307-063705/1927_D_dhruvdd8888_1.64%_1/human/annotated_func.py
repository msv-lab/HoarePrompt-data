#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4; n is an integer such that 2 <= n <= 2 * 10^5; a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^6; q is an integer such that 1 <= q <= 2 * 10^5; each query is represented by two integers l and r such that 1 <= l < r <= n.
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
        
    #State: Output State: The array `arr` will contain pairs of indices and values from the list `nums` where each pair represents a segment of consecutive identical numbers in `nums`. Specifically, each pair in `arr` will have the form `(start_index, end_index, value)`, indicating that the value `value` starts at index `start_index` and ends at index `end_index - 1`. The variable `num` will be equal to the last element of `nums` after the loop completes. The variable `s` will be equal to `N`, and `e` will be equal to `N + 1` since the loop iterates from `0` to `N`, and `s` is updated to `i` at each iteration where `nums[i]` changes. The variable `i` will be equal to `N` after the loop completes.
    #
    #In summary, `arr` will contain segments of consecutive identical numbers from `nums`, `num` will be the last element of `nums`, and `s` and `e` will both be `N + 1`.
    LA = len(arr) - 1
    if (ppp == 23) :
        print(nums)
        #This is printed: [num, ...] where num is the last element of nums and the rest of the elements form segments of consecutive identical numbers
    #State: Postcondition: `arr` will contain segments of consecutive identical numbers from `nums`, `num` will be the last element of `nums`, and `s` and `e` will both be `N + 1`; `LA` is equal to `len(arr) - 1`. The value of `ppp` remains unchanged as 23.
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
        
    #State: Output State: After the loop executes all iterations, `eli` is the index of the first element in `arr` that is greater than or equal to `(l, 0, 0)`, `l` is the first integer input, `r` is the second integer input, `s` and `e` are updated to the start and end indices of the segment in `arr` that `eli` points to. If `s > l`, `s` and `e` are updated to the start and end indices of the segment. Otherwise, if `e >= r`, `s` and `e` are updated to the start and end indices of the segment. Otherwise, if `e < r`, `s` and `e` are updated accordingly. The value of `ppp` remains unchanged as 23, and `LA` is equal to `len(arr) - 1`.
    #
    #This final state reflects the outcome after processing all inputs within the loop, where `s` and `e` are correctly set based on the conditions provided in the loop body, and no further changes are made to the variables outside the loop's scope.
#Overall this is what the function does:The function processes a list of integers `nums` and handles a series of queries. It first identifies segments of consecutive identical numbers in `nums` and stores them in `arr`. For each query defined by `l` and `r`, it determines the segment in `arr` that corresponds to the range `[l, r)` and outputs specific values based on the segment's start and end indices. If the queried segment is not fully contained within any identified segment, it returns `-1 -1`. The function does not modify the original list `nums` and relies on the variables `ppp` and `tc` for conditional checks but does not change their values.

