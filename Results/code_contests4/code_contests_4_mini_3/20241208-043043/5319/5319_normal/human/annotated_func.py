#State of the program right berfore the function call: The input consists of exactly 10 lines, each containing an integer si (0 ≤ si ≤ 100) representing the score of problem i.
def func():
    k = 0
    for i in range(10):
        k = k + int(input())
        
    #State of the program after the  for loop has been executed: `k` is the sum of 10 input integers, `i` is 9, and the loop has executed 10 times.
    print(k)
#Overall this is what the function does:The function accepts no parameters, reads 10 integer scores from user input (each between 0 and 100), calculates the sum of these scores, and prints the total sum. It does not return any value.

