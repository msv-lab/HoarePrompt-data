#State of the program right berfore the function call: Each test case consists of four integers p1, p2, p3, and p4 (0 ≤ p1, p2, p3, p4 ≤ 200) representing the number of ones, twos, threes, and fours in the sequence. The first line of the input contains an integer t (1 ≤ t ≤ 10^4) indicating the number of test cases.
def func():
    for _ in range(int(input())):
        p = list(map(lambda x: int(x) - int(x) % 2, input().split()))
        
        print((sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2)
        
    #State: 3, 4, 5, 6
#Overall this is what the function does:The function processes multiple test cases, each consisting of four integers representing the counts of ones, twos, threes, and fours in a sequence. For each test case, it calculates and prints a value that is the sum of half the total count of these numbers (rounded down) plus 1 if all of the counts of ones, twos, and threes are odd.

