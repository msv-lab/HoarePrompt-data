#State of the program right berfore the function call: h_1, m_1, h_2, and m_2 are integers such that 0 ≤ h_1, h_2 ≤ 23 and 0 ≤ m_1, m_2 ≤ 59. The contest lasts an even number of minutes, and it lasts at least two minutes, occurring within a single day.
def func():
    a = map(int, raw_input().split(':'))
    c = a[0] * 60 + a[1]
    a = map(int, raw_input().split(':'))
    c += a[0] * 60 + a[1]
    c /= 2
    d = map(str, divmod(c, 60))
    if (len(d[0]) == 1) :
        d[0] = '0' + d[0]
    #State of the program after the if block has been executed: *`h_1`, `m_1`, `h_2`, and `m_2` are integers; `c` is updated to half of its previous value; if the length of `d[0]` is 1, then `d[0]` is modified to be '0' + `d[0]`, resulting in a length of 2.
    if (len(d[1]) == 1) :
        d[1] = '0' + d[1]
    #State of the program after the if block has been executed: *`h_1`, `m_1`, `h_2`, and `m_2` are integers; `c` is half of its previous value; if the length of `d[1]` was 1, then `d[1]` is modified to be '0' + the original value of `d[1]`, resulting in a length of 2; `d[0]` is modified to be '0' + `d[0]` if its length was 1, and the length of `d[1]` is now 2.
#Overall this is what the function does:The function accepts no parameters and reads two time inputs in the format "hh:mm" representing the start and end times of a contest. It calculates the average time by converting these times into minutes, dividing by two, and then converting the result back into "hh:mm" format. It ensures that both hours and minutes are formatted as two digits. The function does not validate the inputs for correctness (e.g., the end time being after the start time), nor does it handle any potential errors related to input formatting. It returns the average time in the correct format but lacks error handling for invalid durations.

