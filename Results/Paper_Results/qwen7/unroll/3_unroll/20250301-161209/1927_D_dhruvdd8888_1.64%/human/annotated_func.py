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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is an integer such that 2 ≤ n ≤ 2 \cdot 10^5; `a` is a list of n integers such that 1 ≤ a_i ≤ 10^6; `q` is an integer such that 1 ≤ q ≤ 2 \cdot 10^5; each query is represented by two integers `l` and `r` such that 1 ≤ l < r ≤ n; `nums` is a list of integers with its last element being -1; `s` is equal to `N`; `e` is 0; `num` is the last element of `nums`; `arr` is a list of tuples where each tuple contains three elements: the first element is an integer starting from 1 plus the value of `s`, the second element is an integer `i` ranging from 0 to `N`, and the third element is the integer `num` which is consistent throughout each tuple.
    LA = len(arr) - 1
    if (ppp == 23) :
        print(nums)
        #This is printed: [-1]
    #State: `LA` is equal to `len(arr) - 1`, `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is an integer such that 2 ≤ n ≤ 2 \cdot 10^5; `a` is a list of n integers such that 1 ≤ a_i ≤ 10^6; `q` is an integer such that 1 ≤ q ≤ 2 \cdot 10^5; each query is represented by two integers `l` and `r` such that 1 ≤ l < r ≤ n; `nums` is a list of integers with its last element being -1; `s` is equal to `N`; `e` is 0; `num` is the last element of `nums`; `arr` is a list of tuples where each tuple contains three elements: the first element is an integer starting from 1 plus the value of `s`, the second element is an integer `i` ranging from 0 to `N`, and the third element is the integer `num` which is consistent throughout each tuple. The value of `ppp` is 23.
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
        
    #State: The output state depends on the inputs provided during the execution of the loop. For each query (l, r), the output could be one of the following: (-1, -1), (s, e+1) where s and e are determined based on the binary search result. Since the exact inputs are not given, the output cannot be precisely calculated. However, it will consist of multiple lines, each containing either two numbers or two -1s, corresponding to the results of each query.
#Overall this is what the function does:The function processes a list of integers `nums` and handles a series of queries defined by pairs of indices `l` and `r`. For each query, it determines a subarray within `nums` and outputs either the start and end indices of a segment within this subarray or (-1, -1) if no valid segment is found. The function does not return any value but prints the results for each query.

