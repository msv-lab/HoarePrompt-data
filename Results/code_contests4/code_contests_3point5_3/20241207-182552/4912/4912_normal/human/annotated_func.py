#State of the program right berfore the function call: S is a string consisting of uppercase English letters with a length between 9 and 50 inclusive, and S ends with the word "FESTIVAL".**
def func():
    n = int(input())
    s = input()
    res = []
    count = 0
    if (s[0] == '1') :
        one = 1
    else :
        one = 0
    #State of the program after the if-else block has been executed: *S is a string consisting of uppercase English letters with a length between 9 and 50 inclusive, and S ends with the word "FESTIVAL"; n is an input integer; res is an empty list; count is 0. If the first character of S is '1', then one is assigned the value 1. If the first character of S is not '1', then one is assigned the value 0.
    temp = []
    tar = 0
    for i in range(1, n - 1):
        if s[i - 1:i + 2] == '101':
            tar = 1
            temp.append(one)
            one = 0
        else:
            if s[i] == '0' and tar == 1:
                temp.append(one)
                res.append(temp.copy())
                temp = []
                tar = 0
            if s[i] == '1':
                one += 1
            else:
                one = 0
        
    #State of the program after the  for loop has been executed: S is a string consisting of uppercase English letters with a length between 9 and 50 inclusive, ending with "FESTIVAL"; n is an integer greater than or equal to 2; res is a list with elements containing the updated value of one; count is 0; one is either 0 or a positive integer based on the occurrences of '101' and '0' in the string S; temp is a list containing the updated value of one after appending; tar is 0.
    if (s[-1] == '1') :
        one += 1
    #State of the program after the if block has been executed: *S is a string consisting of uppercase English letters with a length between 9 and 50 inclusive, ending with "FESTIVAL"; n is an integer greater than or equal to 2; res is a list with elements containing the updated value of one; count is 0; one is either 1 or a positive integer based on the occurrences of '101' and '0' in the string S; temp is a list containing the updated value of one after appending; tar is 0; the last character of S is '1'.
    if (tar == 1) :
        temp.append(one)
        res.append(temp.copy())
    #State of the program after the if block has been executed: *S is a string consisting of uppercase English letters with a length between 9 and 50 inclusive, ending with "FESTIVAL"; n is an integer greater than or equal to 2; res is a list with elements containing the updated value of one; count is 0; one is either 1 or a positive integer based on the occurrences of '101' and '0' in the string S; temp is a list containing the updated value of one after appending; tar is 0; the last character of S is '1'; if tar is equal to 1, then temp has the updated value of one after appending and res contains a copy of temp.
    for x in res:
        temp = 0
        
        m = len(x)
        
        f = []
        
        if m == 2:
            temp = max(x[0], x[1])
        
        if m == 3:
            temp = max(x[0], x[1], x[2])
        
        if m == 4:
            temp = max(x[0] + x[2], x[3] + max(x[0], x[1]))
        
        if m >= 5:
            f.append([x[0], x[1]])
            f.append([x[1], max(x[2], x[0])])
            f.append(x[0] + x[2], x[3] + f[0])
            for i in range(3, m - 1):
                f.append(x[i] + max(f[i - 2][0], f[i - 3][0]))
                f.append(x[i + 1] + max(f[i - 2][0], f[i - 2][1]))
            temp = max(f[-1][0], f[-1][1], f[-2][0])
        
        count += temp
        
    #State of the program after the  for loop has been executed: After the loop finishes executing, `count` will contain the sum of all the `temp` values calculated during each iteration of the loop. All other variables will retain their initial values as specified in the initial state.
    print(count)
#Overall this is what the function does:The function `func` takes user input for an integer `n` and a string `s`, then processes the string based on certain conditions. It extracts specific sequences from the input string `s`, calculates values based on these sequences, and ultimately prints the sum of these calculated values. The function assumes that the input string `s` consists of uppercase English letters with a length between 9 and 50 inclusive, and ends with the word "FESTIVAL". The processing of the string involves identifying patterns and updating values accordingly to derive the final sum printed at the end.

