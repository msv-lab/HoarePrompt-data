#State of the program right berfore the function call: extroverts and universals are non-negative integers.
def func_1(extroverts, universals):
    if (extroverts % 3 != 0) :
        if (extroverts % 3 + universals < 3) :
            return None
            #The program returns None
        #State: extroverts and universals are non-negative integers. The current value of extroverts is not divisible by 3. The sum of the remainder when extroverts is divided by 3 and the value of universals is 3 or more.
    #State: extroverts and universals are non-negative integers. If the current value of extroverts is not divisible by 3, the sum of the remainder when extroverts is divided by 3 and the value of universals is 3 or more. Otherwise, there is no change to the values of extroverts and universals.
    return ceil((extroverts + universals) / 3)
    #The program returns the ceiling of the sum of `extroverts` and `universals` divided by 3.
#Overall this is what the function does:The function `func_1` accepts two non-negative integer parameters, `extroverts` and `universals`. It returns `None` if the remainder of `extroverts` divided by 3, when added to `universals`, is less than 3. Otherwise, it returns the ceiling of the sum of `extroverts` and `universals` divided by 3.

#State of the program right berfore the function call: introverts, extroverts, and universals are non-negative integers representing the number of introverts, extroverts, and universals respectively.
def func_2(introverts, extroverts, universals):
    ret = func_1(extroverts, universals)
    return -1 if ret is None else introverts + ret
    #The program returns -1 if `ret` is None; otherwise, it returns the sum of `introverts` and `ret`.
#Overall this is what the function does:The function accepts three non-negative integer parameters: `introverts`, `extroverts`, and `universals`. It computes a value `ret` using `func_1` with `extroverts` and `universals`. If `ret` is `None`, the function returns -1; otherwise, it returns the sum of `introverts` and `ret`.

