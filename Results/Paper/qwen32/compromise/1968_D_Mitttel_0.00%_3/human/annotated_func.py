#State of the program right berfore the function call: n is a positive integer representing the length of the permutation and the array, k is a positive integer representing the duration of the game, PB and PS are positive integers representing the starting positions of Bodya and Sasha respectively, such that 1 <= PB, PS <= n, p is a list of n integers representing the permutation, and a is a list of n integers representing the array.
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
#Overall this is what the function does:The function `func_1` determines the winner of a game between Bodya and Sasha based on their starting positions and scores calculated from a permutation and an array. It returns 'Bodya' if Bodya's score is higher, 'Sasha' if Sasha's score is higher, and 'Draw' if their scores are equal. The parameters `n`, `k`, `PB`, `PS`, `p`, and `a` are used in the calculation, although `k` is not directly utilized in the provided code snippet.

