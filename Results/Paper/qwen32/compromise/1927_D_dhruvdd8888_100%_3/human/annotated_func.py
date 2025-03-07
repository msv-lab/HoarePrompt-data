#State of the program right berfore the function call: The input consists of multiple test cases. For each test case, it starts with an integer n (2 ≤ n ≤ 2 ⋅ 10^5) representing the length of the array a. The next line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^6) representing the elements of the array a. The following line contains an integer q (1 ≤ q ≤ 2 ⋅ 10^5) representing the number of queries. The next q lines each contain two integers l and r (1 ≤ l < r ≤ n) representing the boundaries of each query. The sum of n across all test cases does not exceed 2 ⋅ 10^5, and the sum of q across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: N is the integer input representing the length of the array a; q and the query boundaries l and r remain unchanged; nums is a list of integers read from the input with an additional -1 appended at the end; s is the index of the start of the last segment that was not recorded; e is 0; num is nums[N]; arr is a list of tuples representing segments of identical numbers found in nums.
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
        
    #State: N is the integer input representing the length of the array a; q and the query boundaries l and r remain unchanged; nums is a list of integers read from the input with an additional -1 appended at the end; s is the index of the start of the last segment that was not recorded; e is 0; num is nums[N]; arr is a list of tuples representing segments of identical numbers found in nums; LA is the index of the last element in the list `arr`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an array and a set of queries. For each query, it determines and prints a pair of indices based on the segments of identical numbers within the array. Specifically, for each query defined by boundaries `l` and `r`, it identifies the segment of identical numbers within the specified range and returns the start and end indices of that segment, or `-1 -1` if no such segment exists.

