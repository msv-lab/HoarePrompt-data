#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 100) — the number of test cases. For each test case, the first line contains a single integer n (1 ≤ n ≤ 100) — the number of sticks available. The second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 100) — the stick lengths.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: `ans` is 0. `cnt` is a dictionary where each key is a unique stick length from the list `a`, and each value is the count of that stick length in the list `a`.
    for x in cnt.values():
        ans += x // 4
        
    #State: `ans` is the sum of the integer divisions of each stick count in `cnt` by 4. `cnt` remains unchanged.
    print(ans)
    #This is printed: ans (where ans is the sum of the integer divisions of each stick count in cnt by 4)
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a number of sticks and their respective lengths. It calculates and prints the total number of complete sets of four sticks that can be formed from each test case based on the stick lengths provided.

