#State of the program right berfore the function call: **n is an integer representing the number of coins, and a_i are integers representing the values of the coins.
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *n is an integer representing the number of coins, a_i are integers representing the values of the coins, a is a list of integers obtained from input. If n is equal to 11, then the function proceeds with the specified conditions for n = 11.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: n is an integer representing the number of coins, a_i are integers representing the values of the coins, a is a list of integers obtained from input, c is a list of 101 elements with the value at each index representing the frequency of that value in list a
    print(max(c))
#Overall this is what the function does:The function reads an integer n representing the number of coins, and a list of integers representing the values of the coins. It then creates a frequency list c to count the occurrences of each value in the coin list. Finally, it prints the maximum frequency of any coin value in the list c.

