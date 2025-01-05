#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100. Each of the n strings consists of lowercase English letters and has a length between 1 and 100, inclusive.**
def func():
    t = int(raw_input())
    ls = []
    while t > 0:
        a = raw_input()
        
        ls.append(a)
        
        t = t - 1
        
    #State of the program after the loop has been executed: `n` is an integer such that 1 ≤ n ≤ 100, each of the n strings consists of lowercase English letters and has a length between 1 and 100, `t` is 0, `ls` contains all the strings entered by the user, `a` is the last string entered by the user
    dict1 = {}
    for x in ls:
        count = 0
        
        for z in ls:
            if x in z:
                count = count + 1
        
        dict1[x] = count
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `ls` contains at least one string, `x` is the last string in `ls`, `a` is the last string in `ls`, `t` is 0, `dict1` is a dictionary with keys as the strings in `ls` and the values as the total count of each string in `ls`, `count` is the total number of strings in `ls` that contain `x`, `z` is the last string in `ls`, `x` is in `z`
    sorted_x = sorted(dict1.items(), key=operator.itemgetter(1))
    sorted_x.reverse()
    c2 = 0
    for item in sorted_x:
        if item[1] == 1:
            c2 = c2 + 1
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `ls` contains at least one string, `x` is the last string in `ls`, `a` is the last string in `ls`, `t` is 0, `dict1` is a dictionary with keys as the strings in `ls` and the values as the total count of each string in `ls`, `count` is the total number of strings in `ls` that contain `x`, `z` is the last string in `ls`, `x` is in `z`, `sorted_x` is not empty and has more items in it, `c2` is the total number of items in `sorted_x` where the value is 1.
    if (c2 > 1) :
        print('NO')
    else :
        print('YES')
        for x in sorted_x:
            c1 = ls.count(x[0])
            
            for z in range(c1):
                print(x[0])
            
        #State of the program after the  for loop has been executed: All elements in list `ls` are printed out based on their counts in `sorted_x`
    #State of the program after the if-else block has been executed: *`n` is greater than 0, `ls` contains at least one string, `x` is the last string in ls, `a` is the last string in ls, `t` is 0, `dict1` is a dictionary with keys as the strings in ls and the values as the total count of each string in ls, `count` is the total number of strings in ls that contain x, `z` is the last string in ls, `x` is in z, `sorted_x` is not empty and has more items in it, `c2` is the total number of items in sorted_x where the value is 1. If c2 is greater than 1, `NO` is printed. Otherwise, all elements in list ls are printed out based on their counts in sorted_x.
#Overall this is what the function does:The function `func` reads an integer `t`, then reads `t` strings of lowercase English letters. It then creates a dictionary where each string is a key and the value is the total count of that string in the list. It checks if there is only one unique count in the dictionary and prints 'YES' if true, or 'NO' if false. If 'YES' is printed, it then prints out the strings based on their counts in descending order. The function does not explicitly return any value.

