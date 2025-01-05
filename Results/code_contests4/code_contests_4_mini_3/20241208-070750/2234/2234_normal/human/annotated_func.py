#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and the following n strings consist of lowercase English letters with lengths ranging from 1 to 100, inclusive.
def func():
    t = int(raw_input())
    ls = []
    while t > 0:
        a = raw_input()
        
        ls.append(a)
        
        t = t - 1
        
    #State of the program after the loop has been executed: `t` is 0, `ls` contains the string `a` repeated `n` times, where `n` is the initial value of `t` before the loop started.
    dict1 = {}
    for x in ls:
        count = 0
        
        for z in ls:
            if x in z:
                count = count + 1
        
        dict1[x] = count
        
    #State of the program after the  for loop has been executed: `t` is 0, `ls` is an empty string, `dict1` is an empty dictionary.
    sorted_x = sorted(dict1.items(), key=operator.itemgetter(1))
    sorted_x.reverse()
    c2 = 0
    for item in sorted_x:
        if item[1] == 1:
            c2 = c2 + 1
        
    #State of the program after the  for loop has been executed: `t` is 0, `ls` is an empty string, `dict1` is an empty dictionary, `sorted_x` is a list with at least 0 items, and `c2` is equal to the count of items in `sorted_x` where the second element is 1.
    if (c2 > 1) :
        print('NO')
    else :
        print('YES')
        for x in sorted_x:
            c1 = ls.count(x[0])
            
            for z in range(c1):
                print(x[0])
            
        #State of the program after the  for loop has been executed: `t` is 0, `ls` is an empty string, `dict1` is an empty dictionary, `sorted_x` is a list with at least 0 items, `c2` is equal to the count of items in `sorted_x` where the second element is 1, and `c2` is less than or equal to 1; the output is 'YES'.
    #State of the program after the if-else block has been executed: *`t` is 0, `ls` is an empty string, `dict1` is an empty dictionary, `sorted_x` is a list with at least 0 items, `c2` is equal to the count of items in `sorted_x` where the second element is 1. If `c2` is greater than 1, 'NO' is printed; otherwise, if `c2` is less than or equal to 1, 'YES' is printed.
#Overall this is what the function does:The function reads an integer `t` representing the number of strings to process (where 1 ≤ t ≤ 100) and then reads `t` strings of lowercase English letters. It counts how many times each string appears in the input. If more than one string appears exactly once, it prints 'NO'; otherwise, it prints 'YES' and then prints the strings that appeared in the input according to their counts. The output includes the strings that appear more than once as many times as they appear. If no strings are provided (e.g., if `t` is 0), the function does not handle this case and may produce an error.

