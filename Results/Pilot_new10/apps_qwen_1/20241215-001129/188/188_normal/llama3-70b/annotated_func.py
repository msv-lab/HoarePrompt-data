#State of the program right berfore the function call: n is an even number of integers, written on n cards, where 2 ≤ n ≤ 100 and each integer is in the range 1 ≤ a_i ≤ 100.
def func():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
        
    #State of the program after the  for loop has been executed: `n` is an even number between 2 and 100 (inclusive), `a` is a list containing `n` elements, each element is an integer input, `i` is `n`.
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
        
    #State of the program after the  for loop has been executed: `n` is an even number between 2 and 100, `a` is a list containing `n` elements, each element is an integer, `d` is a dictionary where each key is an element from `a` and the corresponding value is the frequency of that element in `a`.
    c = 0
    a1, a2 = -1, -1
    for i in d:
        if d[i] == n // 2:
            if c == 0:
                a1 = i
                c += 1
            else:
                a2 = i
                break
        
    #State of the program after the  for loop has been executed: `n` is an even number between 2 and 100, `a` is a list containing `n` elements, each element is an integer, `d` is a dictionary where each key is an element from `a` and the corresponding value is the frequency of that element in `a`, `c` is either 0, 1, or 2, `a1` is either -1 or the key `i` from `d` such that `d[i]` is equal to `n // 2`, `a2` is either -1 or equal to `i`.
    if (a1 != -1 and a2 != -1) :
        print('YES')
        print(a1, a2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an even number between 2 and 100, `a` is a list containing `n` elements, each element is an integer, `d` is a dictionary where each key is an element from `a` and the corresponding value is the frequency of that element in `a`, `c` is either 0, 1, or 2, `a1` is either -1 or the key `i` from `d` such that `d[i]` is equal to `n // 2`, `a2` is either -1 or equal to `i`. The output is the printed values of `a1` and `a2` if `a1` and `a2` are not -1. If `a1` and `a2` are -1, the program simply continues without printing anything.
#Overall this is what the function does:The function processes a set of integers written on `n` cards, where `n` is an even number and each integer is in the range 1 ≤ a_i ≤ 100. It creates a dictionary to count the frequency of each integer in the list. Then, it checks if there are two distinct integers in the list that each appear exactly `n // 2` times. If such integers exist, it prints "YES" followed by the two integers; otherwise, it prints "NO".

