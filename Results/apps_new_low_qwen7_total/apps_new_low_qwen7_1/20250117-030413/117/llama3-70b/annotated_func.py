#State of the program right berfore the function call: l_1, r_1, l_2, r_2, and k are integers such that 1 ≤ l_1, r_1, l_2, r_2, k ≤ 10^18, l_1 ≤ r_1, and l_2 ≤ r_2.
def func():
    l1, r1, l2, r2, k = map(int, input().split())

start = max(l1, l2)

end = min(r1, r2)
    if (start <= k <= end) :
        end -= 1
    #State of the program after the if block has been executed: `start` is the maximum of `l1` and `l2`, `end` is `min(r1, r2) - 1`, `k` is input value 5, `l1` is input value 1, `r1` is input value 2, `l2` is input value 3, `r2` is input value 4.
    minutes_together = max(0, end - start + 1)

print(minutes_together)
#Overall this is what the function does:The function `func` accepts five integers `l_1`, `r_1`, `l_2`, `r_2`, and `k` as input. It calculates the maximum overlap between two time intervals `[l_1, r_1]` and `[l_2, r_2]` and returns the length of this overlap, which is the number of minutes both intervals are together. If `k` falls within this overlap, the function adjusts the end of the overlap by decrementing it by 1. If the calculated overlap length is negative or zero, the function returns 0.

