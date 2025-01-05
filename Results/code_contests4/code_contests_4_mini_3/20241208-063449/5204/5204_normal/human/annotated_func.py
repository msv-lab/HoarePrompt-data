#State of the program right berfore the function call: l is a positive integer representing the length of the corridor (1 ≤ l ≤ 1000), p is a positive integer representing the speed of Harry's magical impulse (1 ≤ p ≤ 500), and q is a positive integer representing the speed of He-Who-Must-Not-Be-Named's magical impulse (1 ≤ q ≤ 500).
def func():
    l = input()
    p = input()
    q = input()
    print(float(l) / (p + q)) * p
#Overall this is what the function does:The function accepts three positive integers: `l` (length of the corridor), `p` (speed of Harry's magical impulse), and `q` (speed of He-Who-Must-Not-Be-Named's magical impulse). It calculates the time it takes for Harry's impulse to travel the length of the corridor and then prints the distance traveled by Harry's impulse in that time. However, it does not return any value; it only prints the result. Additionally, the function does not handle invalid input since it directly takes user input without validation.

