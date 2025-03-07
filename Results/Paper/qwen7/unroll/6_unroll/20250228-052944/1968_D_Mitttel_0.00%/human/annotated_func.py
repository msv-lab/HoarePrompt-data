#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2⋅10^5, k is an integer such that 1 ≤ k ≤ 10^9, PB and PS are integers such that 1 ≤ PB, PS ≤ n, and p is a list of n integers representing a permutation, and a is a list of n integers where 1 ≤ a[i] ≤ 10^9 for all 0 ≤ i < n.
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
#Overall this is what the function does:The function accepts parameters n, k, PB, PS, p, and a. It calculates scores for PB and PS based on the elements in the lists p and a. Depending on which score is higher, it returns either 'Bodya', 'Sasha', or 'Draw'. After the function concludes, it will have returned one of these three strings indicating the comparison result.

