#State of the program right berfore the function call: s is a string consisting of lowercase English letters.**
def func():
    a = raw_input()
    b = []
    for k in range(len(a)):
        b.append(a[k])
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase English letters, `a` is a non-empty string, `b` contains all characters of string `a` in order, `k` is equal to the length of string `a`
    b = np.array(b)
    alp = 'abcdefghijklmnopqrstuvwxyz'
    al = []
    for k in range(len(alp)):
        al.append(alp[k])
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase English letters, `a` is a non-empty string, `b` contains all characters of string `a` in order, `k` is 25, `b` is a numpy array, `alp` is assigned the string 'abcdefghijklmnopqrstuvwxyz', `al` contains all lowercase English letters from 'a' to 'z'
    res = []
    for aa in al:
        if aa in b:
            res.append(np.where(b == aa))
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase English letters, `a` is a non-empty string, `b` contains all characters of string `a` in order, `k` is 25, `b` is a numpy array, `alp` is assigned the string 'abcdefghijklmnopqrstuvwxyz', `al` is a list of lowercase English letters, `res` is a list containing the indices where the elements in array `b` are equal to each character in `al`, `aa` is the last element in the list `al`.
    m = []
    for k in range(len(res)):
        zz = np.hstack([np.array([0]), res[k][0], np.array([len(a)])])
        
        z = np.diff(zz)
        
        if len(z) > 0:
            m.append(np.max(z))
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase English letters, `a` is a non-empty string, `b` contains all characters of string `a` in order, `k` is 25, `b` is a numpy array, `alp` is assigned the string 'abcdefghijklmnopqrstuvwxyz', `al` is a list of lowercase English letters, `res` is a list containing the indices where the elements in array `b` are equal to each character in `al`, `aa` is the last element in the list `al`, `m` is a list containing the maximum values of the arrays `z` calculated in each iteration of the loop. If the length of array `z` is greater than 0 in any iteration, its maximum value is appended to `m`.
    if (len(m) > 0) :
        ans = np.min(m)
    else :
        ans = len(a)
    #State of the program after the if-else block has been executed: *`s` is a string consisting of lowercase English letters, `a` is a non-empty string, `b` contains all characters of string `a` in order, `k` is 25, `b` is a numpy array, `alp` is assigned the string 'abcdefghijklmnopqrstuvwxyz', `al` is a list of lowercase English letters, `res` is a list containing the indices where the elements in array `b` are equal to each character in `al`, `aa` is the last element in the list `al`, `m` is a list containing the maximum values of the arrays `z` calculated in each iteration of the loop. If the length of array `z` is greater than 0 in any iteration, its maximum value is appended to `m`. If the length of `m` is greater than 0, `ans` is assigned the minimum value in the list `m`. If the length of `m` is not greater than 0, `ans` is assigned the length of string `a`.
    ans -= 1
    print(ans)
#Overall this is what the function does:The function reads a string of lowercase English letters, converts it into a numpy array, and performs calculations on it. It then finds the minimum value from the maximum values of arrays calculated in each iteration. Lastly, it prints the result after subtracting 1 from this minimum value. The function does not return any specific value.

