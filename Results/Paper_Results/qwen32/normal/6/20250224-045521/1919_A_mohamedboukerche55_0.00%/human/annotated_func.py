#State of the program right berfore the function call: Each test contains multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases. For each test case, there is one line containing two integers a and b (1 ≤ a, b ≤ 10^9) — the number of coins in Alice's and Bob's wallets, respectively.
def func():
    for i in range(int(input())):
        s = input()
        
        a = int(list(s.split())[0])
        
        b = int(list(s.split())[1])
        
    #State: `t` remains unchanged, `i` is `t - 1`, `s` is the input string of the last test case, `a` is the integer value of the first element in the last test case, and `b` is the integer value of the second element in the last test case.
    #
    #Output State:
    if ((a + b) % 2 == 0) :
        print('bob  ')
        #This is printed: bob
    else :
        print('alice')
        #This is printed: alice
    #State: `t` remains unchanged, `i` is `t - 1`, `s` is the input string of the last test case, `a` is the integer value of the first element in the last test case, and `b` is the integer value of the second element in the last test case. Additionally, the sum of `a` and `b` is either even or not even.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers representing the number of coins in Alice's and Bob's wallets. For each test case, it prints "bob" if the sum of the two integers is even, and "alice" if the sum is odd.

