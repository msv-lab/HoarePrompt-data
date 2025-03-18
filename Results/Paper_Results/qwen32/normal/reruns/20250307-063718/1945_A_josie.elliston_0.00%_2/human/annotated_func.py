#State of the program right berfore the function call: extroverts is a non-negative integer, universals is a non-negative integer.
def func_1(extroverts, universals):
    if (extroverts % 3 != 0) :
        if (extroverts % 3 + universals < 3) :
            return None
            #The program returns None
        #State: `extroverts` is a non-negative integer, `universals` is a non-negative integer, the remainder of `extroverts` divided by 3 is not 0, and the sum of the remainder of `extroverts` divided by 3 and `universals` is 3 or greater
    #State: `extroverts` is a non-negative integer, `universals` is a non-negative integer. If the remainder of `extroverts` divided by 3 is not 0, then the sum of the remainder of `extroverts` divided by 3 and `universals` is 3 or greater.
    return ceil((extroverts + universals) / 3)
    #The program returns the ceiling of the sum of `extroverts` and `universals` divided by 3.
#Overall this is what the function does:The function accepts two non-negative integer parameters, `extroverts` and `universals`. It returns `None` if the remainder of `extroverts` divided by 3 is not zero and the sum of this remainder and `universals` is less than 3. Otherwise, it returns the ceiling of the sum of `extroverts` and `universals` divided by 3.

#State of the program right berfore the function call: introverts, extroverts, and universals are non-negative integers representing the number of introverts, extroverts, and universals respectively.
def func_2(introverts, extroverts, universals):
    ret = func_1(extroverts, universals)
    return -1 if ret is None else introverts + ret
    #The program returns -1 if the value returned by `func_1(extroverts, universals)` is None, otherwise it returns the sum of `introverts` and the value returned by `func_1(extroverts, universals)`
#Overall this is what the function does:The function takes three non-negative integer parameters: `introverts`, `extroverts`, and `universals`. It returns -1 if the result of `func_1(extroverts, universals)` is `None`; otherwise, it returns the sum of `introverts` and the result of `func_1(extroverts, universals)`.

