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
    #State of the program after the if block has been executed: *`h_1`, `m_1`, `h_2`, `m_2` are integers where `m_1 % 2 = m_2 % 2;` `a` is a list of integers obtained from the input string separated by ':', `c` is increased by a[0] * 60 + a[1] / 2, `d` is a list of strings obtained by applying `map` to the result of `divmod(c, 60)`. If the length of the first element of `d` is 1, then `d[0]` will have a leading '0'.
    if (len(d[1]) == 1) :
        d[1] = '0' + d[1]
    #State of the program after the if block has been executed: *`h_1`, `m_1`, `h_2`, `m_2` are integers where `m_1 % 2 = m_2 % 2;` `a` is a list of integers obtained from the input string separated by ':', `c` is increased by a[0] * 60 + a[1] / 2, `d` is a list of strings obtained by applying `map` to the result of `divmod(c, 60)`. If the length of the first element of `d` is 1, then `d[0]` will have a leading '0'. After the if condition, the length of the second element of `d` will be 1. If the length of `d[1]` is not 1, then `d[1]` will have a leading '0'.
#Overall this is what the function does:The function reads two times in the format 'hh:mm' from the user input, calculates the average time between them, and ensures the resulting minutes are always represented with leading zeros. The function does not accept any parameters and does not return anything.

