#State of the program right berfore the function call: The input consists of multiple test cases. For each test case, it starts with an integer n (2 ≤ n ≤ 2 · 10^5) representing the length of the array a. The next line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^6), which are the elements of the array a. The following line contains an integer q (1 ≤ q ≤ 2 · 10^5), representing the number of queries. Each of the next q lines contains two integers l and r (1 ≤ l < r ≤ n) representing the boundaries of the query. The sum of n across all test cases does not exceed 2 · 10^5, and the sum of q across all test cases does not exceed 2 · 10^5.
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
        
    #State: - `N` remains the same as the initial length of the array `a`.
    #- `i` will be `N` after the loop finishes.
    #- `s` will be the index of the last element in `nums` that was different from the previous element.
    #- `num` will be `nums[N]`, which is `-1` because `-1` is appended to `nums`.
    #- `arr` will contain tuples representing the segments of `nums`.
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
        
    #State: N remains the same as the initial length of the array `a`; `i` will be `N` after the loop finishes; `s` will be the first element of the tuple at index `min(eli, LA)` in `arr` from the last iteration; `e` will be the second element of the tuple at index `min(eli, LA)` in `arr` from the last iteration; `num` will be `nums[N]`, which is `-1`; `arr` will contain tuples representing the segments of `nums`; `LA` will be `len(arr) - 1`.
#Overall this is what the function does:The function `func_1` processes multiple test cases. For each test case, it reads an array of integers and a series of queries. Each query specifies a range within the array. The function then determines and prints a specific pair of indices for each query based on the segments of identical numbers in the array. If no valid pair can be found, it prints `-1 -1`.

