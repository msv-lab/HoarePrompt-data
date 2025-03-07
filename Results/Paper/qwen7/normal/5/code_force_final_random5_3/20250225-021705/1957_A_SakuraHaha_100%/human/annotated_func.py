#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 1 ≤ n ≤ 100, and the lengths of the sticks a_1, a_2, ..., a_n are integers such that 1 ≤ a_i ≤ 100.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: Output State: `ans` is 0, `t` is an integer such that 1 ≤ t ≤ 100, `n` is an integer such that 1 ≤ n ≤ 100, `a` is an empty list, `cnt` is a dictionary where each key's value is incremented by 1 for every occurrence of that key in the original list `a`.
    #
    #Explanation: After the loop has executed all its iterations, the list `a` will be empty since one element is processed in each iteration. The dictionary `cnt` will contain the count of each unique integer present in the original list `a`, with each count incremented by 1 for every occurrence of that integer in the list.
    for x in cnt.values():
        ans += x // 3
        
    #State: `ans` is the sum of the floor division of each value in `cnt.values()` by 3, `t` is an integer such that \(1 \leq t \leq 100\), `n` is an integer such that \(1 \leq n \leq 100\), `a` is an empty list, `cnt` is a dictionary where each value represents the count of each unique integer in the original list `a` (each count incremented by 1 for every occurrence of that integer in the list).
    print(ans)
    #This is printed: ans (where ans is the sum of the floor division of each value in cnt.values() by 3)
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `t` (1 ≤ t ≤ 100), an integer `n` (1 ≤ n ≤ 100), and a list of integers `a_1, a_2, ..., a_n` (1 ≤ a_i ≤ 100). It counts the occurrences of each unique integer in the list `a` and calculates the sum of the floor division of each count by 3. Finally, it prints the calculated sum.

