#State of the program right berfore the function call: The input consists of four lines, where the i-th line contains one integer cnt_i representing the number of strings of type i ("((") or i+1 ("()", "(})", "))"), with 0 ≤ cnt_i ≤ 10^9 for i = 0, 1, 2, 3.
def func():
    cnt1 = int(input())
    cnt2 = int(input())
    cnt3 = int(input())
    cnt4 = int(input())
    if (cnt1 + cnt2 == cnt3 + cnt4 and cnt2 >= cnt3) :
        print(1)
    else :
        print(0)
    #State of the program after the if-else block has been executed: *`cnt0` is 0, `cnt1` is an input integer, `cnt2` is the integer input from the user, `cnt3` is an integer input from the user, `cnt4` is an integer input from the user. If the condition `(cnt1 + cnt2 == cnt3 + cnt4 and cnt2 >= cnt3)` is true, no changes are made to `cnt2`, `cnt3`, or `cnt4`. Otherwise, either `cnt1 + cnt2` is not equal to `cnt3 + cnt4` or `cnt2` is less than `cnt3`.
#Overall this is what the function does:The function accepts four integers through separate input lines, representing counts of "((", "()", "(})", and "))" respectively. It then checks if the sum of counts of "((" and "()" is equal to the sum of counts of "(}" and "))", and also ensures that the count of "()" is greater than or equal to the count of "(}". If both conditions are met, it prints `1`; otherwise, it prints `0`. The function does not return any value but modifies the state of `cnt2` and `cnt3` by checking their values against the given conditions.

