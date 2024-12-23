#State of the program right berfore the function call: cnt_1, cnt_2, cnt_3, and cnt_4 are non-negative integers such that 0 <= cnt_i <= 10^9 for i in {1, 2, 3, 4}.
def func():
    cnt1, cnt2, cnt3, cnt4 = map(int, [input() for _ in range(4)])
    if (cnt3 > cnt1) :
        print(0)
    else :
        print(1)
    #State of the program after the if-else block has been executed: *`cnt1`, `cnt2`, `cnt3`, and `cnt4` are integers within the range of 0 to 10^9. If `cnt3` is greater than `cnt1`, then the state remains unchanged. Otherwise, if `cnt3` is less than or equal to `cnt1`, the state remains unchanged and 1 is printed.
#Overall this is what the function does:The function reads four non-negative integers (cnt1, cnt2, cnt3, cnt4) from user input, which must be within the range of 0 to 10^9. It evaluates whether cnt3 is greater than cnt1. If cnt3 is greater, it prints 0; otherwise, it prints 1. The function does not modify cnt1, cnt2, cnt3, or cnt4, and there are no return values. The function primarily serves to output a binary response based on this comparison. Additionally, there are unspecified behaviors for handling edge cases, such as invalid input or cases where cnt3 equals cnt1.

