#State of the program right berfore the function call: n is a positive integer, k is a positive integer, PB and PS are integers such that 1 <= PB <= n and 1 <= PS <= n, p is a list of integers representing a permutation of length n, and a is a list of positive integers of length n.
def func_1(n, k, PB, PS, p, a):
    bodya_score = calculate_score(PB)
    sasha_score = calculate_score(PS)
    if (bodya_score > sasha_score) :
        return 'Bodya'
        #The program returns the string 'Bodya'.
    else :
        if (sasha_score > bodya_score) :
            return 'Sasha'
            #The program returns the string 'Sasha'.
        else :
            return 'Draw'
            #The program returns the string 'Draw'.
#Overall this is what the function does:The function `func_1` takes in parameters `n`, `k`, `PB`, `PS`, `p`, and `a`. It calculates the scores for two players, Bodya and Sasha, based on their respective positions `PB` and `PS` in the permutation `p`. The function returns 'Bodya' if Bodya's score is greater than Sasha's score, 'Sasha' if Sasha's score is greater than Bodya's score, and 'Draw' if both scores are equal. The function does not modify any of its input parameters.

