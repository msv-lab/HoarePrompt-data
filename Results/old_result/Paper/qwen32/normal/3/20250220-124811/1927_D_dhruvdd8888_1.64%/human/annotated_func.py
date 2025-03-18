#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (2 ≤ n ≤ 2 ⋅ 10^5) representing the length of the array a. The next line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^6) which are the elements of the array a. The following line contains an integer q (1 ≤ q ≤ 2 ⋅ 10^5) representing the number of queries. Each of the next q lines contains two integers l and r (1 ≤ l < r ≤ n) representing the boundaries of the query. The sum of the values of n across all test cases does not exceed 2 ⋅ 10^5, and the sum of the values of q across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: i is N, s is the last index where a change in nums occurred or N, num is nums[N], arr contains tuples representing contiguous segments of equal elements in nums.
    LA = len(arr) - 1
    if (ppp == 23) :
        print(nums)
        #This is printed: nums (where nums is the list of elements as defined by the initial state)
    #State: `i` is N, `s` is the last index where a change in `nums` occurred or N, `num` is `nums[N]`, `arr` contains tuples representing contiguous segments of equal elements in `nums`, and `LA` is `len(arr) - 1`. If `ppp` is 23, then the state of the variables remains unchanged. Otherwise, the state of the variables also remains unchanged as there is no else part.
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
        
    #State: `i` is N, `s` is the first element of `arr[min(eli, LA)]`, `num` is `nums[N]`, `arr` contains tuples representing contiguous segments of equal elements in `nums`, `LA` is `len(arr) - 1`.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an array of integers and a set of queries. For each query, it determines and prints a pair of indices representing a subarray that meets specific conditions related to the queried range. The function does not return a value explicitly; instead, it outputs results directly.

