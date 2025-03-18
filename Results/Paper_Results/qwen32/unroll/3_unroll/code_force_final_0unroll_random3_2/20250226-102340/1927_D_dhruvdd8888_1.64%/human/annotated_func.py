#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (2 ≤ n ≤ 2 · 10^5) representing the length of the array a. This is followed by a line containing n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^6) representing the elements of the array a. Next is an integer q (1 ≤ q ≤ 2 · 10^5) representing the number of queries. Each of the next q lines contains two integers l and r (1 ≤ l < r ≤ n) representing the boundaries of the query. The sum of n across all test cases does not exceed 2 · 10^5, and the sum of q across all test cases does not exceed 2 · 10^5.
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
        
    #State: `N` is the first integer read from the input, `nums` is a list of integers representing the elements of the array `a` with an additional `-1` at the end, `s` is the last index where a new segment started, `e` is 0 (unchanged), `num` is `-1` (the last element in `nums`), `arr` is a list of tuples representing segments of consecutive identical numbers in `nums`.
    LA = len(arr) - 1
    if (ppp == 23) :
        print(nums)
        #This is printed: [elements of array a, -1] (where elements of array a are the integers that form the array a)
    #State: `N` is the first integer read from the input, `nums` is a list of integers representing the elements of the array `a` with an additional `-1` at the end, `s` is the last index where a new segment started, `e` is 0, `num` is `-1`, `arr` is a list of tuples representing segments of consecutive identical numbers in `nums`, `LA` is `len(arr) - 1`. If `ppp` equals 23, the state of all variables remains unchanged. Otherwise, the state of all variables remains unchanged as there is no else part.
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
        
    #State: N is the first integer read from the input, nums is a list of integers representing the elements of the array a with an additional -1 at the end, s is the last index where a new segment started, e is 0, num is -1, arr is a list of tuples representing segments of consecutive identical numbers in nums, LA is len(arr) - 1.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an array and a series of queries. For each query, it computes and prints a pair of indices based on the segments of consecutive identical numbers within the array. The function does not return a value explicitly but outputs results for each query.

