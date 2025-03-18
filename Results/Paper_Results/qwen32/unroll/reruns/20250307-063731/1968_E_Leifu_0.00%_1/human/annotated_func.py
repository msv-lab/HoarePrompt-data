#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and for each of the following t lines, n is an integer such that 2 <= n <= 10^3.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        print('1 1')
        
        print('1 2')
        
        if n == 3:
            print('2 3')
        else:
            print('2 4')
            for j in range(4, n + 1):
                print(str(j) + ' ' + str(j))
        
    #State: A series of printed pairs for each input `n`, where the pairs are determined by the logic described in the code. No changes to the initial state variables `t` and `n`.
#Overall this is what the function does:The function processes a series of integers `n` (where `2 <= n <= 1000`), each provided after an initial integer `t` (where `1 <= t <= 50`). For each `n`, it prints a specific sequence of pairs of integers. The sequence starts with '1 1' and '1 2'. If `n` is 3, it prints '2 3'. Otherwise, it prints '2 4' followed by pairs of the form 'j j' for each `j` from 4 to `n`.

