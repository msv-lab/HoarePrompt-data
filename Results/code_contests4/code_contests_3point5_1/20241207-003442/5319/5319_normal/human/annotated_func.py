#State of the program right berfore the function call: Each si (0 ≤ si ≤ 100) is an integer representing the score of a problem.**
def func():
    k = 0
    for i in range(10):
        k = k + int(input())
        
    #State of the program after the  for loop has been executed: Each si (0 ≤ si ≤ 100) is an integer representing the score of a problem, `k` is the sum of 10 input integer values
    print(k)
#Overall this is what the function does:The function does not accept any parameters. It iterates 10 times, taking an integer input each time, and calculates the sum of these inputs. Finally, it prints the total sum. The function does not have any specific return value, but it effectively calculates and displays the sum of 10 input integer values.

