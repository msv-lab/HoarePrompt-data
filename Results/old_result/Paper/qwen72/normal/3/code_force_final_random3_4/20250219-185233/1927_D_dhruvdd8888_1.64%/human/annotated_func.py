#State of the program right berfore the function call: The function `func_1` is expected to read input from stdin and write output to stdout. The input consists of multiple test cases, where each test case starts with an integer n (2 ≤ n ≤ 2·10^5) representing the length of the array a, followed by n integers (1 ≤ a_i ≤ 10^6) representing the elements of the array a. The next line contains an integer q (1 ≤ q ≤ 2·10^5) representing the number of queries. Each of the following q lines contains two integers l and r (1 ≤ l < r ≤ n) representing the boundaries of the query. The sum of n and q across all test cases does not exceed 2·10^5.
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
        
    #State: `N` is the input integer, `i` is `N`, `s` is the index of the last occurrence of the last unique number in `nums` before `-1`, `e` is 0, `num` is the last integer in the list `nums` (which is `-1`), `arr` is a list of tuples where each tuple represents the start and end indices of a segment in `nums` and the value of the segment, and `nums` is a list of integers read from the next line of input with `-1` appended to it.
    LA = len(arr) - 1
    if (ppp == 23) :
        print(nums)
        #This is printed: [list of integers read from the next line of input, followed by -1]
    #State: *`N` is the input integer, `i` is `N`, `s` is the index of the last occurrence of the last unique number in `nums` before `-1`, `e` is 0, `num` is the last integer in the list `nums` (which is `-1`), `arr` is a list of tuples where each tuple represents the start and end indices of a segment in `nums` and the value of the segment, `LA` is `len(arr) - 1`, and `nums` is a list of integers read from the next line of input with `-1` appended to it. If `ppp` is 23, the program retains all these conditions.
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
        
    #State: The input integer for the loop is 0 (indicating the loop has completed all iterations), `l` and `r` are the last set of integers provided by the user, `s` and `e` are the first and second elements of the tuple at the index `min(eli, LA)` in the list `arr`, `eli` is the index where the tuple `(l, 0, 0)` would be inserted in the list `arr` to maintain sorted order. If `tc > 5`, the loop has continued to the next iteration for all iterations where this condition was true. If `ppp` is 23, the loop has printed `l` and `r` for all iterations where `tc > 5` and `ppp` is 23. The values of `s` and `e` have been updated based on the conditions within the loop for each iteration.
#Overall this is what the function does:The function `func_1` reads multiple test cases from standard input. Each test case consists of an array `a` of integers and a series of queries. For each query, the function determines and prints a pair of indices that represent the boundaries of a segment in `a` or prints `(-1, -1)` if no such segment exists. The function processes each query independently and writes the results to standard output. After processing all queries, the function terminates.

