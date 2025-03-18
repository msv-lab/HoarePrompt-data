#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n is an integer where 2 ≤ n ≤ 2·10^5, a is a list of integers where 1 ≤ a_i ≤ 10^6, q is an integer where 1 ≤ q ≤ 2·10^5, and each query is a pair of integers l and r where 1 ≤ l < r ≤ n. The sum of n across all test cases does not exceed 2·10^5, and the sum of q across all test cases does not exceed 2·10^5.
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
        
    #State: `N` is the same integer value as the input, `nums` is the same list of integers read from `sys.stdin` with `-1` appended to it, `s` is the index of the last element in `nums`, `e` is 0, `num` is the last element in `nums` (which is `-1`), `arr` is a list of tuples where each tuple represents the start and end indices of a segment in `nums` that contains the same integer, and the integer itself.
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
        
    #State: The values of `l`, `r`, `s`, `e`, `num`, and `LA` remain unchanged. The loop iterates `N` times, and for each iteration, it reads a pair of integers `(l, r)` from the input, processes them according to the conditions in the loop, and prints a pair of integers or `(-1, -1)` based on those conditions. The list `arr` and the variable `N` are not modified by the loop.
#Overall this is what the function does:The function reads an integer `N` and a list of integers `nums` from the standard input. It processes `nums` to identify segments of consecutive identical integers and stores these segments in a list `arr`, where each segment is represented as a tuple `(start_index, end_index, value)`. The function then reads a series of queries, each consisting of a pair of integers `(l, r)`, and for each query, it prints a pair of integers representing the indices of the first and last occurrence of a value within the segment `[l, r]` of `nums`. If no such segment exists, it prints `(-1, -1)`. The function does not return any value; it only prints the results of the queries.

