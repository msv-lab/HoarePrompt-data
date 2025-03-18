#State of the program right berfore the function call: cnt_1, cnt_2, cnt_3, and cnt_4 are non-negative integers such that 0 <= cnt_i <= 10^9 for i in {1, 2, 3, 4}.
def func():
    cnt1, cnt2, cnt3, cnt4 = map(int, [input() for _ in range(4)])
    if (cnt3 > cnt1) :
        print(0)
    else :
        print(1)
    #State of the program after the if-else block has been executed: *`cnt_1`, `cnt_2`, `cnt_3`, and `cnt_4` are non-negative integers. If `cnt3` is greater than `cnt1`, the function proceeds with that condition. Otherwise, if `cnt3` is less than or equal to `cnt1`, the printed value is 1.
#Overall this is what the function does:The function accepts four non-negative integers `cnt1`, `cnt2`, `cnt3`, and `cnt4` via user input. It checks if `cnt3` is greater than `cnt1` and prints `0` if it is; otherwise, it prints `1`. The function does not return any value but only prints output based on the condition. The functionality does not handle any potential errors related to input types or invalid inputs.

