#State of the program right berfore the function call: field is a string consisting of '*' and '.', and i is an integer such that 0 <= i < len(field).
def func_1(field, i):
    for slice_len in xrange(1, len(field) + 1):
        res = field[i::slice_len]
        
        if len(res) == 5 and set(res) == {'*'}:
            return slice_len
        
    #State of the program after the  for loop has been executed: `field` is a string consisting of '*' and '.', `i` is an integer such that `0 <= i < len(field)`, `len(field)` must be at least 1, and `res` is a substring of `field` starting from index `i` with a step size of `slice_len`. If there exists any `slice_len` for which the length of `res` is 5 and the set of characters in `res` is {'*'}, the function returns `slice_len`. If no such `slice_len` exists, the function returns None.
    return 0
    #The program returns 0
#Overall this is what the function does:The function `func_1` accepts two parameters: `field`, which is a string consisting of '*' and '.', and `i`, which is an integer such that `0 <= i < len(field)`. The function iterates over possible step sizes (`slice_len`) from 1 to the length of `field`. For each step size, it extracts a substring `res` from `field` starting at index `i` with the given step size. The function checks if the length of `res` is exactly 5 and if it consists solely of asterisks ('*'). If such a substring is found, the function returns the corresponding step size `slice_len`. If no such substring exists, the function returns 0.

#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100, and field is a string of length n consisting of characters '*' and '.', representing the scheme of the level where '*' is a platform and '.' is a pit.
def func_2():
    n = int(raw_input())
    field = raw_input()
    win = False
    for i in xrange(n):
        if field[i] != '.':
            slice_len = func_1(field, i)
            if slice_len:
                j = i + 4 * slice_len
                if j + slice_len >= n or field[j + slice_len] == '*':
                    win = True
                    break
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100, `field` is a string of length `n` consisting of characters '*' and '.', `win` is `True` if there exists any index `i` (0 ≤ `i` < `n`) such that `field[i]` is not '.', `slice_len` returned by `func_1(field, i)` satisfies `j + slice_len < n` and `field[j + slice_len]` is '*', otherwise `win` remains `False`.
    if win :
        print('yes')
    else :
        print('no')
    #State of the program after the if-else block has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100, `field` is a string of length `n` consisting of characters '*' and '.', `win` is `True` if there exists any index `i` (0 ≤ `i` < `n`) such that `field[i]` is not '.', `slice_len` returned by `func_1(field, i)` satisfies `j + slice_len < n` and `field[j + slice_len]` is '*', otherwise `win` remains `False`. If the win condition is met in the if statement, the program prints 'yes'; otherwise, it prints 'no'.
#Overall this is what the function does:The function `func_2` takes an integer `n` and a string `field` of length `n` consisting of characters `'*'` and `'.'`, representing a level scheme where `'*'` is a platform and `'.'` is a pit. It iterates through each character in `field` and checks if there is a platform (`'*'`) followed by a sequence of pits and platforms (of length `4 * slice_len`) that ends with another platform. If such a sequence is found, it sets `win` to `True`. After the loop, the function prints `'yes'` if `win` is `True`, indicating that a win condition was met, otherwise it prints `'no'`. The function does not return anything explicitly, but the final state of the program includes the variables `n`, `field`, and `win`. If `win` is `True`, it means there is a path from a platform to another platform via a sequence of pits and platforms that can be traversed without falling into a pit. If `win` is `False`, no such path exists.

