#State of the program right berfore the function call: extroverts is a non-negative integer, universals is a non-negative integer.
def func_1(extroverts, universals):
    if (extroverts % 3 != 0) :
        if (extroverts % 3 + universals < 3) :
            return None
            #The program returns None
        #State: `extroverts` is a non-negative integer that is not divisible by 3, and `universals` is a non-negative integer. Additionally, `extroverts % 3 + universals` is greater than or equal to 3.
    #State: `extroverts` is a non-negative integer, and `universals` is a non-negative integer. If `extroverts` is not divisible by 3, then `extroverts % 3 + universals` is greater than or equal to 3.
    return ceil((extroverts + universals) / 3)
    #The program returns the ceiling of the division of the sum of `extroverts` and `universals` by 3.
#Overall this is what the function does:The function takes two non-negative integer parameters, `extroverts` and `universals`. It returns `None` if `extroverts` is not divisible by 3 and the sum of `extroverts % 3` and `universals` is less than 3. Otherwise, it returns the ceiling of the division of the sum of `extroverts` and `universals` by 3.

#State of the program right berfore the function call: introverts, extroverts, and universals are non-negative integers representing the number of introverts, extroverts, and universals respectively.
def func_2(introverts, extroverts, universals):
    ret = func_1(extroverts, universals)
    return -1 if ret is None else introverts + ret
    #The program returns -1 if `ret` is None; otherwise, it returns the sum of `introverts` and `ret`.
#Overall this is what the function does:The function takes three non-negative integer parameters representing the counts of introverts, extroverts, and universals. It returns -1 if a call to `func_1` with `extroverts` and `universals` returns `None`; otherwise, it returns the sum of `introverts` and the result of `func_1`.

