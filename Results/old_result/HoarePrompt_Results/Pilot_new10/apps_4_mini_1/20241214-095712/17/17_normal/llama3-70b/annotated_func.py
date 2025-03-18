#State of the program right berfore the function call: cnt_1, cnt_2, cnt_3, and cnt_4 are non-negative integers such that 0 <= cnt_i <= 10^9 for i in {1, 2, 3, 4}.
def func():
    cnt1, cnt2, cnt3, cnt4 = map(int, [input() for _ in range(4)])
    if (cnt3 > cnt1) :
        print(0)
    else :
        print(1)
    #State of the program after the if-else block has been executed: *`cnt_1`, `cnt_2`, `cnt_3`, and `cnt_4` are integers. If `cnt_3` is greater than `cnt_1`, the output 0 is printed. Otherwise, if `cnt_3` is less than or equal to `cnt_1`, the output 1 is printed.
#Overall this is what the function does:The function accepts four non-negative integers as input, cnt1, cnt2, cnt3, and cnt4. It compares cnt3 with cnt1 and prints 0 if cnt3 is greater than cnt1, and 1 if cnt3 is less than or equal to cnt1. The values of cnt2 and cnt4 are taken as input but are not used in the function's logic.

