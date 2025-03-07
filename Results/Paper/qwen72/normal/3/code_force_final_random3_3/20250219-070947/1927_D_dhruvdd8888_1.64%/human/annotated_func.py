#State of the program right berfore the function call: The function should accept multiple test cases. Each test case includes an array a of n integers (2 ≤ n ≤ 2 · 10^5) where each element a_i is an integer (1 ≤ a_i ≤ 10^6), and q queries (1 ≤ q ≤ 2 · 10^5). Each query is defined by two integers l and r (1 ≤ l < r ≤ n). The sum of n across all test cases does not exceed 2 · 10^5, and the sum of q across all test cases does not exceed 2 · 10^5.
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
        
    #State: `N` is greater than or equal to 0, `i` is `N`, `nums` is a list of integers read from the input, split by spaces, with `-1` appended to the end, `num` is the last integer in the list `nums` (which is `-1`), `s` is the index of the last element in `nums` that is not `-1`, and `arr` contains tuples of the form `(1 + s, i, num)` for each segment of consecutive identical numbers in `nums` before the `-1`.
    LA = len(arr) - 1
    if (ppp == 23) :
        print(nums)
        #This is printed: [1, 2, 2, 3, 3, 3, -1]
    #State: *`N` is greater than or equal to 0, `i` is `N`, `nums` is a list of integers read from the input, split by spaces, with `-1` appended to the end, `num` is `-1`, `s` is the index of the last element in `nums` that is not `-1`, `arr` contains tuples of the form `(1 + s, i, num)` for each segment of consecutive identical numbers in `nums` before the `-1`, `LA` is the length of `arr` minus 1. If `ppp` is 23, the postcondition remains unchanged.
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
        
    #State: The values of `N`, `i`, `nums`, `num`, `s`, and `arr` remain unchanged. `LA` remains the length of `arr` minus 1. The loop iterates a number of times specified by the input integer. For each iteration, `l` and `r` are updated with new input integers. `eli` is updated to the index of the first element in `arr` that is greater than or equal to `(l, 0, 0)`. `s` and `e` are updated to the first and second elements of the tuple at index `min(eli, LA)` in `arr`. If `tc` is greater than 5 and `ppp` is 23, the loop prints `l` and `r`. If `s` is greater than `l`, the loop prints `s - 1` and `s` if `s` is not 1, otherwise it prints `-1, -1`. If `s` is less than or equal to `l` and `e` is greater than or equal to `r`, the loop prints `-1, -1`. If `s` is less than or equal to `l` and `e` is less than `r` and `e` is less than `N`, the loop prints `s` and `e + 1`. If `s` is less than or equal to `l` and `e` is less than `r` and `e` is not less than `N`, the loop prints `-1, -1`.
#Overall this is what the function does:The function reads an integer `N` and a list of integers `nums` from the standard input, processes the list to identify segments of consecutive identical numbers, and then handles a series of queries. Each query consists of two integers `l` and `r`. For each query, the function outputs a pair of indices indicating the boundaries of the segment that contains `l` and `r` or `-1, -1` if the segment does not exist or the conditions are not met. The function does not return any value; it only prints the results of the queries.

