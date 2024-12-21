#State of the program right berfore the function call: cnt_1, cnt_2, cnt_3, and cnt_4 are non-negative integers such that 0 <= cnt_i <= 10^9 for i in {1, 2, 3, 4}.
def func():
    cnt1, cnt2, cnt3, cnt4 = map(int, [input() for _ in range(4)])
    if (cnt3 > cnt1) :
        print(0)
    else :
        print(1)
    #State of the program after the if-else block has been executed: *`cnt_1`, `cnt_2`, `cnt_3`, `cnt_4` are non-negative integers where 0 <= `cnt_1`, `cnt_2`, `cnt_3`, `cnt_4` <= 10^9. If `cnt_3` is greater than `cnt_1`, the output is 0. Otherwise, `cnt_3` is less than or equal to `cnt_1`.
#Overall this is what the function does:The function reads four non-negative integers from user input and assigns them to variables `cnt1`, `cnt2`, `cnt3`, and `cnt4`. It then checks if `cnt3` is greater than `cnt1`. If it is, the function prints `0`. If `cnt3` is less than or equal to `cnt1`, it prints `1`. The function does not return any values and does not modify the input values, which remain unchanged. Notably, the function does not validate the range of inputs or handle edge cases where inputs may not be integers or are outside the specified bounds. Additionally, `cnt2` and `cnt4` are read but unused, which means the state of these variables does not impact the functionality of the function.

