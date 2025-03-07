#State of the program right berfore the function call: n is a positive integer, k is a positive integer, PB and PS are integers such that 1 <= PB, PS <= n, p is a list of integers of length n where each element is between 1 and n, a is a list of integers of length n where each element is a positive integer.
def func_1(n, k, PB, PS, p, a):
    bodya_score = calculate_score(PB)
    sasha_score = calculate_score(PS)
    if (bodya_score > sasha_score) :
        return 'Bodya'
        #The program returns 'Bodya'
    else :
        if (sasha_score > bodya_score) :
            return 'Sasha'
            #The program returns 'Sasha'
        else :
            return 'Draw'
            #The program returns 'Draw'
#Overall this is what the function does:The function `func_1` compares the scores of two players, Bodya and Sasha, based on their positions `PB` and `PS` in a list `p` and returns 'Bodya' if Bodya's score is higher, 'Sasha' if Sasha's score is higher, or 'Draw' if their scores are equal.

