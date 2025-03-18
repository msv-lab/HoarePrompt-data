#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 100) representing the number of test cases. For each test case, there is an integer n (1 ≤ n ≤ 100) representing the number of sticks, followed by a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 100) representing the lengths of the sticks.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: `t` is the number of test cases, `n` is the number of sticks, `a` is the list of stick lengths, `ans` is 0, `cnt` is a dictionary with each key being a unique stick length and the value being the count of that length in `a`.
    for x in cnt.values():
        ans += x // 4
        
    #State: t is the number of test cases, n is the number of sticks, a is the list of stick lengths, ans is the sum of x // 4 for all x in cnt.values(), cnt is a dictionary with each key being a unique stick length and the value being the count of that length in a.
    print(ans)
    #This is printed: ans (where ans is the sum of the integer division of the count of each unique stick length by 4)
#Overall this is what the function does:The function reads an integer `n` representing the number of sticks and a list of `n` integers representing the lengths of the sticks. It calculates and prints the total number of sets of four sticks that can be formed from the list, where each set consists of sticks of the same length.

