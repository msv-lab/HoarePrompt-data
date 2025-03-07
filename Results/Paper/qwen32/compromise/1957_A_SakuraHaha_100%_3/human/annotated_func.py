#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 100) representing the number of test cases. For each test case, there is an integer n (1 ≤ n ≤ 100) representing the number of sticks, followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 100) representing the lengths of the sticks.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: The output state consists of the integer `t` representing the number of test cases, the integer `n` representing the number of sticks, the list `a` of integers representing the lengths of the sticks, `ans` which remains 0, and `cnt` which is a dictionary where each key is a unique stick length from the list `a` and each value is the count of how many times that stick length appears in the list `a`.
    for x in cnt.values():
        ans += x // 3
        
    #State: Output State:
    print(ans)
    #This is printed: ans (where ans is the value of the variable `ans`)
#Overall this is what the function does:The function reads the number of sticks and their lengths for a single test case, counts how many times each stick length appears, and calculates how many complete sets of three sticks of the same length can be formed. It then prints the number of such sets.

