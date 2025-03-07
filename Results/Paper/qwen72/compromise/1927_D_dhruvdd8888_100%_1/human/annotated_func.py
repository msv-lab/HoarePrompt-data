#State of the program right berfore the function call: The function `func_1` is expected to read input from stdin and process multiple test cases. Each test case includes an array `a` of integers and a series of queries. The array `a` has a length `n` (2 ≤ n ≤ 2 · 10^5), and each element `a_i` is an integer (1 ≤ a_i ≤ 10^6). The number of queries `q` for each test case is a non-negative integer (1 ≤ q ≤ 2 · 10^5). Each query is defined by two integers `l` and `r` (1 ≤ l < r ≤ n). The sum of `n` and `q` across all test cases does not exceed 2 · 10^5.
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
        
    #State: `nums` remains unchanged, `N` remains unchanged, `num` is the last element of `nums` (which is `-1`), `s` is the index of the last element of `nums` (which is `N`), `e` remains 0, `arr` contains tuples representing the start and end indices of each segment of consecutive identical numbers in `nums`, excluding the last `-1`.
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
        
    #State: The values of `nums`, `N`, `num`, `s`, `e`, `arr`, and `LA` remain unchanged. The loop prints a series of tuples or pairs of `-1, -1` based on the input ranges and the conditions within the loop.
#Overall this is what the function does:The function `func_1` reads multiple test cases from standard input. Each test case includes an array `a` of integers and a series of queries. For each query defined by two integers `l` and `r`, the function processes the array to find and print a pair of indices representing the boundaries of a segment of consecutive identical numbers that intersects with the range `[l, r]`. If no such segment exists, it prints `(-1, -1)`. After processing all queries, the function leaves the input array `nums` and other internal variables unchanged.

