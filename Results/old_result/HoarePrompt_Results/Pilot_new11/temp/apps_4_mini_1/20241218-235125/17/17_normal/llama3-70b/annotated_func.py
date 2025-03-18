#State of the program right berfore the function call: cnt_1, cnt_2, cnt_3, and cnt_4 are non-negative integers such that 0 <= cnt_i <= 10^9 for i = 1, 2, 3, 4.
def func():
    cnt1, cnt2, cnt3, cnt4 = map(int, [input() for _ in range(4)])
    if (cnt3 > cnt1) :
        print(0)
    else :
        print(1)
    #State of the program after the if-else block has been executed: *`cnt_1`, `cnt_2`, `cnt_3`, and `cnt_4` are non-negative integers. If `cnt_3` is greater than `cnt_1`, then the program retains that state. Otherwise, `cnt_3` is less than or equal to `cnt_1`, and the variables retain their non-negative integer values.
#Overall this is what the function does:The function reads four non-negative integers from user input and compares the first integer (`cnt_1`) with the third integer (`cnt_3`). If `cnt_3` is greater than `cnt_1`, it outputs `0`. Otherwise, it outputs `1`. The function does not return a value or alter the input integers; it merely prints an output based on the comparison. The variables `cnt_1`, `cnt_2`, `cnt_3`, and `cnt_4` remain non-negative integers in the range [0, 10^9] throughout the function execution. There are no conditions or logic in the code to handle any specific edge cases such as invalid input or numbers out of the specified range, as it assumes correct use according to the comments.

