#State of the program right berfore the function call: s is a string of lowercase English letters with a length between 1 and 100.
def func():
    a = raw_input()
    b = []
    for k in range(len(a)):
        b.append(a[k])
        
    #State of the program after the  for loop has been executed: `s` is a string of lowercase English letters with a length between 1 and 100; `a` is a non-empty string from raw_input(); `b` contains all characters of `a`; `k` is equal to the length of `a`.
    b = np.array(b)
    alp = 'abcdefghijklmnopqrstuvwxyz'
    al = []
    for k in range(len(alp)):
        al.append(alp[k])
        
    #State of the program after the  for loop has been executed: `s` is a string of lowercase English letters with a length between 1 and 100; `a` is a non-empty string from raw_input(); `b` is now a numpy array containing all characters of `a`; `k` is 26; `alp` is 'abcdefghijklmnopqrstuvwxyz'; `al` is now ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'].
    res = []
    for aa in al:
        if aa in b:
            res.append(np.where(b == aa))
        
    #State of the program after the  for loop has been executed: `s` is a string of lowercase English letters with a length between 1 and 100, `a` is a non-empty string, `b` is a numpy array containing all characters of `a`, `k` is 26, `alp` is 'abcdefghijklmnopqrstuvwxyz', `al` is now ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], and `res` contains the indices of all characters in `al` that are present in `b`.
    m = []
    for k in range(len(res)):
        zz = np.hstack([np.array([0]), res[k][0], np.array([len(a)])])
        
        z = np.diff(zz)
        
        if len(z) > 0:
            m.append(np.max(z))
        
    #State of the program after the  for loop has been executed: `s` is a string of lowercase English letters, `a` is a non-empty string, `b` is a numpy array containing all characters of `a`, `res` contains indices of characters in `al` that are present in `b`, `m` contains the maximum values of the differences calculated from the `zz` arrays formed during each iteration, and if `len(res)` is 0, `m` remains an empty list.
    if (len(m) > 0) :
        ans = np.min(m)
    else :
        ans = len(a)
    #State of the program after the if-else block has been executed: *`s` is a string of lowercase English letters, `a` is a non-empty string, `b` is a numpy array containing all characters of `a`, `res` contains indices of characters in `a` that are present in `b`, if `m` contains maximum values of differences calculated from `zz` arrays, then `ans` is the minimum value from `m`. Otherwise, `m` is an empty list and `ans` is the length of `a`.
    ans -= 1
    print(ans)
#Overall this is what the function does:The function accepts a string `s` of lowercase English letters with a length between 1 and 100, processes the characters to find the maximum gap between consecutive characters (based on their first occurrences), and prints the minimum of these gaps decreased by 1. If no characters from the alphabet are found in `s`, it prints the length of `s` minus 1. If `s` consists of the same character or has no gaps, it will return -1.

