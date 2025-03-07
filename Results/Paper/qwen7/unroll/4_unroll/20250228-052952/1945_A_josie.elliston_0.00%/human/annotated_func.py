#State of the program right berfore the function call: extroverts is a non-negative integer representing the number of extroverts, and universals is a non-negative integer representing the number of universals.
def func_1(extroverts, universals):
    if (extroverts % 3 != 0) :
        if (extroverts % 3 + universals < 3) :
            return None
            #The program returns None
        #State: extroverts is a non-negative integer representing the number of extroverts, and universals is a non-negative integer representing the number of universals. The current value of extroverts is not divisible by 3, and (extroverts % 3 + universals) is greater than or equal to 3
    #State: `extroverts` is a non-negative integer representing the number of extroverts, and `universals` is a non-negative integer representing the number of universals. If `extroverts` modulo 3 is not equal to 0 and `(extroverts % 3 + universals)` is greater than or equal to 3, then the condition holds true. Otherwise, no change is made to the values of `extroverts` and `universals`.
    return ceil((extroverts + universals) / 3)
    #The program returns the ceiling value of (extroverts + universals) divided by 3, given that extroverts modulo 3 is not equal to 0 and (extroverts % 3 + universals) is greater than or equal to 3.
#Overall this is what the function does:The function accepts two parameters, `extroverts` and `universals`, both non-negative integers. It checks if `extroverts` modulo 3 is not equal to 0 and if `(extroverts % 3 + universals)` is greater than or equal to 3. If these conditions are met, it returns the ceiling value of `(extroverts + universals)` divided by 3. Otherwise, it returns None.

#State of the program right berfore the function call: introverts, extroverts, and universals are non-negative integers such that 0 <= introverts, extroverts, universals <= 10^9.
def func_2(introverts, extroverts, universals):
    ret = func_1(extroverts, universals)
    return -1 if ret is None else introverts + ret
    #The program returns -1 if `ret` is None, otherwise it returns the value of `introverts` plus the value of `ret`.
#Overall this is what the function does:The function accepts three parameters (`introverts`, `extroverts`, and `universals`) and calls another function `func_1` with `extroverts` and `universals` as arguments. If the result of `func_1` is `None`, the function returns `-1`; otherwise, it returns the sum of `introverts` and the result of `func_1`.

