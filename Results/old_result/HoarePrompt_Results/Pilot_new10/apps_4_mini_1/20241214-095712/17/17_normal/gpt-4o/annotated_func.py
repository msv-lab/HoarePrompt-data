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
    #State of the program after the if-else block has been executed: *`cnt_1` is a non-negative integer, `cnt_2` is an integer, `cnt_3` is an integer within the range 0 to 10^9, and `cnt_4` is a non-negative integer. If the sum of `cnt_1` and `cnt_2` equals the sum of `cnt_3` and `cnt_4` and `cnt_2` is greater than or equal to `cnt_3`, the value `1` has been printed. Otherwise, either the sum of `cnt_1` and `cnt_2` does not equal the sum of `cnt_3` and `cnt_4` or `cnt_2` is less than `cnt_3`.
#Overall this is what the function does:The function does not accept any parameters and reads four non-negative integers from input. It checks if the sum of the first two integers equals the sum of the last two integers and if the second integer is greater than or equal to the third integer. It prints `1` if both conditions are met; otherwise, it prints `0`. The function does not handle any edge cases for invalid inputs, and it relies on the assumption that the inputs will always be within the specified range (0 to 10^9).

