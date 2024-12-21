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
    #State of the program after the if-else block has been executed: *`cnt_1` is a non-negative integer such that 0 <= `cnt_1` <= 10^9; `cnt_2` is an input integer; `cnt_3` remains unchanged; `cnt_4` is an input integer assigned with an input integer value; `cnt1` is an input integer; `cnt3` is an input integer. If `cnt1 + cnt2` equals `cnt3 + cnt4` and `cnt2` is greater than or equal to `cnt3`, the conditions hold true. Otherwise, if `cnt1 + cnt2` does not equal `cnt3 + cnt4` or `cnt2` is less than `cnt3`, `0` has been printed.
#Overall this is what the function does:The function takes four input integers (referred to as cnt1, cnt2, cnt3, and cnt4) from the user. It checks if the sum of cnt1 and cnt2 equals the sum of cnt3 and cnt4, and also verifies that cnt2 is greater than or equal to cnt3. Depending on these conditions, it prints either `1` or `0`. After execution, cnt1, cnt2, cnt3, and cnt4 are non-negative integers, but cnt1, cnt2, cnt3, and cnt4 are not necessarily constrained within the specified bounds in the code; they rely on user input, which may lead to potential edge cases where those values exceed expected limits (like negative values or inputs greater than 10^9). The function does not accept parameters and does not explicitly return a value; instead, it prints a result based on the conditions it evaluates.

