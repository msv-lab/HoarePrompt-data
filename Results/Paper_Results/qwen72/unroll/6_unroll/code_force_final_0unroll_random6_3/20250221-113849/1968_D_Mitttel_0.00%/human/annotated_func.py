#State of the program right berfore the function call: n is a positive integer, k is a positive integer, PB and PS are positive integers such that 1 <= PB, PS <= n, p is a list of n integers representing a permutation of 1 to n, and a is a list of n positive integers.
def func_1(n, k, PB, PS, p, a):
    bodya_score = calculate_score(PB)
    sasha_score = calculate_score(PS)
    if (bodya_score > sasha_score) :
        return 'Bodya'
        #The program returns the string 'Bodya'
    else :
        if (sasha_score > bodya_score) :
            return 'Sasha'
            #The program returns the string 'Sasha'.
        else :
            return 'Draw'
            #The program returns 'Draw'
#Overall this is what the function does:The function `func_1` takes in parameters `n`, `k`, `PB`, `PS`, `p`, and `a`. It calculates the scores for two players, Bodya and Sasha, using the `calculate_score` function with their respective positions `PB` and `PS`. The function returns 'Bodya' if Bodya's score is greater than Sasha's score, 'Sasha' if Sasha's score is greater than Bodya's score, and 'Draw' if both scores are equal. The function does not modify the input parameters.

