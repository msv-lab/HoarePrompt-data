#State of the program right berfore the function call: extroverts is a non-negative integer, universals is a non-negative integer.
def func_1(extroverts, universals):
    if (extroverts % 3 != 0) :
        if (extroverts % 3 + universals < 3) :
            return None
            #The program returns None
        #State: `extroverts` is a non-negative integer that is not divisible by 3, `universals` is a non-negative integer, and the sum of the remainder of `extroverts` divided by 3 and `universals` is 3 or greater.
    #State: `extroverts` is a non-negative integer, `universals` is a non-negative integer. If `extroverts` is not divisible by 3, the sum of the remainder of `extroverts` divided by 3 and `universals` is 3 or greater.
    return ceil((extroverts + universals) / 3)
    #The program returns the ceiling of the sum of `extroverts` and `universals` divided by 3. Given the conditions, this value is at least 2.
#Overall this is what the function does:The function accepts two non-negative integer parameters, `extroverts` and `universals`. It returns `None` if `extroverts` is not divisible by 3 and the sum of the remainder of `extroverts` divided by 3 and `universals` is less than 3. Otherwise, it returns the ceiling of the sum of `extroverts` and `universals` divided by 3, which is at least 2.

#State of the program right berfore the function call: introverts, extroverts, and universals are non-negative integers representing the number of introverts, extroverts, and universals respectively.
def func_2(introverts, extroverts, universals):
    ret = func_1(extroverts, universals)
    return -1 if ret is None else introverts + ret
    #The program returns -1 if ret is None else the sum of introverts and ret, where introverts is a non-negative integer and ret is the result of func_1(extroverts, universals)
#Overall this is what the function does:The function takes three non-negative integer parameters representing the number of introverts, extroverts, and universals. It computes a result using `func_1` with the extroverts and universals. If the result is `None`, it returns -1; otherwise, it returns the sum of the introverts and the result.

