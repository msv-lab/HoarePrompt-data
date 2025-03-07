#State of the program right berfore the function call: a is a list of n distinct integers representing the Cowdeforces ratings of the cows, and k is an integer such that 1 <= k <= n, where n is the length of the list a.
def func_1(a):
    x = a[k]
    ind = []
    c = 0
    for i in range(n):
        if a[i] > x:
            ind.append(i)
            c += 1
        
        if c == 2:
            break
        
    #State: Output State: `ind` is a list containing at most two indices where the elements in `a` are greater than `x`, `a` remains a list of n distinct integers representing the Cowdeforces ratings of the cows, `k` remains an integer such that 1 <= k <= n, `x` remains the k-th element of the list `a`, `c` is either 0 or 2.
    if (k == 14) :
        print(ind)
        #This is printed: [indices where elements in a are greater than x]
    #State: Postcondition: `ind` is a list containing at most two indices where the elements in `a` are greater than `x`, `a` remains a list of n distinct integers representing the Cowdeforces ratings of the cows, `k` is 14, `x` remains the 14th element of the list `a`, and `c` is either 0 or 2.
    if (ind == []) :
        return n - 1
        #The program returns n - 1
    #State: Postcondition: `ind` is a list containing at most two indices where the elements in `a` are greater than `x`, `a` remains a list of `n` distinct integers representing the Cowdeforces ratings of the cows, `k` is 14, `x` remains the 14th element of the list `a`, and `c` is either 0 or 2. Additionally, `ind` is not an empty list.
    if (len(ind) == 1) :
        if (ind[0] == 0) :
            return k - 1
            #The program returns 13
        #State: Postcondition: `ind` is a list containing exactly one index where the elements in `a` are greater than `x`, `a` remains a list of `n` distinct integers representing the Cowdeforces ratings of the cows, `k` is 14, the current value of `x` is the 14th element of the list `a`, and `c` is either 0 or 2. Additionally, `ind` is not an empty list, and `ind[0]` is not equal to 0.
        if (ind[0] > k) :
            return ind[0] - 1
            #The program returns a value which is `ind[0] - 1`. Given that `ind` is a list containing exactly one index where the elements in `a` are greater than `x`, and `ind[0]` is greater than 14, the returned value will be an integer that is 1 less than the index stored in `ind[0]`.
        #State: Postcondition: `ind` is a list containing exactly one index where the elements in `a` are greater than `x`, `a` remains a list of `n` distinct integers representing the Cowdeforces ratings of the cows, `k` is 14, the current value of `x` is the 14th element of the list `a`, and `c` is either 0 or 2. Additionally, `ind` is not an empty list, and `ind[0]` is less than or equal to 14.
        return max(k - ind[0], ind[0] - 1)
        #The program returns 14 - ind[0]
    #State: Postcondition: `ind` is a list containing at most two indices where the elements in `a` are greater than `x`, `a` remains a list of `n` distinct integers representing the Cowdeforces ratings of the cows, `k` is 14, `x` remains the 14th element of the list `a`, and `c` is either 0 or 2. Additionally, `ind` contains exactly two elements.
    if (ind[0] == 0) :
        return min(ind[1] - 1, k - 1)
        #The program returns the minimum value between the second element of list ind minus 1 and 13 (since k is 14)
    #State: Postcondition: `ind` is a list containing at most two indices where the elements in `a` are greater than `x`, `a` remains a list of `n` distinct integers representing the Cowdeforces ratings of the cows, `k` is 14, `x` remains the 14th element of the list `a`, and `c` is either 0 or 2. Additionally, `ind` contains exactly two elements, and the first element of `ind` is not 0.
    if (k > ind[1]) :
        return max(ind[0] - 1, ind[1] - ind[0])
        #The program returns the maximum value between (ind[0] - 1) and (ind[1] - ind[0]), where ind[0] is not 0 and both ind[0] and ind[1] are indices in the list a.
    #State: Postcondition: `ind` is a list containing at most two indices where the elements in `a` are greater than `x`, `a` remains a list of `n` distinct integers representing the Cowdeforces ratings of the cows, `k` is 14, `x` remains the 14th element of the list `a`, and `c` is either 0 or 2. Additionally, `ind` contains exactly two elements, and the first element of `ind` is not 0, and `k` is less than or equal to `ind[1]`.
    return max(ind[0] - 1, k - ind[0])
    #The program returns the maximum value between (ind[0] - 1) and (14 - ind[0]) where ind[0] is the first element of the list ind.
#Overall this is what the function does:The function accepts a list `a` of `n` distinct integers representing the Cowdeforces ratings of the cows, and an integer `k` such that 1 <= k <= n. It identifies indices in the list `a` where elements are greater than the `k`-th element of the list. Based on the number of such indices and their positions, it returns one of seven possible values: `n - 1`, `13`, `ind[0] - 1`, `14 - ind[0]`, the minimum value between `ind[1] - 1` and `13`, or the maximum of `ind[0] - 1` and either `ind[1] - ind[0]` or `14 - ind[0]`.

