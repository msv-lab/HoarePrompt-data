#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 1 ≤ n ≤ 100, and the second line of each test case contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 100.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 100, `n` is an input integer such that 1 ≤ n ≤ 100, `a` is a list of integers obtained from splitting the input string and converting each element to an integer, `ans` is 0, `cnt` is a dictionary where each key is an integer from the list `a` and its value is the count of how many times that integer appears in `a`.
    for x in cnt.values():
        ans += x // 4
        
    #State: Output State: `ans` is an integer calculated by summing up the values in the dictionary `cnt` and then performing integer division by 4 for each value.
    print(ans)
    #This is printed: 9
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and a list of \( n \) integers \( a_1, a_2, \ldots, a_n \). It counts the occurrences of each integer in the list and calculates the sum of these counts divided by 4. Finally, it prints the result of this calculation for each test case.

