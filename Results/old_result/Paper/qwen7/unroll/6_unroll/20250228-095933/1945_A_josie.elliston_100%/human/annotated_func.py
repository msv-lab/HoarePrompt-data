#State of the program right berfore the function call: extroverts is a non-negative integer representing the number of extroverts, and universals is a non-negative integer representing the number of universals. The function returns the minimum number of tents required for the extroverts and universals to be accommodated according to the specified conditions, or None if it is impossible to accommodate them.
def func_1(extroverts, universals):
    if (extroverts % 3 != 0) :
        if (extroverts % 3 + universals < 3) :
            return None
            #The program returns None
        #State: extroverts is a non-negative integer, representing the number of extroverts, and universals is a non-negative integer, representing the number of universals. The current value of extroverts is not divisible by 3, and the sum of (extroverts modulo 3) and universals is greater than or equal to 3
    #State: extroverts is a non-negative integer, and universals is a non-negative integer. If extroverts is not divisible by 3 and the sum of (extroverts modulo 3) and universals is at least 3, then the function returns the minimum number of tents required. Otherwise, the function returns None.
    return ceil((extroverts + universals) / 3)
    #The program returns the ceiling value of (extroverts + universals) divided by 3 if extroverts is not divisible by 3 and the sum of (extroverts modulo 3) and universals is at least 3, otherwise it returns None.
#Overall this is what the function does:The function accepts two parameters, `extroverts` and `universals`, both non-negative integers. It checks if the number of extroverts is not divisible by 3 and if the sum of the remainder when extroverts is divided by 3 and the number of universals is at least 3. If these conditions are met, it returns the minimum number of tents required, calculated as the ceiling value of the sum of extroverts and universals divided by 3. If the conditions are not met, it returns None.

#State of the program right berfore the function call: introverts is a non-negative integer representing the number of introverts, extroverts is a non-negative integer representing the number of extroverts, and universals is a non-negative integer representing the number of universals.
def func_2(introverts, extroverts, universals):
    ret = func_1(extroverts, universals)
    return -1 if ret is None else introverts + ret
    #The program returns the value of `introverts` plus the return value of `func_1(extroverts, universals)` if `func_1(extroverts, universals)` does not return `None`; otherwise, it returns `-1`.
#Overall this is what the function does:The function accepts three parameters: `introverts`, `extroverts`, and `universals`, all of which are non-negative integers. It calls another function `func_1` with `extroverts` and `universals` as arguments. If `func_1` returns a value other than `None`, the function returns the sum of `introverts` and the value returned by `func_1`. If `func_1` returns `None`, the function returns `-1`.

