#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 1 ≤ n ≤ 100, and the following list contains n integers a_1, a_2, \ldots, a_n such that 1 ≤ a_i ≤ 100.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: Output State: The list `a` is a list of `n` integers each between 1 and 100. The dictionary `cnt` is a dictionary where each key is an integer from the list `a` and its value is the count of that integer in the list `a`, with each integer's count updated based on its occurrence in the list `a` after all iterations of the loop.
    #
    #In simpler terms, after all iterations of the loop, the dictionary `cnt` will contain the frequency of each integer present in the list `a`.
    for x in cnt.values():
        ans += x // 3
        
    #State: The dictionary `cnt` contains the frequency of each integer present in the list `a`, and the variable `ans` is the sum of each count in `cnt` divided by 3 after all iterations of the loop.
    print(ans)
    #This is printed: ans (where ans is the sum of the values in the dictionary cnt divided by 3)
#Overall this is what the function does:The function processes a list of integers provided as input and calculates the sum of the counts of each integer in the list, divided by 3. It then prints the result. The function does not accept any parameters and does not return a value, but rather prints the computed result directly.

