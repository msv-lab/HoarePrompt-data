#State of the program right berfore the function call: Each test case consists of four integers \( p_1, p_2, p_3, p_4 \) (0 \(\le\) \( p_i \) \(\le\) 200) representing the number of ones, twos, threes, and fours in the sequence, respectively. There are \( t \) (1 \(\le\) \( t \) \(\le\) 10^4) such test cases.
def func():
    for _ in range(int(input())):
        p = list(map(lambda x: int(x) - int(x) % 2, input().split()))
        
        print((sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2)
        
    #State: 4
#Overall this is what the function does:The function processes multiple test cases, each consisting of four integers representing the counts of ones, twos, threes, and fours in a sequence. For each test case, it calculates and prints a result that is the sum of half the total count of these numbers (rounded down) plus one if all of the counts of ones, twos, and threes are odd.

