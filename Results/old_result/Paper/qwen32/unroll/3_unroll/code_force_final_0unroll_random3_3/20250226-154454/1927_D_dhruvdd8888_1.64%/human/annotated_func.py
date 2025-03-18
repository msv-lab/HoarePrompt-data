#State of the program right berfore the function call: There are t test cases (1 \le t \le 10^4). For each test case, there is an integer n (2 \le n \le 2 \cdot 10^5) representing the length of the array a. The array a consists of n integers a_1, a_2, \dots, a_n where each a_i satisfies 1 \le a_i \le 10^6. There are q queries (1 \le q \le 2 \cdot 10^5) for each test case, and each query is defined by two integers l and r (1 \le l < r \le n) representing the boundaries of the query. The sum of n across all test cases does not exceed 2 \cdot 10^5, and the sum of q across all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: `arr` is `[(1, 2, 2), (3, 4, 3)]`, `s` is `4`, `num` is `-1`.
    LA = len(arr) - 1
    if (ppp == 23) :
        print(nums)
        #This is printed: NameError: name 'nums' is not defined
    #State: `arr` is `[(1, 2, 2), (3, 4, 3)]`, `s` is `4`, `num` is `-1`, `LA` is `1`. If `ppp` is `23`, then `ppp` remains `23`. Otherwise, the state of the variables remains unchanged.
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
        
    #State: arr is [(1, 2, 2), (3, 4, 3)], s is 4, num is -1, LA is 1, ppp is 23.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an array of integers and a series of queries. For each query, which specifies a range within the array, the function determines and prints a specific pair of indices based on the values in the array within that range. The function does not return a value; instead, it outputs results directly.

