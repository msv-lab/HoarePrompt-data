#State of the program right berfore the function call: h_1, m_1, h_2, and m_2 are integers such that 0 ≤ h_1, h_2 ≤ 23, 0 ≤ m_1, m_2 ≤ 59, and m_1 % 2 = m_2 % 2.**
def func():
    a = map(int, raw_input().split(':'))
    c = a[0] * 60 + a[1]
    a = map(int, raw_input().split(':'))
    c += a[0] * 60 + a[1]
    c /= 2
    d = map(str, divmod(c, 60))
    if (len(d[0]) == 1) :
        d[0] = '0' + d[0]
    #State of the program after the if block has been executed: *`h_1`, `m_1`, `h_2`, `m_2`, `a` remain unchanged. `c` is updated to half of its previous value. `d` is a list of strings representing the result of dividing the updated `c` by 60 where the length of the first element of `d` is 2 if the length of `d[0]` is 1.
    if (len(d[1]) == 1) :
        d[1] = '0' + d[1]
    #State of the program after the if block has been executed: *`h_1`, `m_1`, `h_2`, `m_2`, `a` remain unchanged. `c` is updated to half of its previous value. `d` is a list of strings representing the result of dividing the updated `c` by 60 where the length of the first element of `d` is 2 if the length of `d[0]` is 1. Additionally, the length of the second element of `d` is 1. `d[1]` is updated by adding '0' at the beginning if the length of `d[1]` was 1 originally.
#Overall this is what the function does:The function `func` reads two time values in the format (hours:minutes) from the user input, calculates the average time between the two given times, and ensures that the minutes part of the average time has two digits. It then checks if the minutes of the average time have the same parity (both even or both odd) and adjusts the formatting if necessary. The function does not explicitly return any value but performs these operations.

