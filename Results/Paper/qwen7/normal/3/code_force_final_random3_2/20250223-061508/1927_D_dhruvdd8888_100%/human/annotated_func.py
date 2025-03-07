#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5; a is a list of n integers such that 1 ≤ a_i ≤ 10^6; q is an integer such that 1 ≤ q ≤ 2 \cdot 10^5; each query is represented by two integers l and r such that 1 ≤ l < r ≤ n.
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
        
    #State: Output State: The loop will execute exactly `N + 1` times, where `N` is the integer input from stdin. After all iterations, the variable `i` will be `N`, `s` will be equal to `N`, and `arr` will contain tuples of the form `(1 + s, j, num)` for each index `j` from `0` to `N` inclusive, where `num` is the value of `nums[j]`. The value of `num` will be the last element of `nums` since the loop continues until `i` reaches `N` and appends the final tuple with `i` being `N`.
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
        
    #State: i is N, s is N, e is N, arr contains tuples of the form (1 + N, j, nums[j]) for each index j from 0 to N inclusive, nums is a list with at least N + 1 elements, l and r are integers from the input split, eli is the updated index of the leftmost insertion point of the tuple (l, 0, 0) in the sorted list arr, and _ is the loop counter which is N.
#Overall this is what the function does:The function processes a list of integers `nums` and handles a series of queries. For each query defined by indices `l` and `r`, it determines and prints a pair of indices based on the segments of `nums` identified during the initial pass through the list. If no valid segment is found, it prints `-1 -1`. The function does not return any value but modifies and uses predefined global variables `t`, `n`, `a`, and `q`.

