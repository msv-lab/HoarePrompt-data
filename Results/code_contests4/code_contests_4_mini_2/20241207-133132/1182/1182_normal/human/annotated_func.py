#State of the program right berfore the function call: s is a string consisting of lowercase English letters with a length between 1 and 100.
def func():
    a = raw_input()
    b = []
    for k in range(len(a)):
        b.append(a[k])
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase English letters with a length between 1 and 100; `b` contains all characters of `a`; `k` is equal to the length of `a`.
    b = np.array(b)
    alp = 'abcdefghijklmnopqrstuvwxyz'
    al = []
    for k in range(len(alp)):
        al.append(alp[k])
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase English letters, `b` is now a NumPy array containing all characters of `a`, `k` is equal to 26, `alp` is 'abcdefghijklmnopqrstuvwxyz', `al` is now ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    res = []
    for aa in al:
        if aa in b:
            res.append(np.where(b == aa))
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase English letters, `b` is a NumPy array containing all characters of `s`, `k` is equal to 26, `alp` is 'abcdefghijklmnopqrstuvwxyz', `al` is a list containing all lowercase English letters, `res` is a list of indices of characters from `al` that are present in `b`.
    m = []
    for k in range(len(res)):
        zz = np.hstack([np.array([0]), res[k][0], np.array([len(a)])])
        
        z = np.diff(zz)
        
        if len(z) > 0:
            m.append(np.max(z))
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase English letters; `b` is a NumPy array containing all characters of `s`; `k` is the last index of `res` if `res` is not empty, otherwise it is 0; `alp` is 'abcdefghijklmnopqrstuvwxyz'; `al` is a list containing all lowercase English letters; `res` is a list of indices of characters from `al` that are present in `b`; `m` is a list containing the maximum values of `z` for each iteration if `res` is not empty, otherwise it is empty.
    if (len(m) > 0) :
        ans = np.min(m)
    else :
        ans = len(a)
    #State of the program after the if-else block has been executed: *`s` is a string consisting of lowercase English letters; `b` is a NumPy array containing all characters of `s`; `k` is the last index of `res` if `res` is not empty, otherwise it is 0; `alp` is 'abcdefghijklmnopqrstuvwxyz'; `al` is a list containing all lowercase English letters; `res` is a list of indices of characters from `al` that are present in `b`; if `m` is not empty, `ans` is the minimum value from the list `m`; otherwise, `m` is an empty list and `ans` is the length of `a`.
    ans -= 1
    print(ans)
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase English letters and calculates the minimum distance between occurrences of each letter in the string. It outputs the minimum distance minus one. If no letter is repeated, it outputs the length of the string minus one.

