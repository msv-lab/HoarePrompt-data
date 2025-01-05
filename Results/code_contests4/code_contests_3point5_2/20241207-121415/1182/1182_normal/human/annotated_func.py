#State of the program right berfore the function call: s is a string consisting of lowercase English letters.**
def func():
    a = raw_input()
    b = []
    for k in range(len(a)):
        b.append(a[k])
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase English letters, `a` is not empty, `b` is a list containing all elements from list `a`
    b = np.array(b)
    alp = 'abcdefghijklmnopqrstuvwxyz'
    al = []
    for k in range(len(alp)):
        al.append(alp[k])
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase English letters, `a` is not empty, `b` is a numpy array containing all elements from list `a`, `alp` is a string containing all lowercase English letters, `al` is a list containing all elements of `alp`, `k` is equal to `len(alp) - 1`
    res = []
    for aa in al:
        if aa in b:
            res.append(np.where(b == aa))
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase English letters, `a` is not empty, `b` is a numpy array containing all elements from list `a`, `alp` is a string containing all lowercase English letters, `al` is a list containing all elements of `alp` with at least one element, `k` is equal to `len(alp) - 1`, `res` is a list containing the index where each element in `al` is found in `b` using numpy's `where` function.
    m = []
    for k in range(len(res)):
        zz = np.hstack([np.array([0]), res[k][0], np.array([len(a)])])
        
        z = np.diff(zz)
        
        if len(z) > 0:
            m.append(np.max(z))
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase English letters, `a` is not empty, `b` is a numpy array containing all elements from list `a`, `alp` is a string containing all lowercase English letters, `al` is a list containing all elements of `alp` with at least one element, `k` is equal to `len(res) - 1`, `res` is a list containing the index where each element in `al` is found in `b` using numpy's `where` function with at least one element, `m` is a list containing the maximum value of `z` after appending for each iteration of the loop, `zz` is a numpy array containing 0, the first element of `res[k]`, and the length of `a`, `z` is the result of applying numpy's `diff` function on `zz` with a length greater than 0.
    if (len(m) > 0) :
        ans = np.min(m)
    else :
        ans = len(a)
    #State of the program after the if-else block has been executed: *`s` is a string consisting of lowercase English letters, `a` is not empty, `b` is a numpy array containing all elements from list `a`, `alp` is a string containing all lowercase English letters, `al` is a list containing all elements of `alp` with at least one element, `k` is equal to `len(res) - 1`, `res` is a list containing the index where each element in `al` is found in `b` using numpy's `where` function with at least one element, `m` is a list containing the maximum value of `z` after appending for each iteration of the loop, `zz` is a numpy array containing 0, the first element of `res[k]`, and the length of `a`, `z` is the result of applying numpy's `diff` function on `zz` with a length greater than 0. If the length of `m` is greater than 0, `ans` is assigned the minimum value from the list `m`. Otherwise, if the length of `m` is not greater than 0, `ans` is the length of `a`.
    ans -= 1
    print(ans)
#Overall this is what the function does:The function reads a string `s` consisting of lowercase English letters, converts it into a numpy array `b`, finds the indices of each lowercase English letter from 'a' to 'z' in `b`, calculates the maximum consecutive occurrence of each index, and prints the result. The function does not handle any potential errors like invalid input or empty strings.

