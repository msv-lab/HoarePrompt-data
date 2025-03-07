#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 2 · 10^5, a is a list of n integers where each element a_i satisfies 1 ≤ a_i ≤ 10^6, q is an integer such that 1 ≤ q ≤ 2 · 10^5, and for each query, l and r are integers such that 1 ≤ l < r ≤ n. The sum of n across all test cases does not exceed 2 · 10^5, and the sum of q across all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `N` is an integer read from the input; `nums` is a list of integers read from the input with an additional -1 appended to it; `s` is the starting index of the last segment; `num` is -1; `arr` contains tuples representing each contiguous segment of identical numbers in `nums`; `i` is N + 1.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4, N is an integer read from the input, nums is a list of integers read from the input with an additional -1 appended to it, s is the starting index of the segment at index min(eli, LA) (updated for the last iteration), num is -1, arr contains tuples representing each contiguous segment of identical numbers in nums, i is N + 1, LA is len(arr) - 1. The loop has executed t times, and the input value for the next iteration would be 0. The variables l, r, eli, and e are the values from the last iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads a list of integers and a series of queries. Each query specifies a range within the list, and the function returns a pair of indices or `-1 -1` based on the segments of identical numbers within that range.

