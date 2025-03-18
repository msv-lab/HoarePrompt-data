#State of the program right berfore the function call: extroverts is a non-negative integer representing the number of extroverts, and universals is a non-negative integer representing the number of universals.
def func_1(extroverts, universals):
    if (extroverts % 3 != 0) :
        if (extroverts % 3 + universals < 3) :
            return None
            #The program returns None
        #State: `extroverts` is a non-negative integer representing the number of extroverts, and `universals` is a non-negative integer representing the number of universals. The current value of `extroverts` is not divisible by 3, and `extroverts % 3 + universals` is greater than or equal to 3
    #State: Postcondition: `extroverts` is a non-negative integer representing the number of extroverts, and `universals` is a non-negative integer representing the number of universals. If `extroverts` is not divisible by 3 and `extroverts % 3 + universals` is greater than or equal to 3, then the condition holds true. If `extroverts` is divisible by 3, no changes are made to `extroverts` and `universals`.
    return ceil((extroverts + universals) / 3)
    #The program returns the ceiling value of (extroverts + universals) divided by 3, where extroverts is a non-negative integer representing the number of extroverts and universals is a non-negative integer representing the number of universals. This value is calculated under the condition that if extroverts is not divisible by 3 and extroverts % 3 + universals is greater than or equal to 3, then the condition holds true. Otherwise, if extroverts is divisible by 3, no changes are made to extroverts and universals.
#Overall this is what the function does:The function accepts two parameters, `extroverts` and `universals`, both non-negative integers. If `extroverts` is not divisible by 3 and `extroverts % 3 + universals` is greater than or equal to 3, it returns the ceiling value of `(extroverts + universals) / 3`. Otherwise, it returns `None`.

#State of the program right berfore the function call: introverts, extroverts, and universals are non-negative integers such that 0 <= introverts, extroverts, universals <= 10^9.
def func_2(introverts, extroverts, universals):
    ret = func_1(extroverts, universals)
    return -1 if ret is None else introverts + ret
    #The program returns -1 if the return value of `func_1(extroverts, universals)` is None, otherwise it returns the sum of `introverts` and the return value of `func_1(extroverts, universals)`
#Overall this is what the function does:The function accepts three parameters: `introverts`, `extroverts`, and `universals`. It calls another function `func_1` with `extroverts` and `universals` as arguments. If `func_1` returns `None`, the function returns `-1`. Otherwise, it returns the sum of `introverts` and the value returned by `func_1`.

