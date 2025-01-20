#State of the program right berfore the function call: c, v_0, v_1, a, and l are integers such that 1 ≤ c ≤ 1000, 0 ≤ l < v_0 ≤ v_1 ≤ 1000, and 0 ≤ a ≤ 1000.
def func_1():
    c, v_0, v_1, a, l = map(int, input().split())

days = 0

pages_read = 0

current_speed = v_0
    while pages_read < c:
        days += 1
        
        if days == 1:
            pages_read += v_0
        else:
            pages_read += min(current_speed, v_1) - l
            current_speed += a
        
        current_speed = min(current_speed, v_1)
        
        if pages_read < 0:
            pages_read = 0
        
    #State of the program after the loop has been executed: `c` is an integer such that 1 ≤ c ≤ 1000, `v_0` is an integer such that 0 ≤ l < v_0 ≤ v_1 ≤ 1000, `v_1` is an integer such that 0 ≤ l < v_0 ≤ v_1 ≤ 1000, `a` is an integer such that 0 ≤ a ≤ 1000, `l` is an integer such that 0 ≤ l < v_0, `days` is the minimum number of days required to read `c` pages or more, `pages_read` is `c` or the exact value that makes the condition `pages_read < c` false, `current_speed` is `min(v_0 + (days-1)*a, v_1)`.
    print(days)
#Overall this is what the function does:The function `func_1` reads five integer inputs `c`, `v_0`, `v_1`, `a`, and `l` from the user, where `1 ≤ c ≤ 1000`, `0 ≤ l < v_0 ≤ v_1 ≤ 1000`, and `0 ≤ a ≤ 1000`. It calculates the minimum number of days required to read at least `c` pages, given the following conditions:
- On the first day, the reader reads `v_0` pages.
- On subsequent days, the reader reads `min(current_speed, v_1) - l` pages, where `current_speed` starts at `v_0` and increases by `a` each day, up to a maximum of `v_1`.
- If the number of pages read becomes negative, it is reset to 0.
- The function prints the total number of days required to reach or exceed `c` pages read.
- After the function concludes, the state of the program includes the original input values (`c`, `v_0`, `v_1`, `a`, `l`), the number of days (`days`), the total pages read (`pages_read`), and the final reading speed (`current_speed`).

