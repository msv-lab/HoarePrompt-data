#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and b is a list of n integers where each integer b_i satisfies 1 ≤ b_i ≤ 4 ⋅ 10^5.
def func():
    input = sys.stdin.readline
    n = int(input())
    seq = sorted(((int(x) - i, int(x)) for i, x in enumerate(input().split())),
    key=lambda x: x[0])
    d = dict()
    ans = 0
    ansb = 0
    for (g, val) in seq:
        try:
            d[abs(g)] += val
        except:
            d[abs(g)] = val
        
        ans = max(ans, d[abs(g)])
        
        ansb = max(val, ansb)
        
    #State of the program after the  for loop has been executed: `n` is the initial integer value, `b` is the initial list of integers, `input` is an alias for `sys.stdin.readline`, `seq` is the initial sorted list of tuples, `d` is a dictionary where each key is the absolute value of the first element of the tuples in `seq` and the value is the cumulative sum of the corresponding `val` values, `ans` is the maximum value found in `d`, `ansb` is the maximum value of `val` encountered during the loop.
    if (ans == 0) :
        ans = ansb
    #State of the program after the if block has been executed: *`n` is the initial integer value, `b` is the initial list of integers, `input` is an alias for `sys.stdin.readline`, `seq` is the initial sorted list of tuples, `d` is a dictionary where each key is the absolute value of the first element of the tuples in `seq` and the value is the cumulative sum of the corresponding `val` values, `ansb` is the maximum value of `val` encountered during the loop. If `ans` is 0, `ans` is updated to the maximum value of `val` encountered during the loop. Otherwise, `ans` remains unchanged.
    print(ans)
#Overall this is what the function does:The function reads a positive integer `n` (1 ≤ n ≤ 2 ⋅ 10^5) and a list `b` of `n` integers (1 ≤ b_i ≤ 4 ⋅ 10^5) from standard input. It then processes these inputs to compute the maximum cumulative value associated with the absolute difference between the elements of `b` and their indices. Specifically, it creates a dictionary `d` where each key is the absolute difference (`|b_i - i|`) and the value is the cumulative sum of the corresponding `b_i` values. The function outputs the maximum value found in this dictionary. If no cumulative value is found (i.e., `ans` is 0), it outputs the maximum individual value from the list `b`. The final state of the program includes the original `n`, the original list `b`, the dictionary `d`, and the computed maximum value `ans`.

