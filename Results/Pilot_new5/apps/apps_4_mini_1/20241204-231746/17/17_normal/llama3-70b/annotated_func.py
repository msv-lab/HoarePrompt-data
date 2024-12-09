#State of the program right berfore the function call: cnt_1, cnt_2, cnt_3, and cnt_4 are non-negative integers such that 0 <= cnt_i <= 10^9 for i in {1, 2, 3, 4}.
def func():
    cnt1, cnt2, cnt3, cnt4 = map(int, [input() for _ in range(4)])
    if (cnt3 > cnt1) :
        print(0)
    else :
        print(1)
    #State of the program after the if-else block has been executed: *`cnt_1`, `cnt_2`, `cnt_3`, and `cnt_4` are non-negative integers. If `cnt_3` is greater than `cnt_1`, then the output printed is 0. Otherwise, if `cnt_3` is less than or equal to `cnt_1`, then 1 is printed to the console.
#Overall this is what the function does:The function accepts four non-negative integers `cnt1`, `cnt2`, `cnt3`, and `cnt4` (inputted by the user) and prints 0 if `cnt3` is greater than `cnt1`, otherwise it prints 1. The value of `cnt2` and `cnt4` is inputted but not used in any computation or condition within the function.

