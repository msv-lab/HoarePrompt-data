#State of the program right berfore the function call: t is a positive integer; for each test case, n is an integer such that 2 <= n <= 2 * 10^5, the array a is a list of n integers where each integer is in the range [1, 10^6], and q is an integer such that 1 <= q <= 2 * 10^5. Each query is represented by two integers l and r such that 1 <= l < r <= n.
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
        
    #State: Output State: `t` is a positive integer, `n` is an integer such that 2 <= n <= 2 * 10^5, the array `a` remains unchanged, `q` is an integer such that 1 <= q <= 2 * 10^5, `nums` is a list of n integers where each integer is in the range [1, 10^6] with an additional element `-1` at the end, `s` is equal to `n`, `e` is 0, `num` is the last element of the list `nums`, `arr` is a list containing tuples of the form `(1 + s, i, num)` for each change in consecutive elements in `nums` except the last one.
    LA = len(arr) - 1
    if (ppp == 23) :
        print(nums)
        #This is printed: [1, 2, ..., n-1, n, -1]
    #State: `t` is a positive integer, `n` is an integer such that 2 <= n <= 2 * 10^5, the array `a` remains unchanged, `q` is an integer such that 1 <= q <= 2 * 10^5, `nums` is a list of n integers where each integer is in the range [1, 10^6] with an additional element `-1` at the end, `s` is equal to `n`, `e` is 0, `num` is the last element of the list `nums`, `arr` is a list containing tuples of the form `(1 + s, i, num)` for each change in consecutive elements in `nums` except the last one, `LA` is the length of `arr` minus 1. The value of `ppp` is 23.
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
        
    #State: The output state depends on the inputs provided during the loop's execution. Specifically, for each iteration, the values of `l` and `r` provided via `input()` will determine the output printed. If `tc` exceeds 5, the loop will print `l` and `r` and then skip further processing for that iteration. Otherwise, it will perform a binary search on the list `arr` and based on the results, it will either print `(-1, -1)` or a range defined by `s` and `e+1`. The final state includes all printed outputs from each iteration.
#Overall this is what the function does:The function processes a series of queries on a list of integers. It first identifies segments of consecutive identical numbers in the input list and stores their start and end indices along with the number itself. Then, for each query, it determines the segment within the identified segments that overlaps with the query range and prints the start and end indices of that segment. If no such segment exists, it prints `(-1, -1)`. The function does not return any value but prints the results directly.

