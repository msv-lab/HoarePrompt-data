#State of the program right berfore the function call: The input is a list of integers representing the numbers on the cards, with the length of the list being an even number n (2 ≤ n ≤ 100), and each integer in the list is between 1 and 100 inclusive.
def func():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
        
    #State of the program after the  for loop has been executed: `a` is a list containing `n` elements, each element is an integer input from the list of integers representing the numbers on the cards, `n` is an even number between 2 and 100.
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
        
    #State of the program after the  for loop has been executed: `a` is a non-empty list with exactly `n` elements, where `n` is an even number between 2 and 100, `d` is a dictionary where each key is an element from the list `a` and the value is the count of occurrences of that element in `a`.
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
        
    #State of the program after the  for loop has been executed: `a` is a non-empty list with exactly `n` elements, `d` is a non-empty dictionary where each key is an element from the list `a` and the value is the count of occurrences of that element in `a`, `c` is 2, `a1` is the value of `i` from the dictionary `d` where the count of occurrences of `i` in `a` is equal to `n // 2`, and `a2` is the value of the next key from the dictionary `d` where the count of occurrences of `i` in `a` is not equal to `n // 2`.
    if (a1 != -1 and a2 != -1) :
        print('YES')
        print(a1, a2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`a` is a non-empty list with exactly `n` elements, `d` is a non-empty dictionary where each key is an element from the list `a` and the value is the count of occurrences of that element in `a`, `c` is 2. If both `a1` and `a2` are valid (i.e., `a1 != -1` and `a2 != -1`), the program prints `a1 a2`. Otherwise, the program prints 'NO'.
#Overall this is what the function does:The function `func` accepts a list of integers representing the numbers on the cards. The length of the list is an even number \( n \) where \( 2 \leq n \leq 100 \), and each integer in the list is between 1 and 100 inclusive. The function then checks if there are two distinct integers in the list that appear exactly \( \frac{n}{2} \) times. If such integers exist, the function prints "YES" followed by these two integers. Otherwise, it prints "NO".

