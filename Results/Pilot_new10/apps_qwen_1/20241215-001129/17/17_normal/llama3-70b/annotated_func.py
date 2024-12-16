#State of the program right berfore the function call: The input consists of four lines, where each line contains one integer \( cnt_i \) (\( 0 \le cnt_i \le 10^9 \)), representing the counts of strings "(((", "()", "())", and "))" respectively.
def func():
    cnt1, cnt2, cnt3, cnt4 = map(int, [input() for _ in range(4)])
    if (cnt3 > cnt1) :
        print(0)
    else :
        print(1)
    #State of the program after the if-else block has been executed: *`cnt1`, `cnt2`, `cnt3`, and `cnt4` are integers. If `cnt3` is greater than `cnt1`, no changes are made to the variables. If `cnt3` is less than or equal to `cnt1`, no changes are made to the variables.
#Overall this is what the function does:The function reads four integers from the user, each representing the counts of "(((", "()", "())", and "))" respectively. It then compares the count of "())" with the count of "((( )". If the count of "())" is greater than the count of "((( ", it prints `0`; otherwise, it prints `1`. The function does not return any value.

