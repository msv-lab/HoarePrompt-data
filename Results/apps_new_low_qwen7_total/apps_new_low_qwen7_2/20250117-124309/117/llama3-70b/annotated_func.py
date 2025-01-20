#State of the program right berfore the function call: l_1, r_1, l_2, r_2, and k are non-negative integers such that 1 ≤ l_1, r_1, l_2, r_2, k ≤ 10^18, l_1 ≤ r_1, and l_2 ≤ r_2.
def func():
    l1, r1, l2, r2, k = map(int, input().split())

start = max(l1, l2)

end = min(r1, r2)
    if (start <= k <= end) :
        end -= 1
    #State of the program after the if block has been executed: *`l1` is the maximum of `l1` and `l2`, `r1` is unchanged, `l2` is unchanged, `r2` is unchanged, `k` is unchanged, `start` is the maximum of `l1` and `l2`, `end` is the minimum of `r1` and `r2` - 1, and if `start` <= `k` <= `end`, then the condition holds; otherwise, the condition does not change.
    minutes_together = max(0, end - start + 1)

print(minutes_together)
#Overall this is what the function does:The function accepts five non-negative integer parameters \( l_1 \), \( r_1 \), \( l_2 \), \( r_2 \), and \( k \). It first determines the maximum of \( l_1 \) and \( l_2 \) and assigns it to the variable `start`, and the minimum of \( r_1 \) and \( r_2 \) and assigns it to the variable `end`. If \( k \) falls within the range defined by `start` and `end` (inclusive), it subtracts 1 from `end`. Finally, it calculates the number of overlapping minutes between the intervals \([ \max(l_1, l_2), \min(r_1, r_2) - 1 ]\) and \([ \max(l_1, l_2), \min(r_1, r_2) - 1 ]\) and returns this value. If no overlap exists, it returns 0. Potential edge cases include when \( l_1 > r_1 \) or \( l_2 > r_2 \), in which case the function will set `start` and `end` to invalid values, leading to a non-overlapping interval and a return value of 0.

