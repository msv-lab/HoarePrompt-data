#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n is an integer where 2 ≤ n ≤ 2·10^5, a is a list of integers where 1 ≤ a_i ≤ 10^6, q is an integer where 1 ≤ q ≤ 2·10^5, and each query (l, r) is a pair of integers where 1 ≤ l < r ≤ n. The sum of n across all test cases does not exceed 2·10^5, and the sum of q across all test cases does not exceed 2·10^5.
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
        
    #State: `N` is an integer value obtained from the input, `nums` is a list of integers obtained from the input with `-1` appended to the end, `s` is `N`, `e` is 0, `num` is `-1`, and `arr` is a list of tuples where each tuple represents a segment of the `nums` list that contains the same value. Each tuple is in the form `(start_index + 1, end_index, value)` where `start_index` is the index of the first occurrence of the value in the segment, and `end_index` is the index of the last occurrence of the value in the segment before a different value appears.
    LA = len(arr) - 1
    if (ppp == 23) :
        print(nums)
        #This is printed: [input integers, -1] (where the input integers are the integers provided in the input list, and -1 is appended to the end of the list)
    #State: *`N` is an integer value obtained from the input, `nums` is a list of integers obtained from the input with `-1` appended to the end, `s` is `N`, `e` is 0, `num` is `-1`, `arr` is a list of tuples where each tuple represents a segment of the `nums` list that contains the same value, `LA` is `len(arr) - 1`. If `ppp` is 23, the postcondition remains unchanged.
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
        
    #State: The values of `N`, `nums`, `num`, and `arr` remain unchanged. `s` and `e` are the first and second elements of the tuple at the index `min(eli, LA)` in `arr`, respectively, for the last iteration. `LA` remains `len(arr) - 1`. `l` and `r` are the last integers obtained from the input. If `tc` > 5, the loop may have skipped some iterations due to the `continue` statement. If `ppp` is 23, it remains unchanged.
#Overall this is what the function does:The function reads an integer `N` and a list of integers `nums` from the standard input. It then processes a series of queries, each consisting of two integers `l` and `r`. For each query, the function determines the segment of `nums` that contains the same value and intersects with the range `[l, r]`. If such a segment exists, it returns the start and end indices of the segment. If no such segment exists, it returns `(-1, -1)`. The function does not return a list of results; instead, it prints the results directly to the standard output for each query. The state of the program after the function concludes includes the unchanged values of `N`, `nums`, and `arr`, and the last processed values of `l` and `r`.

