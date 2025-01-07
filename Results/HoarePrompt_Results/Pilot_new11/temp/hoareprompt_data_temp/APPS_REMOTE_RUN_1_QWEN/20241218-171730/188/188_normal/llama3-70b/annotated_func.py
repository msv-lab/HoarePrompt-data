#State of the program right berfore the function call: n is an even number and is an integer between 2 and 100 inclusive. The following n lines contain a sequence of integers a_1, a_2, ..., a_n, where each integer a_i is written on a card and is between 1 and 100 inclusive.
def func():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
        
    #State of the program after the  for loop has been executed: `a` is a list of length `n` containing integers entered via input(), `i` is `n`, `n` is an even number between 2 and 100 inclusive, `total` is undefined.
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
        
    #State of the program after the  for loop has been executed: `a` is a non-empty list of integers, `i` is the last element of `a`, `d` is a dictionary where each key is an integer from `a` and the value is the count of occurrences of that integer in `a`, `total` is undefined, and `n` is an even number between 2 and 100 inclusive.
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
        
    #State of the program after the  for loop has been executed: `d` is a dictionary where each key is an integer from the original list `a` and the value is the count of occurrences of that integer in `a`, `i` is the last integer checked in the dictionary, `n` is an even number between 2 and 100 inclusive, `c` is 0, 1, or 2, `a1` is either -1 or the first integer `i` such that `d[i] == n // 2`, and `a2` is either -1 or the second integer `i` such that `d[i] == n // 2`.
    if (a1 != -1 and a2 != -1) :
        print('YES')
        print(a1, a2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`d` is a dictionary where each key is an integer from the original list `a` and the value is the count of occurrences of that integer in `a`, `i` is the last integer checked in the dictionary, `n` is an even number between 2 and 100 inclusive, `c` is 0, 1, or 2, `a1` is either -1 or the first integer `i` such that `d[i] == n // 2`, and `a2` is either -1 or the second integer `i` such that `d[i] == n // 2`. If both `a1` and `a2` are not equal to -1, then both `a1` and `a2` are printed; otherwise, 'NO' is printed to the console.
#Overall this is what the function does:The function processes a sequence of \( n \) integers, where \( n \) is an even number between 2 and 100 inclusive, and each integer in the sequence is between 1 and 100 inclusive. It constructs a dictionary to count the occurrences of each integer in the sequence. Then, it checks if there are exactly two distinct integers that each appear \( \frac{n}{2} \) times. If such integers exist, the function prints 'YES' followed by these two integers; otherwise, it prints 'NO'. The function handles edge cases such as when \( n \) is even and no integers appear exactly \( \frac{n}{2} \) times.

