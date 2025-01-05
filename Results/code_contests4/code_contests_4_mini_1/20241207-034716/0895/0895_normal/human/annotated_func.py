#State of the program right berfore the function call: h_1, m_1, h_2, and m_2 are integers such that 0 ≤ h_1, h_2 ≤ 23 and 0 ≤ m_1, m_2 ≤ 59, and the contest lasts an even number of minutes with m_1 % 2 = m_2 % 2, and the duration of the contest is at least two minutes.
def func():
    a = map(int, raw_input().split(':'))
    c = a[0] * 60 + a[1]
    a = map(int, raw_input().split(':'))
    c += a[0] * 60 + a[1]
    c /= 2
    d = map(str, divmod(c, 60))
    if (len(d[0]) == 1) :
        d[0] = '0' + d[0]
    #State of the program after the if block has been executed: *`h_1`, `m_1`, `h_2`, `m_2` are integers; `d` holds string representations of the quotient and remainder from dividing `c` (halved) by 60; if the length of the first element of `d` is equal to 1, `d[0]` is updated to '0' + `d[0]`, making `d[0]` a two-character string.
    if (len(d[1]) == 1) :
        d[1] = '0' + d[1]
    #State of the program after the if block has been executed: *`h_1`, `m_1`, `h_2`, `m_2` are integers; `d` holds string representations of the quotient and remainder from dividing `c` (halved) by 60. If the length of the second element of `d` is equal to 1, then `d[1]` is updated to '0' + its previous value.
#Overall this is what the function does:The function accepts two pairs of time inputs in the format "h:m" (representing the start and end times of a contest) and calculates the average time by halving the total minutes between the two times. It ensures that both the hour and minute components of the average time are formatted as two-digit strings. The function does not return any value or output, so the results are not directly accessible to the caller; it processes the input but lacks a return statement or output mechanism.

