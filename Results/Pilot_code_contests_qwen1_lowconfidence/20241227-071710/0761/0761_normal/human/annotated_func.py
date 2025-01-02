#State of the program right berfore the function call: k is an integer such that 2 ≤ k ≤ 2 ⋅ 10^5. Each sequence is represented by two lines: the first line contains an integer n_i (1 ≤ n_i < 2 ⋅ 10^5) indicating the length of the i-th sequence, and the second line contains n_i integers a_{i, 1}, a_{i, 2}, ..., a_{i, n_i} representing the elements of the sequence. The elements of the sequences are integer numbers from -10^4 to 10^4. The sum of the lengths of all given sequences does not exceed 2 ⋅ 10^5.
def func():
    k = int(raw_input())
    tk = dict()
    jam = []
    flag = 0
    for l in range(k):
        ni = int(raw_input())
        
        arr = list(map(int, raw_input().split()))
        
        jam.append(arr)
        
        s = sum(arr)
        
        sk = list(set(arr))
        
        for i in sk:
            tk[i - s] = tk.get(i - s, [])
            tk[i - s].append((l, arr.index(i) + 1))
            if len(tk[i - s]) > 1:
                if jam[tk[i - s][0][0]] != jam[tk[i - s][1][0]]:
                    print('YES')
                    print(str(tk[i - s][0][0] + 1) + ' ' + str(tk[i - s][0][1]))
                    print(str(tk[i - s][1][0] + 1) + ' ' + str(tk[i - s][1][1]))
                    exit(0)
        
    #State of the program after the  for loop has been executed: `k` is an integer input from the user that satisfies \(2 \leq k \leq 2 \cdot 10^5\); `tk` is a dictionary where keys are differences between elements of `sk` and `s`, and values are lists of tuples containing indices `l` and the position of the element in `arr`; `jam` is a list containing the list `arr`; `flag` is 0; `ni` is an input integer; `arr` is a list of integers; `s` is the sum of all elements in the list `arr`; `sk` is a list of unique elements from `arr`.
    if (not flag) :
        print('NO')
    #State of the program after the if block has been executed: *`k` is an integer satisfying \(2 \leq k \leq 2 \cdot 10^5\). `tk` is a dictionary where keys are differences between elements of `sk` and `s`, and values are lists of tuples containing indices `l` and the position of the element in `arr`. `jam` is a list containing the list `arr`. `flag` remains 0. `ni` is an input integer. `arr` is a list of integers. `s` is the sum of all elements in the list `arr`. `sk` is a list of unique elements from `arr`. The program prints "NO".
#Overall this is what the function does:The function processes a series of sequences, each defined by its length and the elements within it. It checks if there exist two distinct sequences such that the sum of one sequence equals the sum of another sequence plus the difference between two elements within those sequences. If such a pair of sequences is found, it prints "YES" along with the indices of the elements in the two sequences that satisfy this condition. If no such pair is found after checking all sequences, it prints "NO". The function does not accept any parameters and does not return any value. Potential edge cases include handling sequences of varying lengths and ensuring the uniqueness of elements within each sequence.

