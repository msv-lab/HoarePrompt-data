#State of the program right berfore the function call: **Precondition**: 
- n is an integer such that 1 ≤ n ≤ 100.
- Each of the n strings consists of lowercase English letters.
- The number of letters in each string is from 1 to 100, inclusive.
def func():
    t = int(raw_input())
    ls = []
    while t > 0:
        a = raw_input()
        
        ls.append(a)
        
        t = t - 1
        
    #State of the program after the loop has been executed: n is an integer such that 1 ≤ n ≤ 100, ls contains the values of all `a` inputs from `raw_input()`, `t` is 0
    dict1 = {}
    for x in ls:
        count = 0
        
        for z in ls:
            if x in z:
                count = count + 1
        
        dict1[x] = count
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 100, `t` is 0, `ls` contains the same values as before, `dict1` is a dictionary with key `x` and value `count` where count is the number of times `x` appears in the list `ls`.
    sorted_x = sorted(dict1.items(), key=operator.itemgetter(1))
    sorted_x.reverse()
    c2 = 0
    for item in sorted_x:
        if item[1] == 1:
            c2 = c2 + 1
        
    #State of the program after the  for loop has been executed: c2 is the count of tuples in sorted_x where the second element is equal to 1
    if (c2 > 1) :
        print('NO')
    else :
        print('YES')
        for x in sorted_x:
            c1 = ls.count(x[0])
            
            for z in range(c1):
                print(x[0])
            
        #State of the program after the  for loop has been executed: All elements in each tuple of sorted_x have been printed c1 times, c2 is 0, x is the last element in sorted_x, c1 is the count of the last element of list ls and c1 is greater than 0
    #State of the program after the if-else block has been executed: *c2 is the count of tuples in sorted_x where the second element is equal to 1. If c2 > 1, the code prints 'NO'. Otherwise, all elements in each tuple of sorted_x have been printed c1 times, c2 is 0, x is the last element in sorted_x, c1 is the count of the last element of list ls, and c1 is greater than 0.
#Overall this is what the function does:The function `func` reads an integer `t` from input and then reads `t` strings. It then processes these strings to count the occurrences of each string within the list of strings. After processing, it determines whether there is only one unique occurrence of a string and prints 'YES' if so, 'NO' otherwise. If there are multiple unique occurrences, it prints each string the number of times it appears in the list. The function does not accept any parameters and is meant to handle a list of strings with lowercase English letters, with the number of strings between 1 and 100 inclusive, and each string having a length between 1 and 100 inclusive.

