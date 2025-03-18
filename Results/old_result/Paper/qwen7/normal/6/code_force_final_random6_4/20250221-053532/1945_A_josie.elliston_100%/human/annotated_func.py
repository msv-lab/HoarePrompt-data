#State of the program right berfore the function call: extroverts is a non-negative integer representing the number of extroverts, and universals is a non-negative integer representing the number of universals.
def func_1(extroverts, universals):
    if (extroverts % 3 != 0) :
        if (extroverts % 3 + universals < 3) :
            return None
            #The program returns None
        #State: `extroverts` is a non-negative integer representing the number of extroverts, and `universals` is a non-negative integer representing the number of universals. The current value of `extroverts` is not divisible by 3, and `extroverts % 3 + universals` is greater than or equal to 3
    #State: Postcondition: `extroverts` is a non-negative integer representing the number of extroverts, and `universals` is a non-negative integer representing the number of universals. If `extroverts` is not divisible by 3 and `extroverts % 3 + universals` is greater than or equal to 3, then the condition `extroverts % 3 + universals >= 3` holds true.
    return ceil((extroverts + universals) / 3)
    #The program returns the ceiling value of (extroverts + universals) divided by 3, where extroverts is a non-negative integer representing the number of extroverts and universals is a non-negative integer representing the number of universals.
#Overall this is what the function does:The function accepts two parameters, `extroverts` and `universals`, both of which are non-negative integers. It checks if the sum of `extroverts` and `universals` is zero; if so, it returns `None`. Otherwise, it returns the ceiling value of the sum of `extroverts` and `universals` divided by 3.

#State of the program right berfore the function call: introverts is a non-negative integer representing the number of introverts, extroverts is a non-negative integer representing the number of extroverts, and universals is a non-negative integer representing the number of universals.
def func_2(introverts, extroverts, universals):
    ret = func_1(extroverts, universals)
    return -1 if ret is None else introverts + ret
    #The program returns introverts plus ret if ret is not None, otherwise it returns -1.
#Overall this is what the function does:The function accepts three parameters: `introverts`, `extroverts`, and `universals`, all of which are non-negative integers. It calls another function `func_1` with `extroverts` and `universals` as arguments. If `func_1` returns `None`, the function returns `-1`; otherwise, it returns the sum of `introverts` and the value returned by `func_1`.

