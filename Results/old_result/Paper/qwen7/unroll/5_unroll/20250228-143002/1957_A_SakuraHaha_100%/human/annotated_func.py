#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 1 ≤ n ≤ 100, and the following list contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 100.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 100, `n` is an integer such that 1 ≤ n ≤ 100, `a` is a list of integers obtained from splitting the input string on spaces and converting each element to an integer, `ans` is 0, `cnt` is a dictionary where each key is an integer from the list `a` and its value is the count of how many times that integer appears in `a`.
    for x in cnt.values():
        ans += x // 3
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 100, `n` is an integer such that 1 ≤ n ≤ 100, `a` is a list of integers obtained from splitting the input string on spaces and converting each element to an integer, `ans` is the sum of counts of each integer in `a` divided by 3, `cnt` is a dictionary where each key is an integer from the list `a` and its value is the count of how many times that integer appears in `a`.
    print(ans)
    #This is printed: ans (where ans is the sum of counts of each integer in list `a` divided by 3)
#Overall this is what the function does:The function reads a list of integers from the user input, counts the occurrences of each integer, and then calculates the sum of these counts divided by 3. The final result is printed.

