#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 2 <= n <= 2 * 10^5, a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^6, q is an integer such that 1 <= q <= 2 * 10^5, and for each query, l and r are integers such that 1 <= l < r <= n. The sum of all n across all test cases does not exceed 2 * 10^5, and the sum of all q across all test cases does not exceed 2 * 10^5.
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
        
    #State: - `t` is an integer such that 1 <= `t` <= 10^4.
    #- `N` is an integer read from input.
    #- `n` is an integer such that 2 <= `n` <= 2 * 10^5.
    #- `nums` is a list of `n + 1` integers where the first `n` integers are the original `nums` and the last integer is `-1`.
    #- `q` is an integer such that 1 <= `q` <= 2 * 10^5, and for each query, `l` and `r` are integers such that 1 <= `l` < `r` <= `n + 1`.
    #- `s` is the index of the last change in `nums` or `N` if the last element is different from the previous one.
    #- `e` is 0.
    #- `num` is `nums[N]`.
    #- `arr` contains tuples `(start_index, end_index, number)` representing segments of consecutive identical numbers in `nums`.
    #
    #Output State:
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
        
    #State: `t` is an integer such that 1 <= `t` <= 10^4; `N` is an integer read from input; `n` is an integer such that 2 <= `n` <= 2 * 10^5; `nums` is a list of `n + 1` integers where the first `n` integers are the original `nums` and the last integer is `-1`; `q` is 0 (since all queries have been processed); `s` is the start index of the segment in `arr` at the index `min(eli, LA)` from the last iteration; `e` is the end index of the segment in `arr` at the index `min(eli, LA)` from the last iteration; `num` is `nums[N]`; `arr` contains tuples `(start_index, end_index, number)` representing segments of consecutive identical numbers in `nums`; `LA` is `len(arr) - 1`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers and a series of queries. For each query, it determines and prints a specific pair of indices based on the segments of consecutive identical numbers within the list.

