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
    #State of the program after the if-else block has been executed: *`cnt_1`, `cnt_2`, `cnt_3`, and `cnt_4` are integers satisfying 0 <= `cnt_4` <= 10^9. If `cnt_1 + cnt_2` equals `cnt_3 + cnt_4` and `cnt_2` is greater than or equal to `cnt_3`, the output of the print statement is 1. Otherwise, the output of the print statement is 0.
#Overall this is what the function does:The function reads four non-negative integer values from user input, named `cnt1`, `cnt2`, `cnt3`, and `cnt4`. It checks if the sum of the first two integers (`cnt1 + cnt2`) equals the sum of the last two integers (`cnt3 + cnt4`) and whether `cnt2` is greater than or equal to `cnt3`. If both conditions are met, it prints `1`. Otherwise, it prints `0`. The function does not return any values, and the final outputs are solely determined by the input conditions without any additional state modifications to the input variables. It also does not handle potential edge cases such as invalid input types or values outside the specified ranges, which could lead to runtime errors.

