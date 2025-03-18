#State of the program right berfore the function call: cnt_1, cnt_2, cnt_3, and cnt_4 are non-negative integers such that 0 <= cnt_i <= 10^9 for i in {1, 2, 3, 4}.
def func():
    cnt1, cnt2, cnt3, cnt4 = map(int, [input() for _ in range(4)])
    if (cnt3 > cnt1) :
        print(0)
    else :
        print(1)
    #State of the program after the if-else block has been executed: *`cnt_1`, `cnt_2`, `cnt_3`, and `cnt_4` are input integers. If `cnt_3` is greater than `cnt_1`, then 0 has been printed to the console. Otherwise, `cnt_3` is less than or equal to `cnt_1`.
#Overall this is what the function does:The function accepts no parameters and reads four non-negative integers from the input. It compares the third integer (cnt3) with the first integer (cnt1). If cnt3 is greater than cnt1, it prints 0; otherwise, it prints 1. The function does not return any value.

