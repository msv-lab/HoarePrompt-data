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
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `N` is an integer read from the input; `i` is `N`; `num` is `-1`; `arr` is a list of tuples representing segments of consecutive identical numbers in `nums`.
    LA = len(arr) - 1
    if (ppp == 23) :
        print(nums)
        #This is printed: nums (where nums is an undefined or uninitialized list of integers)
    #State: `t` is an integer such that 1 <= t <= 10^4; `N` is an integer read from the input; `i` is `N`; `num` is `-1`; `arr` is a list of tuples representing segments of consecutive identical numbers in `nums`; `LA` is `len(arr) - 1`. If `ppp` is equal to 23, then `ppp` remains equal to 23. Otherwise, there is no change to the variables.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `N` is an integer read from the input; `i` is `N`; `num` is `-1`; `arr` is a list of tuples representing segments of consecutive identical numbers in `nums`; `LA` is `len(arr) - 1`; `ppp` remains 23 if it equals 23, otherwise no change.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers and a series of queries. For each query, it identifies and prints a segment of the list that meets specific conditions related to the positions of the query's start and end indices.

