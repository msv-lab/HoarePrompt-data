#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 100) representing the number of test cases. For each test case, the input contains an integer n (1 ≤ n ≤ 100) representing the number of sticks, followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 100) representing the lengths of the sticks.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: `t` is an integer (1 ≤ t ≤ 100), `n` is an integer (1 ≤ n ≤ 100), `a` is a list of `n` integers representing the lengths of the sticks, `ans` is 0, `cnt` is a dictionary where each key is a unique length from the list `a` and the corresponding value is the count of how many times that length appears in `a`.
    for x in cnt.values():
        ans += x // 4
        
    #State: `t` is an integer (1 ≤ t ≤ 100), `n` is an integer (1 ≤ n ≤ 100), `a` is a list of `n` integers representing the lengths of the sticks, `ans` is the sum of the integer divisions of the counts of each unique stick length by 4, `cnt` is a dictionary where each key is a unique length from the list `a` and the corresponding value is the count of how many times that length appears in `a`.
    print(ans)
    #This is printed: ans (where ans is the sum of the integer divisions of the counts of each unique stick length in the list `a` by 4)
#Overall this is what the function does:The function reads the number of sticks and their lengths for a single test case, counts how many sets of four sticks of the same length can be formed, and prints the total number of such sets.

