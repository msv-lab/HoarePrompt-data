#State of the program right berfore the function call: The input consists of four non-negative integers, cnt_1, cnt_2, cnt_3, and cnt_4, where cnt_1 represents the number of strings "((", cnt_2 represents the number of strings "()", cnt_3 represents the number of strings ")(", and cnt_4 represents the number of strings "))".
def func():
    cnt1, cnt2, cnt3, cnt4 = map(int, [input() for _ in range(4)])
    if (cnt3 > cnt1) :
        print(0)
    else :
        print(1)
    #State of the program after the if-else block has been executed: *`cnt1`, `cnt2`, `cnt3`, `cnt4` are non-negative integers. If `cnt3` is greater than `cnt1`, then 0 has been printed. Otherwise, `cnt3` is less than or equal to `cnt1`, and the number 1 has been printed.
#Overall this is what the function does:The function accepts four non-negative integers representing counts of "((", "()", ")((", and "))", and returns 1 if the count of "((" is greater than or equal to the count of ")((", indicating potential balance, and 0 otherwise

