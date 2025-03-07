#State of the program right berfore the function call: extroverts is a non-negative integer representing the number of extroverts, and universals is a non-negative integer representing the number of universals.
def func_1(extroverts, universals):
    if (extroverts % 3 != 0) :
        if (extroverts % 3 + universals < 3) :
            return None
            #The program returns None
        #State: extroverts is a non-negative integer representing the number of extroverts, and universals is a non-negative integer representing the number of universals. The current value of extroverts is not divisible by 3, and (extroverts % 3 + universals) is greater than or equal to 3
    #State: `extroverts` is a non-negative integer representing the number of extroverts, and `universals` is a non-negative integer representing the number of universals. If `extroverts` is not divisible by 3 and `(extroverts % 3 + universals) >= 3`, then the condition `(extroverts % 3 + universals) >= 3` holds true.
    return ceil((extroverts + universals) / 3)
    #The program returns the ceiling value of (extroverts + universals) divided by 3, where extroverts is a non-negative integer representing the number of extroverts and universals is a non-negative integer representing the number of universals.
#Overall this is what the function does:The function accepts two parameters, `extroverts` and `universals`, both of which are non-negative integers. It returns `None` if `extroverts` is not divisible by 3 and `(extroverts % 3 + universals)` is less than 3. Otherwise, it returns the ceiling value of `(extroverts + universals)` divided by 3.

#State of the program right berfore the function call: introverts, extroverts, and universals are non-negative integers such that 0 <= introverts, extroverts, universals <= 10^9.
def func_2(introverts, extroverts, universals):
    ret = func_1(extroverts, universals)
    return -1 if ret is None else introverts + ret
    #The program returns -1 if the function call `func_1(extroverts, universals)` returns None, otherwise it returns the value of `introverts` plus the result of the function call `func_1(extroverts, universals)`
#Overall this is what the function does:The function accepts three parameters (introverts, extroverts, and universals) and returns -1 if `func_1(extroverts, universals)` returns None. Otherwise, it returns the sum of `introverts` and the result of `func_1(extroverts, universals)`.

