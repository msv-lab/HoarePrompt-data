#State of the program right berfore the function call: The input consists of four non-negative integers cnt_1, cnt_2, cnt_3, and cnt_4, where 0 <= cnt_i <= 10^9 for i in {1, 2, 3, 4}.
def func():
    cnt1 = int(input())
    cnt2 = int(input())
    cnt3 = int(input())
    cnt4 = int(input())
    if (cnt1 + cnt2 == cnt3 + cnt4 and cnt2 >= cnt3) :
        print(1)
    else :
        print(0)
    #State of the program after the if-else block has been executed: *`cnt_1`, `cnt_2`, `cnt_3`, and `cnt_4` are non-negative integers; `cnt1` is a non-negative integer input; `cnt2`, `cnt3`, and `cnt4` are input integers. If `cnt1 + cnt2` equals `cnt3 + cnt4` and `cnt2` is greater than or equal to `cnt3`, the value 1 has been printed. Otherwise, if either condition is not met, the printed output is 0.
#Overall this is what the function does:The function accepts four non-negative integers as input (cnt1, cnt2, cnt3, cnt4) and prints 1 if the sum of cnt1 and cnt2 is equal to the sum of cnt3 and cnt4, and cnt2 is greater than or equal to cnt3; otherwise, it prints 0. There is no return value, only printed output.

