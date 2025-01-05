#State of the program right berfore the function call: The input consists of 10 integers representing the scores of each problem, where each score si is an integer such that 0 ≤ si ≤ 100.
def func():
    k = 0
    for i in range(10):
        k = k + int(input())
        
    #State of the program after the  for loop has been executed: `k` is the sum of 10 user inputs, `i` is 9
    print(k)
#Overall this is what the function does:The function does not accept any parameters. It reads 10 integer inputs representing scores of problems, calculates the total sum of these scores, and prints the final sum.

