#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 200000, and the sequence of opened doors is a list of n integers where each integer is either 0 (for left exit) or 1 (for right exit).
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = map(int, raw_input().split())
    ans = 0
    for i in range(n - 2, -1, -1):
        if c[i] != c[i + 1]:
            ans = i + 1
            break
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 200000; `ans` is either 0 or the index of the last position checked plus one, depending on the values in `c`.
    print(ans)
#Overall this is what the function does:The function accepts an integer `n` and a list of integers `c` (where each integer is either 0 or 1), and it prints the index of the last door where the value differs from the next one, or 0 if all doors are the same. It does not return specific exit status strings as suggested by the annotations.

