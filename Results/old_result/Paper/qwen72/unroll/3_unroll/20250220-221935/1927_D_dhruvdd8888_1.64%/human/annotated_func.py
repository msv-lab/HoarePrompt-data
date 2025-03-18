#State of the program right berfore the function call: The function `func_1` is not defined with any parameters, but based on the problem description, it should take a list of integers `a` and a list of queries, where each query is a pair of integers `(l, r)`. The list `a` contains `n` integers (2 ≤ n ≤ 2 · 10^5), and each element `a_i` is an integer (1 ≤ a_i ≤ 10^6). The list of queries contains `q` queries (1 ≤ q ≤ 2 · 10^5), and each query `(l, r)` satisfies 1 ≤ l < r ≤ n. The function should be called multiple times for different test cases, where the number of test cases `t` is an integer (1 ≤ t ≤ 10^4).
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
        
    #State: `nums` is a list of integers obtained from the input with an additional `-1` appended at the end, `N` is an input integer, `s` is `N`, `e` is 0, `num` is `-1`, `arr` is a list of tuples where each tuple represents the start and end indices of a contiguous segment of the same integer in `nums`, along with the integer itself.
    LA = len(arr) - 1
    if (ppp == 23) :
        print(nums)
        #This is printed: [input_list, -1] (where input_list is the list of integers provided by the user, and `-1` is appended at the end)
    #State: *`nums` is a list of integers obtained from the input with an additional `-1` appended at the end, `N` is an input integer, `s` is `N`, `e` is 0, `num` is `-1`, `arr` is a list of tuples where each tuple represents the start and end indices of a contiguous segment of the same integer in `nums`, along with the integer itself, `LA` is `len(arr) - 1`. If `ppp` is 23, the program retains these conditions.
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
        
    #State: The variables `l`, `r`, `s`, `e`, and `num` will have their values changed within the loop, but their final values will depend on the input and the specific iterations. The variables `nums`, `N`, `arr`, `LA`, and `ppp` will remain unchanged.
#Overall this is what the function does:The function `func_1` reads from standard input and processes a series of test cases. For each test case, it takes a list of integers `nums` and a series of queries, where each query is a pair of integers `(l, r)`. The function identifies contiguous segments of the same integer in `nums` and stores these segments in a list `arr`, where each element is a tuple `(start, end, value)`. For each query `(l, r)`, the function determines if there is a valid segment boundary within the range `[l, r]` and prints the indices of the segment boundary. If no valid boundary exists, it prints `(-1, -1)`. The function does not return any value; it only prints the results to standard output. The final state of the program includes the list `nums` with an additional `-1` appended, the list `arr` containing the segment boundaries, and the variables `N`, `s`, `e`, `num`, `LA`, and `ppp` (if defined) retaining their final values.

