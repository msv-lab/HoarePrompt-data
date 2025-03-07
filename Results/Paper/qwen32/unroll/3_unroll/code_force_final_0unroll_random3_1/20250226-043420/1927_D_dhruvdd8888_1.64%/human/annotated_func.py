#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 2 <= n <= 2 * 10^5, a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^6, q is an integer such that 1 <= q <= 2 * 10^5, and for each query, l and r are integers such that 1 <= l < r <= n. The sum of all n across all test cases does not exceed 2 * 10^5, and the sum of all q across all test cases does not exceed 2 * 10^5.
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
        
    #State: `arr` contains tuples representing segments of consecutive identical numbers in `nums`, `s` is the index of the last change in the sequence, `e` is 0, `num` is -1, and `i` is `N`.
    LA = len(arr) - 1
    if (ppp == 23) :
        print(nums)
        #This is printed: - We cannot provide the exact numerical values of `nums` because they are not specified in the initial state.
        #    - Therefore, we describe the output in terms of the variable `nums`.
        #
        #Output:
    #State: `arr` contains tuples representing segments of consecutive identical numbers in `nums`, `s` is the index of the last change in the sequence, `e` is 0, `num` is -1, `i` is `N`, `LA` is `len(arr) - 1`. If `ppp` equals 23, then the conditions remain the same as described. Otherwise, the conditions remain unchanged as there is no else part.
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
        
    #State: arr contains tuples representing segments of consecutive identical numbers in nums, s is the index of the last change in the sequence, e is 0, num is -1, i is N, LA is len(arr) - 1.
#Overall this is what the function does:The function processes a list of integers and handles a series of queries. For each query, it determines a specific segment in the list and outputs the indices of a sub-segment based on certain conditions. The function does not return a value but prints the results of each query directly.

