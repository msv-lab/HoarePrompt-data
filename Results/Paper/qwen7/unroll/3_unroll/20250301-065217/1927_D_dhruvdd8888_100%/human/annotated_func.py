#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5; a is a list of n integers such that 1 ≤ a_i ≤ 10^6; q is an integer such that 1 ≤ q ≤ 2 \cdot 10^5; each query is represented by two integers l and r such that 1 ≤ l < r ≤ n.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is an integer such that 2 ≤ n ≤ 2 \cdot 10^5; `a` is a list of n integers such that 1 ≤ a_i ≤ 10^6; `q` is an integer such that 1 ≤ q ≤ 2 \cdot 10^5; each query is represented by two integers `l` and `r` such that 1 ≤ l < r ≤ n; `nums` is a list of integers obtained from `map(int, input().split())` with an additional element `-1` appended to it; `s` is an integer representing the start index of segments where elements in `nums` are the same; `e` is an integer representing the end index of segments where elements in `nums` are the same; `num` is the current element being compared in `nums`; `arr` is a list of tuples, where each tuple contains three elements: the start index (`1 + s`), the end index (`i`), and the value of `num` for each segment of consecutive identical elements in `nums`.
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
        
    #State: Output State: The output state depends on the inputs provided during the loop iterations. For each iteration, the loop processes two integers `l` and `r` from the input, finds a segment in the array `arr` based on these values, and prints either a segment or `-1 -1` based on certain conditions. After all iterations, the output state will consist of a series of segments printed for each valid input pair `(l, r)`, or `-1 -1` if no valid segment is found.
#Overall this is what the function does:The function processes a list of integers `nums` and handles a series of queries. It first identifies segments of consecutive identical elements in `nums` and stores their start and end indices along with the value of the elements. Then, for each query defined by `l` and `r`, it determines whether a valid segment exists within the specified range and prints the start and end indices of that segment, or `-1 -1` if no valid segment is found.

