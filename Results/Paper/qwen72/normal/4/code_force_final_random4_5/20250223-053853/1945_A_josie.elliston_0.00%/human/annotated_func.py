#State of the program right berfore the function call: extroverts and universals are non-negative integers such that 0 <= extroverts, universals <= 10^9.
def func_1(extroverts, universals):
    if (extroverts % 3 != 0) :
        if (extroverts % 3 + universals < 3) :
            return None
            #The program returns None.
        #State: extroverts and universals are non-negative integers such that 0 <= extroverts, universals <= 10^9, and the current value of extroverts is not divisible by 3. Additionally, the sum of the remainder of extroverts divided by 3 and universals is greater than or equal to 3.
    #State: extroverts and universals are non-negative integers such that 0 <= extroverts, universals <= 10^9. If extroverts % 3 != 0, the sum of the remainder of extroverts divided by 3 and universals is greater than or equal to 3.
    return ceil((extroverts + universals) / 3)
    #The program returns the ceiling of (extroverts + universals) / 3, where extroverts and universals are non-negative integers such that 0 <= extroverts, universals <= 10^9, and if extroverts % 3 != 0, the sum of the remainder of extroverts divided by 3 and universals is greater than or equal to 3.
#Overall this is what the function does:The function `func_1` accepts two non-negative integers, `extroverts` and `universals`, both of which are in the range 0 to 10^9. If `extroverts` is not divisible by 3 and the sum of the remainder of `extroverts` divided by 3 and `universals` is less than 3, the function returns `None`. Otherwise, it returns the ceiling of the division of the sum of `extroverts` and `universals` by 3.

#State of the program right berfore the function call: introverts, extroverts, and universals are non-negative integers such that 0 <= introverts, extroverts, universals <= 10^9.
def func_2(introverts, extroverts, universals):
    ret = func_1(extroverts, universals)
    return -1 if ret is None else introverts + ret
    #The program returns -1 if `ret` is None, otherwise it returns the sum of `introverts` and `ret`. Here, `ret` is the result of `func_1(extroverts, universals)`, where `extroverts` and `universals` are non-negative integers between 0 and 10^9.
#Overall this is what the function does:The function `func_2` accepts three non-negative integer parameters `introverts`, `extroverts`, and `universals`, each between 0 and 10^9. It returns -1 if `func_1(extroverts, universals)` returns `None`, otherwise it returns the sum of `introverts` and the result of `func_1(extroverts, universals)`.

