#State of the program right berfore the function call: N is a positive integer and a_i is an integer for each i where 1 <= i <= N.**
def func():
    N = raw_input()
    a = raw_input().split()
    ans = np.abs(np.max(a) - np.min(a))
    print(ans)
#Overall this is what the function does:The function accepts no explicit parameters but reads a positive integer N and a list of integers a_i. It then calculates the absolute difference between the maximum and minimum values in the list a and prints the result. The function lacks error handling for invalid inputs or empty list cases.

