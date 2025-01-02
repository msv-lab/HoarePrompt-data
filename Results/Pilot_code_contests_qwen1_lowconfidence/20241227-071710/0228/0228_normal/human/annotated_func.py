#State of the program right berfore the function call: vp, vd, t, f, and c are integers where 1 ≤ vp, vd ≤ 100, 1 ≤ t, f ≤ 10, and 1 ≤ c ≤ 1000.
def func():
    vp = int(raw_input())
    vd = int(raw_input())
    t_read = int(raw_input())
    f = int(raw_input())
    c = int(raw_input())
    pl = 0
    dl = 0
    t = 1
    count = 0
    while pl + vp <= c:
        pl += vp
        
        if t > t_read:
            dl += vd
            if dl >= pl and pl + vp <= c:
                count += 1
                dl = pl
                pl += (2 * (dl / vd) + f) * vp
        
        t += 1
        
    #State of the program after the loop has been executed: `vp` is an integer obtained from `int(raw_input())` and satisfies `0 <= vp <= c`; `pl` is updated to `pl + (2 * (pl / vd) + f) * vp` or unchanged; `c` remains unchanged; `t` is incremented by the number of iterations; `dl` is equal to `pl` if `dl >= pl` and `pl + vp <= c` is true, otherwise `dl` remains unchanged; `count` is incremented by 1 if the condition `dl >= pl and pl + vp <= c` is met, otherwise `count` remains unchanged.
    print(count)
#Overall this is what the function does:The function `func()` accepts five integer parameters `vp`, `vd`, `t`, `f`, and `c`. It reads `vp` and `vd` from user input, where `1 ≤ vp, vd ≤ 100`. The variable `t` is read as `t_read` and `1 ≤ t_read ≤ 10`. The parameters `f` and `c` are also read from user input, where `1 ≤ f, c ≤ 1000`. The function then iterates through a loop until `pl + vp > c`, updating `pl` and `dl` based on certain conditions. Inside the loop, `pl` is incremented by `vp`, and if `t > t_read`, `dl` is updated to `pl` and `pl` is further incremented by `(2 * (dl / vd) + f) * vp`. The loop increments `t` and `count` is incremented when `dl >= pl` and `pl + vp <= c` is true. After the loop, the function prints the value of `count`, which represents the number of times the condition `dl >= pl` and `pl + vp <= c` was met during the loop iterations. If any of the initial parameters are out of their specified ranges, the function will raise an error.

