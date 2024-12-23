#State of the program right berfore the function call: cnt_1, cnt_2, cnt_3, and cnt_4 are integers such that 0 <= cnt_i <= 10^9 for i in {1, 2, 3, 4}.
def func():
    cnt1 = int(input())
    cnt2 = int(input())
    cnt3 = int(input())
    cnt4 = int(input())
    if (cnt1 + cnt2 == cnt3 + cnt4 and cnt2 >= cnt3) :
        print(1)
    else :
        print(0)
    #State of the program after the if-else block has been executed: *`cnt_1`, `cnt_2`, `cnt_3`, and `cnt_4` are integers. If the sum of `cnt_1` and `cnt_2` equals the sum of `cnt_3` and `cnt_4` and `cnt_2` is greater than or equal to `cnt_3`, then the value `1` is printed. Otherwise, the output is `0`.
#Overall this is what the function does:The function reads four integer inputs from the user and checks whether the sum of the first two integers equals the sum of the last two integers, while also verifying that the second integer is greater than or equal to the third integer. It outputs `1` if both conditions are true; otherwise, it outputs `0`. The function does not return any values or accept any parameters, and it only interacts with the user through console input and output. Additionally, the function accepts inputs in the range of `0` to `10^9`, but does not handle invalid inputs or any exceptions that may arise from this. This means that if the user enters non-integer values, the function will throw an error, which is a missing functionality in terms of input validation.

