#State of the program right berfore the function call: a is a list of non-negative integers representing the initial number of stones in each pile, and the length of the list (n) satisfies 1 <= n <= 2 * 10^5.
def func_1(a):
    a_new = sorted(list(set(a)))
    a_temp = a_new.copy()
    for i in range(1, len(a_new)):
        a_new[i] = a_new[i] - a_temp[i - 1]
        
    #State: Output State: The final state of `a_new` will be such that each element `a_new[i]` (for `i` starting from 1) has been decremented by the sum of all preceding elements in `a_temp` up to `a_temp[i-1]`. All other variables (`a`, `a_temp`, and `i`) will be as follows: `i` will be equal to `len(a_new)`, `a` and `a_temp` will retain their initial values but modified according to the loop's effect, and `a_new` will contain the updated values as described.
    #
    #In simpler terms, after the loop completes all its iterations, each element in `a_new` (starting from the second element) will have subtracted from it the cumulative sum of all previous elements in `a_temp`. The variable `i` will be equal to the length of `a_new`, indicating that the loop has processed all elements. The initial lists `a` and `a_temp` will still exist but will reflect the changes made during the loop's execution on `a_new`.
    return a_new
    #a_new is a list where each element a_new[i] (for i starting from 1) has been decremented by the sum of all preceding elements in a_temp up to a_temp[i-1], i is equal to the length of a_new, a and a_temp retain their initial values but modified according to the loop's effect, and a_new contains the updated values as described.
#Overall this is what the function does:The function `func_1` accepts a list `a` of non-negative integers and returns a new list `a_new`. Each element `a_new[i]` (for i starting from 1) is decremented by the sum of all preceding elements in `a` up to `a[i-1]`. After the function executes, `a_new` contains the updated values, while `a` retains its initial values but is modified according to the loop's effect. The variable `i` equals the length of `a_new`, indicating that the loop has processed all elements.

#State of the program right berfore the function call: a is a list of n integers representing the initial number of stones in each pile, and n is a positive integer such that 1 <= n <= 2 * 10^5. Each integer in the list a is a positive integer not exceeding 10^9.
def func_2(a, n):
    if (n == 1) :
        return 1
        #The program returns 1
    else :
        if (n == 2) :
            if (a[0] % 2 == 0) :
                return 1
                #The program returns 1
            else :
                return 2
                #The program returns 2
        else :
            winNext = func_2(a[1:], n - 1)
            if (winNext == 2 or winNext == 1 and a[0] != 1) :
                return 1
                #The program returns 1
            else :
                return 2
                #The program returns 2
#Overall this is what the function does:The function accepts a list `a` of `n` integers representing the initial number of stones in each pile, and an integer `n` indicating the number of piles. It recursively determines whether the player who starts the game can guarantee a win based on the current configuration of stone piles. If the starting player can guarantee a win, the function returns 1; otherwise, it returns 2.

