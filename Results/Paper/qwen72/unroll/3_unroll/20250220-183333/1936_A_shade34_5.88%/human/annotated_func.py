#State of the program right berfore the function call: The function operates in an interactive environment where it can make queries to find the maximum XOR of any two elements in a permutation of {0, 1, ..., n-1}. The input n is an integer such that 2 ≤ n ≤ 10^4, and the function can make at most 3n queries. The permutation is fixed and not adaptive during the interaction.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        mak = 0
        
        for i in range(1, n):
            print('?', mak, mak, i, i)
            sys.stdout.flush()
            if str(input()) == '<':
                mak = i
        
        mak2 = mak
        
        pans = []
        
        for i in range(n):
            print('?', mak, mak2, i, mak2)
            sys.stdout.flush()
            s = str(input())
            if s == '<':
                mak = i
                pans = [i]
            elif s == '=':
                pans.append(i)
        
        mak = 0
        
        for i in range(1, len(pans)):
            print('?', pans[mak], pans[mak], pans[i], pans[i])
            sys.stdout.flush()
            if str(input()) == '>':
                mak = i
        
        print('!', mak2, mak)
        
        sys.stdout.flush()
        
    #State: The loop iterates over a series of inputs, and for each input, it determines the maximum XOR of any two elements in a permutation of {0, 1, ..., n-1} and prints the indices of the two elements that achieve this maximum XOR. After all iterations, the variables `mak` and `mak2` will hold the indices of the elements that achieve the maximum XOR for the last input `n`. The list `pans` will contain the indices of the elements that are equal to `mak2` in the last permutation. All other variables will be in their final state as determined by the last iteration of the loop.
#Overall this is what the function does:The function operates in an interactive environment to determine the maximum XOR of any two elements in a fixed permutation of the set {0, 1, ..., n-1}, where `n` is an integer such that 2 ≤ n ≤ 10^4. For each input `n`, the function makes a series of queries to identify the indices of the two elements that achieve this maximum XOR and prints these indices. After processing all inputs, the final state of the program includes the variables `mak` and `mak2` holding the indices of the elements that achieve the maximum XOR for the last input `n`, and the list `pans` containing the indices of the elements that are equal to `mak2` in the last permutation. All other variables will be in their final state as determined by the last iteration of the loop.

