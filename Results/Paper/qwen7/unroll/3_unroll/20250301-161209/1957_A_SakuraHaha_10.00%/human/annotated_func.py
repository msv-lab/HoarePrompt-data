#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 1 ≤ n ≤ 100, and the lengths of the sticks a_1, a_2, ..., a_n are integers such that 1 ≤ a_i ≤ 100.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: Output State: `ans` is 0, `t` is an integer such that 1 ≤ t ≤ 100, `n` is an input integer, `a` is a list of integers obtained from splitting the input string and converting each element to an integer, `cnt` is a dictionary where each key is an integer from the list `a` and its value is the count of how many times that integer appears in `a`.
    for x in cnt.values():
        ans += x // 4
        
    #State: Output State: `ans` is the sum of the counts of each integer in `a` divided by 4.
    print(ans)
    #This is printed: ans (where ans is the sum of the counts of each integer in the list `a` divided by 4)
#Overall this is what the function does:The function processes multiple test cases, where each test case includes an integer `t` (1 ≤ t ≤ 100) representing the number of sticks, followed by `t` integers `n` (1 ≤ n ≤ 100) representing the number of sticks in the current test case, and then `n` integers `a_i` (1 ≤ a_i ≤ 100) representing the lengths of the sticks. For each test case, it calculates the sum of the counts of each unique stick length divided by 4 and prints this sum for each test case.

