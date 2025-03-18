#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 1 ≤ n ≤ 100, and the second line of each test case contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 100.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: Output State: `ans` is 0, `t` is an integer such that 1 ≤ t ≤ 100, `n` is an integer such that 1 ≤ n ≤ 100, `a` is a list of integers obtained from splitting the input and converting each element to an integer, `cnt` is a dictionary where each key is an integer from the list `a` and its value is the count of how many times that integer appears in `a`.
    for x in cnt.values():
        ans += x // 4
        
    #State: Output State: `ans` is the sum of the counts of each integer in `a` divided by 4, `t` is an integer such that 1 ≤ t ≤ 100, `n` is an integer such that 1 ≤ n ≤ 100, `a` is a list of integers obtained from splitting the input and converting each element to an integer, `cnt` is a dictionary where each key is an integer from the list `a` and its value is the count of how many times that integer appears in `a`.
    print(ans)
    #This is printed: ans (where ans is the sum of the counts of each integer in list `a` divided by 4)
#Overall this is what the function does:The function processes a series of test cases, where each test case includes an integer `t` indicating the number of subsequent test cases, followed by `t` sets of data. Each set consists of an integer `n` and `n` integers `a_1, a_2, ..., a_n`. For each set, it counts the occurrences of each integer in the list `a`, then calculates the sum of these counts divided by 4, and finally prints this sum for each test case.

