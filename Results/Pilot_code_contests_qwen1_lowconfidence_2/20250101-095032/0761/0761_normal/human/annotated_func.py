#State of the program right berfore the function call: k is an integer such that 2 ≤ k ≤ 2 ⋅ 10^5. For each i from 1 to k, n_i is an integer such that 1 ≤ n_i < 2 ⋅ 10^5, and the sequences are lists of n_i integers where each integer is in the range from -10^4 to 10^4. The sum of the lengths of all sequences does not exceed 2 ⋅ 10^5, i.e., n_1 + n_2 + ... + n_k ≤ 2 ⋅ 10^5.
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
        
    #State of the program after the  for loop has been executed: `tk` is a dictionary with keys `i - s` mapping to lists of tuples `(l, arr.index(i) + 1)`, `i` is the last unique element `i` that was processed, `s` is the sum of the elements in the updated `arr`, `arr` is the list of integers provided by the input, `jam` is `[arr]`, `flag` is 0, `ni` is the input integer, `sk` is the list of unique elements from `arr`, `l` is `k`, `s` is the sum of the elements in the updated `arr`. If the loop finds a valid pair, `tk[i - s]` contains more than one element, otherwise, `tk[i - s]` contains at most one element.
    if (not flag) :
        print('NO')
    #State of the program after the if block has been executed: *`tk` is a dictionary with keys `i - s` mapping to lists of tuples `(l, arr.index(i) + 1)`. If the condition `not flag` is true (which means the loop did not find a valid pair), `tk[i - s]` contains at most one element. Otherwise, `tk[i - s]` contains more than one element. `i` is the last unique element `i` that was processed, `s` is the sum of the elements in the updated `arr`, `arr` is the list of integers provided by the input, `jam` is `[arr]`, `flag` remains 0, `ni` is the input integer, `sk` is the list of unique elements from `arr`, `l` is `k`, `s` is the sum of the elements in the updated `arr`.
#Overall this is what the function does:The function processes `k` sequences of integers, where each sequence is defined by an integer `ni` and a list of `ni` integers. It aims to find two elements from different sequences such that their sums are equal. If such a pair is found, it prints "YES" along with the indices of these elements from their respective sequences and exits. If no such pair is found, it prints "NO". The function reads `k` from the input, followed by `ni` and the sequence of integers for each of the `k` sequences. It uses a dictionary `tk` to store pairs of indices and values that could potentially form the required sum.

