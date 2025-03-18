#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 100) representing the number of test cases. For each test case, the first line contains a single integer n (1 ≤ n ≤ 100) representing the number of sticks available. The second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 100) representing the lengths of the sticks.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: `t` is a single integer (1 ≤ t ≤ 100), `n` is a single integer (1 ≤ n ≤ 100), `a` is a list of integers representing the lengths of the sticks for the current test case, `ans` is 0, `cnt` is a dictionary where each key is a unique stick length from `a` and its value is the count of how many times that length appears in `a`.
    for x in cnt.values():
        ans += x // 3
        
    #State: `t` is a single integer (1 ≤ t ≤ 100), `n` is a single integer (1 ≤ n ≤ 100), `a` is a list of integers representing the lengths of the sticks for the current test case, `ans` is the sum of `x // 3` for all `x` in `cnt.values()`, `cnt` is a dictionary where each key is a unique stick length from `a` and its value is the count of how many times that length appears in `a`.
    print(ans)
    #This is printed: ans (where ans is the sum of x // 3 for all x in cnt.values(), and cnt is the dictionary of stick lengths and their counts)
#Overall this is what the function does:The function reads multiple test cases, where each test case consists of a number of sticks and their respective lengths. For each test case, it calculates how many sets of three sticks can be formed from the sticks of the same length and prints this count.

