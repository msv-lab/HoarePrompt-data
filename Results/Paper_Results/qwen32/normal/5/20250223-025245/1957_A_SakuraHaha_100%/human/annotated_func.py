#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 1 <= n <= 100, and the list of stick lengths a_1, a_2, ..., a_n is a list of integers where each a_i satisfies 1 <= a_i <= 100.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: `t` is an integer such that 1 <= t <= 100; `n` is the integer input provided, where 1 <= `n` <= 100; `a` is a list of integers obtained from the input; `ans` is 0; `cnt` is a dictionary where the count of each unique integer in `a` is stored.
    for x in cnt.values():
        ans += x // 3
        
    #State: `t` is an integer such that 1 <= t <= 100, `n` is the integer input provided, where 1 <= `n` <= 100, `a` is a list of integers obtained from the input, `ans` is the sum of `x // 3` for all `x` in `cnt.values()`, `cnt` is a dictionary where the count of each unique integer in `a` is stored.
    print(ans)
    #This is printed: ans (where ans is the sum of x // 3 for all x in cnt.values())
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of `n` integers representing stick lengths. It calculates the total number of complete sets of three sticks that can be formed from the list, where each set consists of sticks of the same length, and prints this count.

