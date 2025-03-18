#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 1 ≤ n ≤ 100, and the lengths of the sticks a_1, a_2, ..., a_n are integers such that 1 ≤ a_i ≤ 100.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: Output State: `ans` is 0, `t` is an integer such that 1 ≤ t ≤ 100, `n` is an input integer such that 1 ≤ n ≤ 100, `a` is an empty list, `cnt` is a dictionary containing counts of all unique elements from the original list `a` where each key is an element from `a` and its value is the count of how many times it appeared in `a`.
    #
    #This final state occurs because after all iterations of the loop, the list `a` will be empty since one element is processed in each iteration. The dictionary `cnt` will contain the counts of each unique element from the original list `a`, reflecting how many times each number appeared in the list.
    for x in cnt.values():
        ans += x // 4
        
    #State: Output State: `ans` is the sum of the floor division of each value in `cnt` by 4, `t` is an integer such that 1 ≤ t ≤ 100, `n` is an input integer such that 1 ≤ n ≤ 100, `a` is an empty list, `cnt` contains the count of each unique element from the original list `a`, where each key is an element from `a` and its value is the count of how many times it appeared in `a`.
    #
    #In this final state, after all iterations of the loop, `ans` accumulates the result of dividing each value in the `cnt` dictionary by 4 and summing these results. The list `a` remains empty as one element is processed in each iteration, and `cnt` reflects the counts of each unique element from the original list `a`.
    print(ans)
    #This is printed: ans (where ans is the sum of the floor division of each value in cnt by 4)
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it accepts an integer `t` (1 ≤ t ≤ 100) representing the number of test cases, followed by an integer `n` (1 ≤ n ≤ 100) representing the number of sticks, and a list of integers `a_1, a_2, ..., a_n` (1 ≤ a_i ≤ 100) representing the lengths of the sticks. It then counts the occurrences of each stick length, calculates the sum of the floor division of these counts by 4, and prints the result. After processing all test cases, the function returns nothing.

