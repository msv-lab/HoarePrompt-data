#State of the program right berfore the function call: The input consists of four non-negative integers representing the counts of the bracket sequences "(", "()", ")(", and ")" respectively, denoted by cnt_1, cnt_2, cnt_3, and cnt_4, such that 0 <= cnt_1, cnt_2, cnt_3, cnt_4 <= 10^9.
def func():
    cnt1 = int(input())
    cnt2 = int(input())
    cnt3 = int(input())
    cnt4 = int(input())
    if (cnt1 + cnt2 == cnt3 + cnt4 and cnt2 >= cnt3) :
        print(1)
    else :
        print(0)
    #State of the program after the if-else block has been executed: *`cnt1`, `cnt2`, `cnt_3`, `cnt_4` are input integers. If the sum of `cnt1` and `cnt2` equals the sum of `cnt_3` and `cnt_4`, and `cnt2` is greater than or equal to `cnt_3`, then the value 1 has been printed. Otherwise, the value 0 has been printed and returned as output, indicating that either the sums are not equal or `cnt2` is less than `cnt_3`.
#Overall this is what the function does:The function takes four non-negative integers as input, checks if the sum of the first two equals the sum of the last two and if the second is greater than or equal to the third, then prints 1 if both conditions are met, otherwise prints 0, without handling potential input exceptions or range checks

