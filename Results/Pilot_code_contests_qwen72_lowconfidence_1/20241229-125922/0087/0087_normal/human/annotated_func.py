#State of the program right berfore the function call: seconds is a non-negative integer representing the total seconds of the tape used, where the total input time does not exceed 7200 seconds (2 hours).
def func_1(seconds):
    h, remain = divmod(7200 - seconds, 3600)
    m, s = divmod(remain, 60)
    print('{:02d}:{:02d}:{:02d}'.format(h, m, s))
#Overall this is what the function does:The function `func_1` accepts a parameter `seconds`, a non-negative integer representing the total seconds of the tape used (up to 7200 seconds). It calculates the remaining time on the tape in hours, minutes, and seconds and prints this time in the format `HH:MM:SS`. The function does not return any value. The printed time represents the remaining duration of the tape, which is the difference between 7200 seconds (2 hours) and the input `seconds`. If `seconds` is 7200 or more, the printed time will be `00:00:00`. If `seconds` is less than 0, the behavior is undefined as the function assumes a non-negative input.

