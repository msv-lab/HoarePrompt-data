#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each test case consists of an integer n such that 2 <= n <= 2 * 10^5, followed by a list a of n integers where each element a_i satisfies 1 <= a_i <= 10^6. Each test case also includes an integer q such that 1 <= q <= 2 * 10^5, followed by q queries, each query being a pair of integers (l, r) such that 1 <= l < r <= n. The sum of all n across all test cases does not exceed 2 * 10^5, and the sum of all q across all test cases does not exceed 2 * 10^5.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `N` is the first integer read from the input; `nums` is a list of integers where `nums[0]` is `n` and `nums[1:-1]` is the list `a` of `n` integers, and `nums[-1]` is `-1`; `num` is `final_num`; `s` is `final_s`; `e` is 0; `arr` is a list of tuples representing sequences of identical numbers in `nums`.
    LA = len(arr) - 1
    if (ppp == 23) :
        print(nums)
        #This is printed: [n, a1, a2, ..., an, -1] (where n is the first element of nums, a1, a2, ..., an are the elements of the list a, and -1 is the last element of nums)
    #State: `t` is an integer such that 1 <= t <= 10^4; `N` is the first integer read from the input; `nums` is a list of integers where `nums[0]` is `n` and `nums[1:-1]` is the list `a` of `n` integers, and `nums[-1]` is `-1`; `num` is `final_num`; `s` is `final_s`; `e` is 0; `arr` is a list of tuples representing sequences of identical numbers in `nums`; `LA` is `len(arr) - 1`. If `ppp` is equal to 23, then `ppp` remains equal to 23. Otherwise, the state of the variables remains unchanged.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `N` is the first integer read from the input; `nums` is a list of integers where `nums[0]` is `n` and `nums[1:-1]` is the list `a` of `n` integers, and `nums[-1]` is `-1`; `num` is `final_num`; `s` is `final_s`; `e` is 0; `arr` is a list of tuples representing sequences of identical numbers in `nums`; `LA` is `len(arr) - 1`; If `ppp` is equal to 23, then `ppp` remains equal to 23. Otherwise, the state of the variables remains unchanged. The loop has finished executing all `t` iterations, and the state of all variables outside the loop body remains as described.`
#Overall this is what the function does:The function `func_1` reads multiple test cases from standard input. For each test case, it reads a list of integers and a series of queries. Each query specifies a range within the list, and the function outputs a pair of indices based on the sequence of identical numbers within that range. The function does not return a value explicitly but prints the results of each query.

