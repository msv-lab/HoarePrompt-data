#State of the program right berfore the function call: extroverts is a non-negative integer representing the number of extroverts, and universals is a non-negative integer representing the number of universals.
def func_1(extroverts, universals):
    if (extroverts % 3 != 0) :
        if (extroverts % 3 + universals < 3) :
            return None
            #The program returns None
        #State: extroverts is a non-negative integer representing the number of extroverts, and universals is a non-negative integer representing the number of universals. The current value of extroverts is not divisible by 3, and (extroverts % 3 + universals) is greater than or equal to 3
    #State: `extroverts` is a non-negative integer representing the number of extroverts, and `universals` is a non-negative integer representing the number of universals. If `extroverts` is not divisible by 3 and `(extroverts % 3 + universals) >= 3`, then `universals` is adjusted such that `(extroverts % 3 + universals) == 3`.
    return ceil((extroverts + universals) / 3)
    #The program returns the ceiling value of (extroverts + universals) divided by 3, where extroverts is a non-negative integer representing the number of extroverts, and universals is a non-negative integer representing the number of universals, and if extroverts is not divisible by 3 and (extroverts % 3 + universals) >= 3, then universals is adjusted such that (extroverts % 3 + universals) == 3.
#Overall this is what the function does:The function accepts two parameters, `extroverts` and `universals`, both non-negative integers. If `extroverts` is not divisible by 3 and `(extroverts % 3 + universals)` is at least 3, it adjusts `universals` so that `(extroverts % 3 + universals)` equals 3. The function then returns the ceiling value of `(extroverts + universals)` divided by 3. If the initial condition is not met, the function returns `None`.

#State of the program right berfore the function call: introverts, extroverts, and universals are non-negative integers such that 0 <= introverts, extroverts, universals <= 10^9.
def func_2(introverts, extroverts, universals):
    ret = func_1(extroverts, universals)
    return -1 if ret is None else introverts + ret
    #The program returns introverts plus ret if ret is not None, otherwise it returns -1.
#Overall this is what the function does:The function accepts three parameters: `introverts`, `extroverts`, and `universals`. It calls another function `func_1` with `extroverts` and `universals` as arguments. Depending on the result, it either returns the sum of `introverts` and the result of `func_1`, or returns `-1` if `func_1` returns `None`.

