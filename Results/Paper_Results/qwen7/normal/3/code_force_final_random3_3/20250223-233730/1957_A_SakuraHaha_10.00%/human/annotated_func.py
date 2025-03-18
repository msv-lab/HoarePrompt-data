#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 1 ≤ n ≤ 100, and the following list contains n integers a_1, a_2, \ldots, a_n such that 1 ≤ a_i ≤ 100.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: Output State: `ans` is 0, `t` is an integer such that 1 ≤ t ≤ 100, `n` is an integer such that 1 ≤ n ≤ 100, `a` is an empty list, `cnt` is a dictionary with multiple key-value pairs where each key is an element from the original list `a` and each value is the count of occurrences of that element in the original list `a`.
    #
    #This final state occurs because the loop iterates over each element in the list `a`, updating the `cnt` dictionary to keep track of how many times each element appears. After all elements have been processed, the list `a` becomes empty, and `cnt` contains the counts of each unique element from the original list.
    for x in cnt.values():
        ans += x // 4
        
    #State: `ans` is the sum of `x // 4` for all values `x` in `cnt`, `t` is an integer such that 1 ≤ t ≤ 100, `n` is an integer such that 1 ≤ n ≤ 100, `a` is an empty list, `cnt` is a dictionary with the counts of each unique element from the original list `a`.
    print(ans)
    #This is printed: 0
#Overall this is what the function does:The function processes a list of integers provided by the user, counting the occurrences of each unique integer. It then calculates the sum of one-fourth of the count for each unique integer and prints the result. The function does not return any value but modifies the internal state by processing the input list and using a dictionary to store counts.

