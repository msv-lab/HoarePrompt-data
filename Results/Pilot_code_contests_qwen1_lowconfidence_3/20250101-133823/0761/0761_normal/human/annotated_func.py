#State of the program right berfore the function call: k is an integer such that 2 ≤ k ≤ 2 ⋅ 10^5. Each sequence is represented as a pair of lines, where the first line contains an integer n_i (1 ≤ n_i < 2 ⋅ 10^5) indicating the length of the i-th sequence, and the second line contains a list of n_i integers a_{i, 1}, a_{i, 2}, ..., a_{i, n_i} representing the elements of the sequence. The elements of the sequences are integers ranging from -10^4 to 10^4. The sum of the lengths of all given sequences does not exceed 2 ⋅ 10^5.
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
        
    #State of the program after the  for loop has been executed: `tk` is a dictionary with keys as unique differences between elements in `sk` and `s`, and values as lists of tuples containing the index of the element in `arr` and its value from `arr` such that there are at least two elements in `arr` whose difference is the key, `jam` is a list of `k` copies of `arr`, `flag` is 0, `l` is `k`, `ni` is the input integer, `arr` is the list of integers from the input string, `s` is the sum of `arr`, `sk` is a list of unique integers from `arr`.
    if (not flag) :
        print('NO')
    #State of the program after the if block has been executed: *`tk` is a dictionary with keys as unique differences between elements in `sk` and `s`, and values as lists of tuples containing the index of the element in `arr` and its value from `arr` such that there are at least two elements in `arr` whose difference is the key, `jam` is a list of `k` copies of `arr`, `flag` is 0, `l` is `k`, `ni` is the input integer, `arr` is the list of integers from the input string, `s` is the sum of `arr`, `sk` is a list of unique integers from `arr`, and the output is 'NO'.
#Overall this is what the function does:The function processes a series of sequences, each defined by a pair of lines: the first line contains an integer \( n_i \) indicating the length of the sequence, and the second line contains \( n_i \) integers. For each sequence, the function calculates the sum of the integers and identifies unique elements. It then checks if there exist two unique elements within the same sequence whose difference equals another element in the sequence. If such a pair is found, the function prints "YES" along with the indices of these elements and exits. If no such pair is found after processing all sequences, the function prints "NO". The function handles up to \( 2 \times 10^5 \) sequences, with each sequence containing up to \( 2 \times 10^5 \) integers, and the integers in each sequence range from \(-10^4\) to \(10^4\).

