#State of the program right berfore the function call: **
def func():
    raw_input()
    l = raw_input().split()
    m = 0
    for i in l:
        s = 0
        
        for j in i:
            if j.isupper():
                s += 1
        
        m = max(s, m)
        
    #State of the program after the  for loop has been executed: `m` is the maximum count of uppercase characters in any sublist of `l`, `l` is unchanged, `i` points to the last element in the list `l`, `s` is the total count of uppercase characters in `i`, `j` is the last uppercase character in `i` that the loop iterates over, or None if there are no uppercase characters in `i`
    print(m)
#Overall this is what the function does:The function `func` reads input, splits it into a list, and then iterates over each sublist to count the number of uppercase characters in each sublist. It keeps track of the maximum count of uppercase characters found in any sublist. Finally, it prints out this maximum count. The function does not accept any parameters and does not return any value.

