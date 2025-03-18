#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2 × 10^5, k is an integer such that 1 ≤ k ≤ 10^9, PB and PS are integers such that 1 ≤ PB, PS ≤ n, and p is a list of n integers representing the permutation, where each integer is unique and within the range 1 to n, and a is a list of n integers where each integer is within the range 1 to 10^9.
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
#Overall this is what the function does:The function accepts parameters n, k, PB, PS, p, and a. It calculates scores for two individuals, Bodya and Sasha, based on their positions PB and PS in the permutation list p. If Bodya's score is higher, the function returns 'Bodya'. If Sasha's score is higher, the function returns 'Sasha'. If both scores are equal, the function returns 'Draw'.

