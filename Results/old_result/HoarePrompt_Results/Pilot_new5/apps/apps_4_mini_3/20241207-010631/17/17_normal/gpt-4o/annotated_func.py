#State of the program right berfore the function call: cnt_1, cnt_2, cnt_3, and cnt_4 are non-negative integers such that 0 <= cnt_i <= 10^9 for i in {1, 2, 3, 4}.
def func():
    cnt1 = int(input())
    cnt2 = int(input())
    cnt3 = int(input())
    cnt4 = int(input())
    if (cnt1 + cnt2 == cnt3 + cnt4 and cnt2 >= cnt3) :
        print(1)
    else :
        print(0)
    #State of the program after the if-else block has been executed: *`cnt_1` is a non-negative integer, `cnt_2`, `cnt_3`, and `cnt_4` are input integers. If `cnt_1 + cnt_2` equals `cnt_3 + cnt_4` and `cnt_2` is greater than or equal to `cnt_3`, the output is 1. Otherwise, the output is 0.
#Overall this is what the function does:The function accepts four non-negative integers as input (cnt1, cnt2, cnt3, cnt4), checks if the sum of cnt1 and cnt2 equals the sum of cnt3 and cnt4, and whether cnt2 is greater than or equal to cnt3. It prints 1 if both conditions are met; otherwise, it prints 0. The function does not return any values.

