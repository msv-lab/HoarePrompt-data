#State of the program right berfore the function call: the input consists of four non-negative integers cnt_1, cnt_2, cnt_3, and cnt_4, representing the counts of the strings "((", "()", ")(", and "))" respectively.
def func():
    cnt1, cnt2, cnt3, cnt4 = map(int, [input() for _ in range(4)])
    if (cnt3 > cnt1) :
        print(0)
    else :
        print(1)
    #State of the program after the if-else block has been executed: `cnt1`, `cnt2`, `cnt3`, `cnt4` are non-negative integers representing the counts of "(()", "()", ")(", and "}}" respectively. If `cnt3` is greater than `cnt1`, the function returns 0. Otherwise, the function prints 1 and `cnt3` is less than or equal to `cnt1`.
#Overall this is what the function does:The function takes four non-negative integers as input, representing the counts of the strings "((", "()", ")(", and "))" respectively, and returns 0 if the count of ")(" is greater than the count of "((", otherwise it prints 1, indicating that the count of ")(" is less than or equal to the count of "(("; the function does not modify the input variables or perform any additional operations beyond this conditional check and output, and does not account for any potential exceptions or edge cases such as non-integer or negative input values, which may cause the function to behave unexpectedly or terminate prematurely; the function's final state is that it has printed either 0 or 1 based on the input counts, without altering the original input counts or having any further effects on the program's state.

