#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 100) representing the number of sticks. This is followed by a line containing n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 100) representing the lengths of the sticks. The total number of test cases is given by the first integer t (1 ≤ t ≤ 100) in the input.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: `t` is the number of test cases (1 ≤ `t` ≤ 100), `n` is an integer (1 ≤ `n` ≤ 100), `a` is a list of `n` integers representing the lengths of the sticks (with `n` ≥ 1), `ans` is 0, `cnt` is a dictionary with each unique stick length as keys and their respective counts as values.
    for x in cnt.values():
        ans += x // 4
        
    #State: `t` is the number of test cases (1 ≤ `t` ≤ 100), `n` is an integer (1 ≤ `n` ≤ 100), `a` is a list of `n` integers representing the lengths of the sticks (with `n` ≥ 1), `ans` is the sum of `x // 4` for all `x` in `cnt.values()`, `cnt` is a dictionary with each unique stick length as keys and their respective counts as values.
    print(ans)
    #This is printed: ans (where ans is the sum of (count of each unique stick length) // 4 for all unique stick lengths in the list `a`)
#Overall this is what the function does:The function `func_1` reads multiple test cases, where each test case consists of an integer `n` and a list of `n` integers representing the lengths of sticks. It calculates how many sets of four sticks can be formed from each test case and prints the total number of such sets for all test cases.

