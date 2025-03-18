#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 1 ≤ n ≤ 100, and the second line of each test case contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 100.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: Output State: `ans` is 0, `t` is an integer such that 1 ≤ t ≤ 100, `n` is an input integer such that 1 ≤ n ≤ 100, `a` is a list of integers, `cnt` is a dictionary where each key is an element from the list `a` and its value is the count of occurrences of that element in the list `a`.
    #
    #This final output state indicates that after all iterations of the loop have been executed, the dictionary `cnt` contains the count of each unique element in the list `a`. The variable `ans` remains 0 as it is not affected by the loop. The values of `t` and `n` also remain unchanged as they are not modified within the loop.
    for x in cnt.values():
        ans += x // 4
        
    #State: The dictionary `cnt` contains the count of each unique element in the list `a`, and the variable `ans` remains 0.
    print(ans)
    #This is printed: 0
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and a list of \( n \) integers. It counts the occurrences of each unique integer in the list and calculates the sum of the integer divisions of these counts by 4. The function then prints the total sum for each test case.

