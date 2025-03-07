#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 2 ≤ n ≤ 10^4. Additionally, the sequence p_0, p_1, ..., p_{n-1} is a permutation of {0, 1, ..., n-1}.
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
        
    #State: The loop has executed all its iterations, meaning `maxi` is the maximum value in the permutation `p_0, p_1, ..., p_{n-1}`, and `mini` is the minimum value in the same permutation.
#Overall this is what the function does:The function processes a sequence \( p_0, p_1, \ldots, p_{n-1} \) which is a permutation of \{0, 1, \ldots, n-1\}, where \( n \) is an integer such that \( 2 \leq n \leq 10^4 \). For each test case, it determines the maximum and minimum values in the sequence. After processing all test cases, it prints the maximum and minimum values found for each sequence.

