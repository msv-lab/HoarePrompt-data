#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and the next n inputs are strings consisting of lowercase English letters, where the length of each string is from 1 to 100, inclusive.
def func():
    t = int(raw_input())
    ls = []
    while t > 0:
        a = raw_input()
        
        ls.append(a)
        
        t = t - 1
        
    #State of the program after the loop has been executed: `t` is 0, `ls` contains `t` input strings, `n` is an integer such that 1 ≤ `n` ≤ 100.
    dict1 = {}
    for x in ls:
        count = 0
        
        for z in ls:
            if x in z:
                count = count + 1
        
        dict1[x] = count
        
    #State of the program after the  for loop has been executed: `dict1` is a dictionary where each key is a string from `ls` and each value is the count of how many strings in `ls` contain that key as a substring; `ls` is a list of input strings.
    sorted_x = sorted(dict1.items(), key=operator.itemgetter(1))
    sorted_x.reverse()
    c2 = 0
    for item in sorted_x:
        if item[1] == 1:
            c2 = c2 + 1
        
    #State of the program after the  for loop has been executed: `c2` is the count of tuples in `sorted_x` where the second element equals 1, `sorted_x` is the list of tuples sorted by values from `dict1`, and `dict1` is a dictionary where each key is a substring from `ls` and each value is the count of how many strings in `ls` contain that key as a substring.
    if (c2 > 1) :
        print('NO')
    else :
        print('YES')
        for x in sorted_x:
            c1 = ls.count(x[0])
            
            for z in range(c1):
                print(x[0])
            
        #State of the program after the  for loop has been executed: `c2` is the count of tuples in `sorted_x` where the second element equals 1; `sorted_x` is a list of tuples sorted by values from `dict1`; `ls` remains unchanged; each first element of the tuples in `sorted_x` has been printed `c1` times, where `c1` is the count of that first element in `ls`.
    #State of the program after the if-else block has been executed: *`c2` is the count of tuples in `sorted_x` where the second element equals 1, `sorted_x` is the list of tuples sorted by values from `dict1`, and `dict1` is a dictionary where each key is a substring from `ls` and each value is the count of how many strings in `ls` contain that key as a substring. If `c2` is greater than 1, 'NO' is printed. Otherwise, `ls` remains unchanged, and each first element of the tuples in `sorted_x` has been printed `c1` times, where `c1` is the count of that first element in `ls`.
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 100) followed by `n` strings of lowercase English letters (each string length from 1 to 100). It counts how many times each string appears as a substring in the list of strings. If there is more than one string that appears as a substring in exactly one other string, it prints 'NO'. Otherwise, it prints 'YES' and then prints each string that appeared as a substring the number of times it was counted in the input list. This function does not handle cases where the input might be invalid (e.g., if `n` is not within the specified range or if the strings do not meet the length requirements).

