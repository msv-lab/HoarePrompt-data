#State of the program right berfore the function call: vp, vd, t, f, and c are integers where 1 ≤ vp, vd ≤ 100, 1 ≤ t, f ≤ 10, and 1 ≤ c ≤ 1000. vp represents the speed of the princess, vd represents the speed of the dragon, t is the time after which the dragon discovers the escape, f is the time the dragon spends fixing the treasury, and c is the distance from the cave to the king's castle.
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
        
    #State of the program after the loop has been executed: `vp` is an integer value entered by the user and must be less than or equal to `c`; `pl` is the final value of `pl` after all iterations; `dl` is the final value of `dl` after all iterations; `t` is the final value of `t` after all iterations; `count` is the final value of `count` after all iterations.
    print(count)
#Overall this is what the function does:The function accepts five integer parameters `vp`, `vd`, `t`, `f`, and `c`, representing the speed of the princess, the speed of the dragon, the time after which the dragon discovers the escape, the time the dragon spends fixing the treasury, and the distance from the cave to the king's castle, respectively. The function calculates whether the princess can escape to the castle without being caught by the dragon. If the princess can escape, the function prints the number of times the dragon catches up to her before she escapes. If she cannot escape, the function prints 0.

