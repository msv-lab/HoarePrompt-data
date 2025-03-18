#State of the program right berfore the function call: extroverts is a non-negative integer representing the number of extroverts, and universals is a non-negative integer representing the number of universals.
def func_1(extroverts, universals):
    if (extroverts % 3 != 0) :
        if (extroverts % 3 + universals < 3) :
            return None
            #The program returns None
        #State: `extroverts` is a non-negative integer representing the number of extroverts, and `universals` is a non-negative integer representing the number of universals. The current value of `extroverts` is not divisible by 3, and `extroverts % 3 + universals` is greater than or equal to 3
    #State: Postcondition: `extroverts` is a non-negative integer representing the number of extroverts, and `universals` is a non-negative integer representing the number of universals. If `extroverts` is not divisible by 3 and `extroverts % 3 + universals` is greater than or equal to 3, then `extroverts` is adjusted such that it becomes divisible by 3 while keeping `universals` unchanged. If the condition is not met, `extroverts` remains unchanged.
    return ceil((extroverts + universals) / 3)
    #The program returns the ceiling value of (extroverts + universals) divided by 3, ensuring that if extroverts is not divisible by 3 and extroverts % 3 + universals is greater than or equal to 3, extroverts is adjusted to be divisible by 3 while keeping universals unchanged.
#Overall this is what the function does:The function `func_1` accepts two parameters, `extroverts` and `universals`, both of which are non-negative integers. It returns `None` if `extroverts` is not divisible by 3 and `extroverts % 3 + universals` is less than 3. Otherwise, it returns the ceiling value of `(extroverts + universals)` divided by 3, ensuring that `extroverts` is adjusted to be divisible by 3 while keeping `universals` unchanged.

#State of the program right berfore the function call: introverts, extroverts, and universals are non-negative integers such that 0 <= introverts, extroverts, universals <= 10^9.
def func_2(introverts, extroverts, universals):
    ret = func_1(extroverts, universals)
    return -1 if ret is None else introverts + ret
    #The program returns `introverts` plus the return value of `func_1(extroverts, universals)` if `func_1(extroverts, universals)` does not return `None`; otherwise, it returns `-1`.
#Overall this is what the function does:The function accepts three parameters: `introverts`, `extroverts`, and `universals`. It calls another function `func_1` with `extroverts` and `universals` as arguments. If `func_1` returns a value (not `None`), the function returns the sum of `introverts` and the returned value from `func_1`. If `func_1` returns `None`, the function returns `-1`.

