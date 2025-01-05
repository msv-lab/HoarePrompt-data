#State of the program right berfore the function call: s is a string consisting of lowercase English letters with a length between 1 and 100.
def func():
    a = raw_input()
    b = []
    for k in range(len(a)):
        b.append(a[k])
        
    #State of the program after the  for loop has been executed: `s` is a string of lowercase English letters, `b` is a list containing all characters of `a`, `a` is a non-empty string, `k` is equal to the length of `a`.
    b = np.array(b)
    alp = 'abcdefghijklmnopqrstuvwxyz'
    al = []
    for k in range(len(alp)):
        al.append(alp[k])
        
    #State of the program after the  for loop has been executed: `s` is a string of lowercase English letters, `b` is a numpy array containing all characters of `a`, `a` is a non-empty string, `k` is 25, `alp` is 'abcdefghijklmnopqrstuvwxyz', `al` is now a list containing all letters from 'a' to 'z'.
    res = []
    for aa in al:
        if aa in b:
            res.append(np.where(b == aa))
        
    #State of the program after the  for loop has been executed: `s` is a string of lowercase English letters, `b` is a numpy array containing all characters of `a`, `a` is a non-empty string, `k` is 25, `alp` is 'abcdefghijklmnopqrstuvwxyz', `al` is a list containing all letters from 'a' to 'z', `res` contains the indices of all letters from 'a' to 'z' that are present in `b`.
    m = []
    for k in range(len(res)):
        zz = np.hstack([np.array([0]), res[k][0], np.array([len(a)])])
        
        z = np.diff(zz)
        
        if len(z) > 0:
            m.append(np.max(z))
        
    #State of the program after the  for loop has been executed: `s` is a string of lowercase English letters, `b` is a numpy array containing characters of `a`, `a` is a non-empty string, `res` contains the indices of letters present in `b`, `m` is a list containing the maximum distances between the indices, and `k` is equal to the length of `res`.
    if (len(m) > 0) :
        ans = np.min(m)
    else :
        ans = len(a)
    #State of the program after the if-else block has been executed: *`s` is a string of lowercase English letters, `b` is a numpy array containing characters of `a`, `a` is a non-empty string, `res` contains the indices of letters present in `b`, and `k` is equal to the length of `res`. If `m` is a non-empty list, then `ans` is assigned the minimum value from the list `m`. Otherwise, if `m` is empty, then `ans` is assigned the length of `a`.
    ans -= 1
    print(ans)
#Overall this is what the function does:The function accepts a string of lowercase English letters, calculates the maximum distance between the occurrences of each letter in the string, and then returns the minimum of these distances minus one. If there are no repeating letters, it returns the length of the string minus one. If the string contains only one character, it returns 0.

