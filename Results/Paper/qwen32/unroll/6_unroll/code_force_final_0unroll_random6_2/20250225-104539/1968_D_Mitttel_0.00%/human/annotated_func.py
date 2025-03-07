#State of the program right berfore the function call: n is a positive integer representing the length of the permutation and array a, k is a positive integer representing the duration of the game, PB and PS are positive integers representing Bodya's and Sasha's starting positions respectively, such that 1 <= PB, PS <= n. p is a list of n integers representing the permutation, and a is a list of n integers representing the array a.
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
#Overall this is what the function does:The function determines the winner of a game between Bodya and Sasha based on their starting positions and the scores calculated from a permutation and an array. It returns 'Bodya' if Bodya has a higher score, 'Sasha' if Sasha has a higher score, and 'Draw' if both have the same score. The duration of the game `k` is provided but not used in the decision-making process.

