#State of the program right berfore the function call: n is an integer such that 4 ≤ n ≤ 255, and s is a string consisting of characters 'A', 'C', 'G', 'T', and '?'.
def func():
    n = int(input())
    s = input()
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for c in s:
        if c != '?':
            count[c] += 1
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string, `n` is an integer such that 4 ≤ n ≤ 255, `count` is a dictionary where `count['A']`, `count['C']`, `count['G']`, and `count['T']` are non-negative integers, and for every character `c` in the string `s` that is not '?', `count[c]` is incremented by 1.
    avg = n // 4
    for c in 'ACGT':
        count[c] = avg - count[c]
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string, `n` is an integer such that \(4 \leq n \leq 255\), `avg = n // 4\), `count['A']` is `n // 4 - count['A']`, `count['C']` is `n // 4 - count['C']`, `count['G']` is `n // 4 - count['G']`, and `count['T']` is `n // 4 - count['T']`.
    res = ''
    for c in s:
        if c == '?':
            for nc in 'ACGT':
                if count[nc] > 0:
                    res += nc
                    count[nc] -= 1
                    break
        else:
            res += c
        
    #State of the program after the  for loop has been executed: `res` is a string where every '?' in `s` is replaced by one of 'ACGT' such that each nucleotide ('A', 'C', 'G', 'T') is used exactly `n // 4` times, `count['A']`, `count['C']`, `count['G']`, `count['T']` are all 0, and `res` contains all other characters from `s` as they appear.
    if any(count.values()) :
        print('===')
    else :
        print(res)
    #State of the program after the if-else block has been executed: `res` is a string where every '?' in `s` is replaced by one of 'ACGT' such that each nucleotide ('A', 'C', 'G', 'T') is used exactly `n // 4` times, and `count['A']`, `count['C']`, `count['G']`, `count['T']` are all 0. The string `res` contains all other characters from `s` as they appear.
#Overall this is what the function does:The function accepts an integer `n` and a string `s` and replaces all '?' in `s` with 'A', 'C', 'G', or 'T' such that each nucleotide appears exactly `n // 4` times. If this is not possible, it prints '==='; otherwise, it prints the modified string `s`.

