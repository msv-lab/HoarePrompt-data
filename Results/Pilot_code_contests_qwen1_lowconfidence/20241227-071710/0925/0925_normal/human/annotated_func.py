#State of the program right berfore the function call: The input consists of two integers n and k where 2 ≤ n ≤ 100 and 1 ≤ k ≤ n - 1, and a string of length n containing characters '.', '#', 'G', and 'T' indicating empty cells, obstacles, the grasshopper's starting position, and the insect's position, respectively. It is guaranteed that 'G' and 'T' appear exactly once in the string.
def func():
    l1 = list(map(int, raw_input().split()))
    n, k = l1[0], l1[1]
    l = raw_input()
    mestot = None
    mestok = None
    for i in range(len(l)):
        if l[i] == 'G':
            mestok = i
        
        if l[i] == 'T':
            mestot = i
        
        if mestok != None and mestot != None:
            break
        
    #State of the program after the  for loop has been executed: `n` is the length of the string `l` and must be greater than or equal to 1, `k` is the second element of the list `l1`, `l` is the string input by the user, `mestok` is the index of the first 'G' in `l` (or `None`), `mestot` is the index of the first 'T' in `l` (or `None`).
    fl = True
    if (abs(mestot - mestok) % k == 0) :
        for i in range(mestok, len(l), k):
            if l[i] == '#':
                fl = False
                break
            
        #State of the program after the  for loop has been executed: `n` is greater than 0, `mestok` is a valid index (not `None`), `mestot` is a valid index (not `None`), and the absolute difference between `mestot` and `mestok` is divisible by `k`; `fl` is `False` and `i` is the last valid index processed by the loop, or `fl` is `True` and the loop did not execute.
        if (fl != False and mestot < mestok) :
            l = l[::-1]
            for i in range(len(l)):
                if l[i] == 'G':
                    mestok = i
                
                if l[i] == 'T':
                    mestot = i
                
            #State of the program after the  for loop has been executed: `n` is greater than 0, `mestok` is a valid index, `mestot` is a valid index, the absolute difference between `mestot` and `mestok` is divisible by `k`, `fl` is not `False`, and `mestot` is not less than `mestok`. Additionally, `l` is a reversed list.
            for i in range(mestok, len(l), k):
                if l[i] == '#':
                    fl = False
                    break
                
            #State of the program after the  for loop has been executed: `fl` is `False`, `mestok` is a valid index, `mestot` is a valid index, the absolute difference between `mestot` and `mestok` is divisible by `k`, `mestot` is not less than `mestok`, `l` is a reversed list, `k` is a negative integer, and if any element `l[i]` where `i` ranges from `mestok` to `len(l)` (inclusive) equals `'#'`, `fl` is set to `False` and the loop breaks; otherwise, `fl` remains `False`.
        #State of the program after the if block has been executed: *`n` is greater than 0, `mestok` is a valid index, `mestot` is a valid index, and the absolute difference between `mestot` and `mestok` is divisible by `k`. If `fl` is `False` and `mestot` is not less than `mestok`, `fl` remains `False`. The loop did not execute or all elements `l[i]` where `i` ranges from `mestok` to `len(l)` do not equal `'#'`. If any element `l[i]` equals `'#'`, `fl` is set to `False`.
        if (fl == True) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`n` is greater than 0, `mestok` is a valid index, `mestot` is a valid index, and the absolute difference between `mestot` and `mestok` is divisible by `k`. `fl` is `True` if and only if no element `l[i]` (where `i` ranges from `mestok` to `len(l)`) equals `'#'`. If any such element equals `'#'`, `fl` is set to `False`. Depending on the value of `fl`, either 'YES' is printed to the console or 'NO' is printed.
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is the length of the string `l` and must be greater than or equal to 1, `k` is the second element of the list `l1`, `l` is the string input by the user, `mestok` is the index of the first 'G' in `l` (or `None`), `mestot` is the index of the first 'T' in `l` (or `None`). If the absolute difference between `mestot` and `mestok` is divisible by `k`, `fl` is `True` if and only if no element `l[i]` (where `i` ranges from `mestok` to `len(l)`) equals `'#'`. Otherwise, `fl` is `False`. Depending on the value of `fl`, either 'YES' or 'NO' is printed to the console.
#Overall this is what the function does:The function accepts a string and two integers \( n \) and \( k \). It determines whether the grasshopper ('G') can jump from its initial position to the insect ('T')'s position without encountering any obstacles ('#'), where each jump is of size \( k \). If the grasshopper can reach the insect under these conditions, it prints 'YES'; otherwise, it prints 'NO'. The function checks the following:

1. The input string contains exactly one 'G' and one 'T'.
2. The absolute difference between the indices of 'G' and 'T' is divisible by \( k \).
3. There are no obstacles ('#') between the grasshopper and the insect along the path defined by the jumps of size \( k \).

If the absolute difference between the indices of 'G' and 'T' is not divisible by \( k \), the function immediately prints 'NO'.

The function also handles the case where the string is reversed. If the indices of 'G' and 'T' are such that the absolute difference is divisible by \( k \) and there are no obstacles when the string is reversed, it still prints 'NO' unless the string was not reversed, in which case it prints 'YES'.

