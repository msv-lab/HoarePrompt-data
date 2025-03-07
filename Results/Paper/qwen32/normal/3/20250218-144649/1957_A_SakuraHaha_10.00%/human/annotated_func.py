#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 100) representing the number of test cases. For each test case, there is an integer n (1 ≤ n ≤ 100) representing the number of sticks available, followed by a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 100) representing the lengths of the sticks.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: `t` is an integer (1 ≤ `t` ≤ 100), `n` is an integer (1 ≤ `n` ≤ 100) and `n` must equal the length of `a`, `a` is a list of `n` integers representing the lengths of the sticks (with `n` ≥ 1), `ans` is 0, `cnt` is a dictionary where each key is a unique length from the list `a` and its value is the count of how many times that length appears in `a`.
    for x in cnt.values():
        ans += x // 4
        
    #State: ans is the sum of integer divisions of each unique stick length count by 4, t, n, a, and cnt remain unchanged.
    print(ans)
    #This is printed: ans (where ans is the sum of integer divisions of each unique stick length count by 4)
#Overall this is what the function does:The function reads the number of test cases and for each test case, it reads the number of sticks and their lengths. It then calculates and prints the total number of sets of four sticks that can be formed from each test case, where all sticks in a set have the same length.

