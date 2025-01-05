#State of the program right berfore the function call: h_1, m_1, h_2, m_2 are integers such that 0 ≤ h_1, h_2 ≤ 23, 0 ≤ m_1, m_2 ≤ 59, m_1 \% 2 = m_2 \% 2, and the contest lasts at least two minutes.**
def func():
    a = map(int, raw_input().split(':'))
    c = a[0] * 60 + a[1]
    a = map(int, raw_input().split(':'))
    c += a[0] * 60 + a[1]
    c /= 2
    d = map(str, divmod(c, 60))
    if (len(d[0]) == 1) :
        d[0] = '0' + d[0]
    #State of the program after the if block has been executed: *`h_1`, `m_1`, `h_2`, `m_2` are integers such that 0 ≤ h_1, h_2 ≤ 23, 0 ≤ m_1, m_2 ≤ 59, m_1 \% 2 = m_2 \% 2, the contest lasts at least two minutes; `a` contains the integer values from the input split by ':', `c` is half of the total minutes calculated from the input hours and minutes, `d` contains the string representation of the tuple obtained by dividing `c` by 60, and if the length of the first element in `d` is 1, then `d[0]` has an additional '0' at the beginning.
    if (len(d[1]) == 1) :
        d[1] = '0' + d[1]
    #State of the program after the if block has been executed: *`h_1`, `m_1`, `h_2`, `m_2`, `a`, `c`, `d` are integers and strings. If the length of `d[1]` is 1, then `d[1]` contains a string with an additional '0' at the beginning. Otherwise, there is no change in the values of the variables.
#Overall this is what the function does:The function takes the start time (h_1, m_1) and end time (h_2, m_2) of a contest as input. It calculates the total duration of the contest in minutes and divides it by 2. The function then converts this duration into hours and minutes format. The constraints for the input times are 0 ≤ h_1, h_2 ≤ 23, 0 ≤ m_1, m_2 ≤ 59, and m_1 % 2 = m_2 % 2. The contest duration must be at least two minutes.

