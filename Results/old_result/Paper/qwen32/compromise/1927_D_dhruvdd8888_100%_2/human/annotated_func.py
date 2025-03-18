#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 2 <= n <= 2 * 10^5, a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^6, q is an integer such that 1 <= q <= 2 * 10^5, and for each query, there are two integers l and r such that 1 <= l < r <= n. The sum of all n across all test cases does not exceed 2 * 10^5, and the sum of all q across all test cases does not exceed 2 * 10^5.
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
        
    #State: t is an integer such that 1 <= t <= 10^4; N is an integer assigned the value of the first test case from the input; nums is a list of integers obtained from the input with an additional element -1 appended to it; s is 5; e is 0; num is -1; arr is [(1, 2, 2), (3, 5, 3)].
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `N` is an integer assigned the value of the first test case from the input; `nums` is a list of integers obtained from the input with an additional element -1 appended to it; `s` is 5; `e` is 0; `num` is -1; `arr` is [(1, 2, 2), (3, 5, 3)]; `LA` is 1.
#Overall this is what the function does:The function processes a list of integers for each test case and handles a series of queries. For each query, it determines and prints a pair of indices based on specific conditions related to the values in the list. If no valid pair can be found, it prints `-1 -1`.

