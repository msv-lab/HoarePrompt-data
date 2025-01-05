#State of the program right berfore the function call: s is a string consisting of lowercase English letters.**
def func():
    a = raw_input()
    b = []
    for k in range(len(a)):
        b.append(a[k])
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase English letters, `a` is a string of length at least 1, `b` contains all characters of string `a` in order, `k` is equal to the length of string `a`
    b = np.array(b)
    alp = 'abcdefghijklmnopqrstuvwxyz'
    al = []
    for k in range(len(alp)):
        al.append(alp[k])
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase English letters, `a` is a string of length at least 1, `b` contains all characters of string `a` in order, `k` is equal to the length of string `alp`, `b` is now converted to a NumPy array, `alp` is a string containing all lowercase English letters, `al` contains all lowercase English letters
    res = []
    for aa in al:
        if aa in b:
            res.append(np.where(b == aa))
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase English letters, `a` is a string of length at least 1, `b` contains all characters of string `a` in order and is now a NumPy array, `k` is equal to the length of string `alp`, `alp` is a string containing all lowercase English letters, `al` contains all lowercase English letters, `res` contains the indices where each lowercase English letter in `al` is present in the NumPy array `b` after all iterations of the loop have executed.
    m = []
    for k in range(len(res)):
        zz = np.hstack([np.array([0]), res[k][0], np.array([len(a)])])
        
        z = np.diff(zz)
        
        if len(z) > 0:
            m.append(np.max(z))
        
    #State of the program after the  for loop has been executed: If the length of `res` is greater than 0, then `m` will contain the maximum value of `z` for each element in `res` that satisfies the condition. Otherwise, `m` will remain an empty list. Rest of the variables retain their initial values.
    if (len(m) > 0) :
        ans = np.min(m)
    else :
        ans = len(a)
    #State of the program after the if-else block has been executed: *If the length of `res` is greater than 0, then `m` will contain the maximum value of `z` for each element in `res` that satisfies the condition. `m` is a list containing the maximum value of `z` for each element in `res` that satisfies the condition. `ans` is either the minimum value of `m` or 0 if `m` is empty. Otherwise, if the length of `res` is not greater than 0, then `m` will remain an empty list. `z` will have the maximum value for each element in `res` that satisfies the condition. Rest of the variables retain their initial values.
    ans -= 1
    print(ans)
#Overall this is what the function does:The function operates on a string 's' consisting of lowercase English letters. It converts the string 's' into a NumPy array 'b'. It then iterates through all lowercase English letters, checks their presence in 'b', and stores the indices where each letter is found in 'res'. After that, it calculates the maximum consecutive occurrences of each letter in 'res' and stores the maximum values in 'm'. Finally, it determines the minimum value in 'm' and subtracts 1 from it, printing the result.

