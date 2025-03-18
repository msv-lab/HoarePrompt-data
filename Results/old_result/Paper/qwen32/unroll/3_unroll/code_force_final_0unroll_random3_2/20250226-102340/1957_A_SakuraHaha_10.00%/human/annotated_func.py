#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 100) representing the number of test cases. For each test case, there is an integer n (1 ≤ n ≤ 100) indicating the number of sticks available, followed by a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 100) representing the lengths of the sticks.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: The output state consists of the integer t (1 ≤ t ≤ 100) representing the number of test cases. For each test case, the integer n (1 ≤ n ≤ 100) indicating the number of sticks available, and the list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 100) representing the lengths of the sticks remain unchanged. The variable `ans` is still 0. The variable `cnt` is now a dictionary where each key is a unique length from the list `a`, and the corresponding value is the count of how many times that length appears in the list.
    for x in cnt.values():
        ans += x // 4
        
    #State: t, n, a_1, a_2, ..., a_n, ans, cnt
    print(ans)
    #This is printed: ans (where ans is the value determined by the program's logic prior to the print statement)
#Overall this is what the function does:The function reads the number of test cases and for each test case, it reads the number of sticks and their lengths. It then calculates and prints the maximum number of squares that can be formed using the sticks, where each square requires four sticks of the same length.

