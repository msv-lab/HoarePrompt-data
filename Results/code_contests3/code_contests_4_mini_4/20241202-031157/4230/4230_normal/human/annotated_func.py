#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 200,000, and the sequence of opened doors is a list of integers where each integer is either 0 (for left exit) or 1 (for right exit), guaranteeing at least one 0 and one 1 in the list.
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = map(int, raw_input().split())
    ans = 0
    for i in range(n - 2, -1, -1):
        if c[i] != c[i + 1]:
            ans = i + 1
            break
        
    #State of the program after the  for loop has been executed: `n` is at least 2, `c` is a map object containing integers from raw_input split into a list, `ans` is the index of the last occurrence of a change in value between consecutive elements in `c`, or 0 if no change occurs.
    print(ans)
#Overall this is what the function does:The function accepts an integer `n` and a list `c` of integers (0s and 1s) representing exits. It returns the index of the last change in exit type in the list, or 0 if no change occurs.

