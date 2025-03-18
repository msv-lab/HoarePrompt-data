#State of the program right berfore the function call: The function should take three parameters: a list of integers `a`, an integer `n` representing the length of the list `a`, and a list of queries `q` where each query is a list of two integers `[l, r]` such that 1 ≤ l < r ≤ n. The list `a` contains integers in the range 1 ≤ a_i ≤ 10^6, and the number of queries `q` is such that 1 ≤ q ≤ 2 · 10^5. The function should handle multiple test cases, where the number of test cases `t` is 1 ≤ t ≤ 10^4, and the sum of the values of `n` and `q` across all test cases does not exceed 2 · 10^5.
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
        
    #State: The variable `N` remains unchanged. The list `nums` remains unchanged. The variable `s` is equal to `N`. The variable `e` remains unchanged. The variable `num` is equal to `-1`. The list `arr` contains tuples of the form `(1 + start_index, end_index, value)` for each contiguous segment of the same value in `nums`, where `start_index` is the starting index of the segment, `end_index` is the index just after the segment, and `value` is the value of the segment.
    LA = len(arr) - 1
    if (ppp == 23) :
        print(nums)
        #This is printed: [the elements of the list `nums` in their original order]
    #State: *The variable `N` remains unchanged. The list `nums` remains unchanged. The variable `s` is equal to `N`. The variable `e` remains unchanged. The variable `num` is equal to `-1`. The list `arr` contains tuples of the form `(1 + start_index, end_index, value)` for each contiguous segment of the same value in `nums`, where `start_index` is the starting index of the segment, `end_index` is the index just after the segment, and `value` is the value of the segment. The variable `LA` is equal to the length of `arr` minus 1. If `ppp` is equal to 23, then `ppp` remains equal to 23.
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
        
    #State: The variable `N` remains unchanged. The list `nums` remains unchanged. The variable `s` is equal to `N`. The variable `e` remains unchanged. The variable `num` is equal to `-1`. The list `arr` remains unchanged. The variable `LA` remains equal to the length of `arr` minus 1. If `ppp` is equal to 23, then `ppp` remains equal to 23.
#Overall this is what the function does:The function `func_1` processes a list of integers `nums` and a series of queries `q`. For each query `[l, r]`, it identifies the boundaries of the contiguous segments in `nums` that contain the same value and returns a pair of indices that represent the boundaries of the segment containing the queried range. If the queried range does not fit within any segment, it returns `(-1, -1)`. The function handles multiple test cases, where each test case includes a list `nums` and a set of queries `q`. The input list `nums` and the number of elements `N` remain unchanged throughout the function execution. The function does not return a sum of elements but rather the boundaries of segments.

