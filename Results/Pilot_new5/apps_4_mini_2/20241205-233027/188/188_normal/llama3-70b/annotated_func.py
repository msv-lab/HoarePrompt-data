#State of the program right berfore the function call: n is an even integer between 2 and 100, and the next n lines contain integers a_i (1 ≤ a_i ≤ 100) representing the numbers written on the n cards.
def func():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
        
    #State of the program after the  for loop has been executed: `n` is an even integer between 2 and 100, `i` is 99, `a` is a list containing 100 integers input by the user.
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
        
    #State of the program after the  for loop has been executed: `n` is an even integer between 2 and 100, `i` is the last element of `a`, and `a` is a list containing 100 integers input by the user. The dictionary `d` contains the counts of each unique integer in `a`, with keys being the unique integers from `a` and values being their respective counts.
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
        
    #State of the program after the  for loop has been executed: `n` is an even integer between 2 and 100, `a1` is the first key in `d` such that `d[a1]` equals `n // 2` or -1 if no such key exists, `a2` is the second key in `d` such that `d[a2]` equals `n // 2` or -1 if no second such key exists, `c` is either 0, 1, or 2 indicating the count of unique integers in `a` that appeared exactly `n // 2` times, `d` is a dictionary containing counts of each unique integer from `a`.
    if (a1 != -1 and a2 != -1) :
        print('YES')
        print(a1, a2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an even integer between 2 and 100. If both `a1` and `a2` are valid keys in `d` such that `d[a1]` and `d[a2]` equal `n // 2`, the output 'YES' has been printed along with the values of `a1` and `a2`. If either `a1` or `a2` is -1, the output 'NO' has been printed, while `c` indicates the count of unique integers in `a` that appeared exactly `n // 2` times, and `d` remains a dictionary containing counts of each unique integer from `a`.
#Overall this is what the function does:The function accepts an even integer `n` between 2 and 100, followed by `n` integers (each between 1 and 100). It counts the occurrences of each integer and checks if there are exactly two unique integers that appear exactly `n/2` times. If such integers exist, it prints 'YES' along with those integers; otherwise, it prints 'NO'. The function does not handle any input errors or unexpected values, assuming the input adheres strictly to the specified constraints.

