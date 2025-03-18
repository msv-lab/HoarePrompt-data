#State of the program right berfore the function call: the input consists of four non-negative integers, cnt_1, cnt_2, cnt_3, and cnt_4, representing the counts of bracket sequences "(", "()", ")(", and ")" respectively.
def func():
    cnt1 = int(input())
    cnt2 = int(input())
    cnt3 = int(input())
    cnt4 = int(input())
    if (cnt1 + cnt2 == cnt3 + cnt4 and cnt2 >= cnt3) :
        print(1)
    else :
        print(0)
    #State of the program after the if-else block has been executed: *`cnt_1`, `cnt_2`, `cnt_3`, `cnt_4` are input integers. If the sum of `cnt_1` and `cnt_2` equals the sum of `cnt_3` and `cnt_4`, and `cnt_2` is greater than or equal to `cnt_3`, then the value 1 has been printed. Otherwise, the value 0 has been printed.
#Overall this is what the function does:This function accepts four non-negative integers `cnt_1`, `cnt_2`, `cnt_3`, and `cnt_4` as input, representing counts of bracket sequences, and prints 1 if the sum of `cnt_1` and `cnt_2` equals the sum of `cnt_3` and `cnt_4`, and `cnt_2` is greater than or equal to `cnt_3`, otherwise it prints 0. The function does not return any values, it only prints the result. After the function concludes, the program state will have `cnt_1`, `cnt_2`, `cnt_3`, and `cnt_4` as input integers, and either 1 or 0 will have been printed to the console, depending on the conditions met. The function does not modify the input integers and does not handle any potential exceptions that may occur during the input process. The function assumes that the input will always be four non-negative integers.

