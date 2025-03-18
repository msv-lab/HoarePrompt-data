#State of the program right berfore the function call: extroverts and universals are non-negative integers.
def func_1(extroverts, universals):
    if (extroverts % 3 != 0) :
        if (extroverts % 3 + universals < 3) :
            return None
            #The program returns None
        #State: extroverts and universals are non-negative integers. The current value of extroverts is not divisible by 3. The sum of the remainder of extroverts divided by 3 and universals is 3 or more.
    #State: extroverts and universals are non-negative integers. If the current value of extroverts is not divisible by 3, the sum of the remainder of extroverts divided by 3 and universals is 3 or more.
    return ceil((extroverts + universals) / 3)
    #The program returns the ceiling of the sum of extroverts and universals divided by 3. Given the conditions, this value is at least 2.
#Overall this is what the function does:The function accepts two non-negative integer parameters, `extroverts` and `universals`. It returns `None` if the remainder of `extroverts` divided by 3 plus `universals` is less than 3. Otherwise, it returns the ceiling of the sum of `extroverts` and `universals` divided by 3, which is at least 2.

#State of the program right berfore the function call: introverts, extroverts, and universals are non-negative integers representing the number of introverts, extroverts, and universals respectively.
def func_2(introverts, extroverts, universals):
    ret = func_1(extroverts, universals)
    return -1 if ret is None else introverts + ret
    #The program returns -1 if `ret` is None else it returns the sum of `introverts` and `ret`.
#Overall this is what the function does:The function accepts three non-negative integer parameters: `introverts`, `extroverts`, and `universals`. It computes a value based on `extroverts` and `universals` using `func_1`. If the computed value is `None`, the function returns -1. Otherwise, it returns the sum of `introverts` and the computed value.

