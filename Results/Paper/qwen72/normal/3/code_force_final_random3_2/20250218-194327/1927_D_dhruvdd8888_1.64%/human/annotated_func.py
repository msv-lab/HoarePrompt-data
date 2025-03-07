#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), n is an integer (2 ≤ n ≤ 2·10^5), a is a list of n integers (1 ≤ a_i ≤ 10^6), q is an integer (1 ≤ q ≤ 2·10^5), and for each query, l and r are integers (1 ≤ l < r ≤ n). The sum of n across all test cases does not exceed 2·10^5, and the sum of q across all test cases does not exceed 2·10^5.
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
        
    #State: `N` is the integer value read from `sys.stdin.readline`, `nums` is a list of integers with `-1` appended, `s` is `N`, `e` is 0, `num` is the last integer in the list `nums` (which is `-1`), `arr` is a list of tuples where each tuple `(start, end, value)` represents the start and end indices of a contiguous segment of `nums` that had the same value, and the value itself.
    LA = len(arr) - 1
    if (ppp == 23) :
        print(nums)
        #This is printed: [1, 2, 3, -1]
    #State: *`N` is the integer value read from `sys.stdin.readline`, `nums` is a list of integers with `-1` appended, `s` is `N`, `e` is 0, `num` is `-1`, `arr` is a list of tuples where each tuple `(start, end, value)` represents the start and end indices of a contiguous segment of `nums` that had the same value, and the value itself, `LA` is `len(arr) - 1`. If `ppp` is 23, the variables retain their values as described in the precondition.
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
        
    #State: The loop has executed `int(input())` times. For each iteration, `l` and `r` were updated with new integers provided by the user input. If `tc` was greater than 5, the loop printed `l` and `r` for each iteration where `ppp` was 23 and continued to the next iteration. Otherwise, `s` and `e` were assigned the first and second elements of the tuple at the index `min(eli, LA)` in the list `arr`. If `s` was greater than `l`, the loop printed `s - 1` and `s` unless `s` was 1, in which case it printed `-1, -1`. If `e` was greater than or equal to `r`, the loop printed `-1, -1`. If `e` was less than `r` and `e` was less than `N`, the loop printed `s` and `e + 1`. If `e` was greater than or equal to `N`, the loop printed `-1, -1`. The values of `N`, `nums`, `arr`, `LA`, and `ppp` remain unchanged.
#Overall this is what the function does:The function reads an integer `N` and a list of `N` integers `nums` from the standard input. It then processes the list to identify contiguous segments of the same value and stores these segments in a list of tuples `arr`, where each tuple contains the start index, end index, and the value of the segment. The function appends a `-1` to the end of `nums` to handle edge cases. It then reads an integer `q` indicating the number of queries, and for each query, it reads two integers `l` and `r` representing a range of indices in `nums`. For each query, the function checks if the range intersects with any of the identified segments and prints the indices of the segment boundaries that are closest to but outside the query range. If the query range does not intersect with any valid segment, it prints `-1, -1`. The function does not return any value; it only prints the results of the queries.

