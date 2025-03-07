#State of the program right berfore the function call: The function should take three parameters: a list of integers `a`, an integer `n` representing the length of the list `a`, and a list of queries `q` where each query is a tuple of two integers `(l, r)` such that 1 <= l < r <= n. The list `a` should have a length of 2 to 2 * 10^5, and each element `a_i` should be an integer between 1 and 10^6. The number of queries `q` should be a non-negative integer such that 1 <= q <= 2 * 10^5.
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
        
    #State: The loop has completed all iterations, `i` is `N`, `num` is the last element of `nums` (which is `-1`), and `arr` contains tuples representing the ranges of consecutive elements in `nums` that are equal, each tuple in the form `(1 + s, i, num)` where `s` is the start index of the range and `i` is the end index of the range. `s` is the index of the last element in `nums` (which is `N`).
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
        
    #State: The loop has completed all iterations, `i` is `N`, `num` is `-1`, `arr` contains tuples representing the ranges of consecutive elements in `nums` that are equal, each tuple in the form `(1 + s, i, num)` where `s` is the start index of the range and `i` is the end index of the range. `s` is `N`, `LA` is `len(arr) - 1`. For each iteration, `l` and `r` are the integers from the input split, `eli` is the index where the tuple `(l, 0, 0)` would be inserted in `arr` to maintain sorted order, `s` and `e` are the first and second elements of the tuple at the index `min(eli, LA)` in `arr`. The conditions for the output remain consistent with the logic of the loop: if `s > l`, then `s` is either 1 or greater than `r`, or `s` is not equal to 1 and is less than or equal to `r`. If `s <= l`, then `e` is greater than or equal to `r`, or `e` is less than `r` and if `e` is less than `N` or less than `l`, the current value of `e` is less than `N` or less than `l`. If `e` is greater than or equal to `N`, then `e` is greater than or equal to `N` and greater than or equal to `l`.
#Overall this is what the function does:The function reads a list of integers and a series of queries from standard input. Each query consists of two integers `(l, r)` where `1 <= l < r <= n`. The function processes these queries to find and print pairs of indices `(x, y)` such that `x < y` and the elements at these indices are different. If no such pair exists within the query range, it prints `(-1, -1)`. The function does not return any value; it only prints the results of the queries.

