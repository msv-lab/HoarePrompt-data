#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of four non-negative integers p_i (0 ≤ p_i ≤ 200), representing the counts of 1s, 2s, 3s, and 4s in the initial sequence, respectively.
def func():
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3))
        
    #State: Output State: The sum of the quotients when each of the four counts (a, b, c, d) is divided by 2, plus 1 if the sum of the remainders of these divisions is exactly 3.
#Overall this is what the function does:The function processes four non-negative integers representing the counts of 1s, 2s, 3s, and 4s in an initial sequence. It calculates the total count of elements in the sequence by summing the quotients of each count divided by 2 and adding 1 if the sum of their remainders equals 3. The function does not return any value but prints the calculated result for each input set.

