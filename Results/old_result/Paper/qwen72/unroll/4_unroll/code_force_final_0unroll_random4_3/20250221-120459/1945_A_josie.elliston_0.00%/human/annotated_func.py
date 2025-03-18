#State of the program right berfore the function call: extroverts and universals are non-negative integers such that 0 <= extroverts, universals <= 10^9.
def func_1(extroverts, universals):
    if (extroverts % 3 != 0) :
        if (extroverts % 3 + universals < 3) :
            return None
            #The program returns None.
        #State: extroverts and universals are non-negative integers such that 0 <= extroverts, universals <= 10^9, and the current value of extroverts is not divisible by 3. Additionally, the sum of (extroverts % 3) and universals is greater than or equal to 3.
    #State: `extroverts` and `universals` are non-negative integers such that 0 <= `extroverts`, `universals` <= 10^9. If `extroverts` is not divisible by 3, the sum of (`extroverts` % 3) and `universals` is greater than or equal to 3.
    return ceil((extroverts + universals) / 3)
    #The program returns the ceiling of the division of the sum of `extroverts` and `universals` by 3.
#Overall this is what the function does:The function `func_1` accepts two non-negative integers, `extroverts` and `universals`, where both are between 0 and 10^9 inclusive. If `extroverts` is not divisible by 3 and the sum of `extroverts % 3` and `universals` is less than 3, the function returns `None`. Otherwise, it returns the ceiling of the division of the sum of `extroverts` and `universals` by 3.

#State of the program right berfore the function call: introverts, extroverts, and universals are non-negative integers such that 0 <= introverts, extroverts, universals <= 10^9.
def func_2(introverts, extroverts, universals):
    ret = func_1(extroverts, universals)
    return -1 if ret is None else introverts + ret
    #The program returns -1 if the result of `func_1(extroverts, universals)` is `None`. Otherwise, it returns the sum of `introverts` and the result of `func_1(extroverts, universals)`. `introverts` is a non-negative integer between 0 and 10^9, `extroverts` is a non-negative integer between 0 and 10^9, and `universals` is a non-negative integer between 0 and 10^9.
#Overall this is what the function does:The function `func_2` accepts three non-negative integer parameters `introverts`, `extroverts`, and `universals`, each ranging from 0 to 10^9. It returns -1 if `func_1(extroverts, universals)` returns `None`. Otherwise, it returns the sum of `introverts` and the result of `func_1(extroverts, universals)`.

