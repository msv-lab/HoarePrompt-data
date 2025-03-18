#State of the program right berfore the function call: This is an interactive problem involving a secret permutation \( p_0, p_1, \ldots, p_{n-1} \) of \( \{0, 1, \ldots, n-1\} \). You can ask up to 3n queries of the form "? a b c d" to compare the bitwise OR of pairs of elements in the permutation. After finding a pair of indices \( i \) and \( j \) such that \( p_i \oplus p_j \) is maximized, you must print "! i j".
def func():
    for _ in range(int(input())):
        n = int(input())
        
        maxi = 0
        
        for i in range(1, n):
            print('?', maxi, maxi, i, i, flush=True)
            res = input()
            if res == '<':
                maxi = i
        
        arr = [0]
        
        for i in range(1, n):
            print('?', maxi, arr[0], maxi, i, flush=True)
            res = input()
            if res == '<':
                arr = [i]
            elif res == '=':
                arr.append(i)
        
        mini = arr[0]
        
        for item in arr[1:]:
            print('?', mini, mini, item, item, flush=True)
            res = input()
            if res == '>':
                mini = item
        
        print('!', maxi, mini, flush=True)
        
    #State: Output State: The output state is the pair of indices (maxi, mini) that are printed after all the iterations of the loop have finished. These indices represent the pair of elements in the secret permutation \( p \) such that the bitwise XOR of these two elements is maximized.
#Overall this is what the function does:The function interacts with a secret permutation \( p_0, p_1, \ldots, p_{n-1} \) of \( \{0, 1, \ldots, n-1\} \) by making up to 3n queries to compare the bitwise OR of pairs of elements. It identifies a pair of indices \( i \) and \( j \) where the bitwise XOR \( p_i \oplus p_j \) is maximized and prints the indices "! i j".

