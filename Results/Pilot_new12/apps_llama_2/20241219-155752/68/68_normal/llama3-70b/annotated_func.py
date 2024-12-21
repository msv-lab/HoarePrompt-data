#State of the program right berfore the function call: x, y, and z are non-negative integers less than or equal to 100, representing the number of persons who would upvote, downvote, and vote with unknown outcome, respectively.
def func():
    x, y, z = map(int, input().split())
    if (x > y + z) :
        print('+')
    else :
        if (x < y) :
            print('-')
        else :
            if (x == y) :
                if (z == 0) :
                    print('0')
                else :
                    print('?')
                #State of the program after the if-else block has been executed: x, y, and z are input integers, x equals y, if z is 0, '0' has been printed to the console. Otherwise, z is a non-zero positive integer, and x = y, and x ≤ y + z holds true, given that x and y are input integers.
            else :
                print('?')
            #State of the program after the if-else block has been executed: x, y, and z are input integers, x is the first integer input, y is the second integer input, z is the third integer input, x is less than or equal to the sum of y and z, and x is greater than or equal to y. If x equals y, then if z is 0, '0' has been printed to the console, otherwise z is a non-zero positive integer. If x does not equal y, then '?' has been printed to the console.
        #State of the program after the if-else block has been executed: x, y, and z are input integers, x is the first integer input, y is the second integer input, z is the third integer input, and x is less than or equal to the sum of y and z. If x is less than y, a hyphen (-) has been printed. If x is greater than or equal to y, then if x equals y, either '0' has been printed to the console when z is 0, or z is a non-zero positive integer; otherwise, '?' has been printed to the console.
    #State of the program after the if-else block has been executed: x, y, and z are input integers, x is the first integer input, y is the second integer input, z is the third integer input. If x is greater than the sum of y and z, '+' has been printed to the console. If x is less than or equal to the sum of y and z, then if x is less than y, a hyphen (-) has been printed; otherwise, if x equals y, then either '0' has been printed to the console when z is 0, or '?' has been printed when z is a non-zero positive integer; if x is greater than y, '?' has been printed to the console.
#Overall this is what the function does:The function determines the outcome of a vote based on the number of upvotes (x), downvotes (y), and votes with unknown outcomes (z). It accepts three non-negative integers less than or equal to 100 as input, representing x, y, and z, and prints a character to the console indicating the outcome: '+' if x is greater than the sum of y and z, '-' if x is less than y, '0' if x equals y and z is 0, and '?' otherwise. The function does not return a value. After the function concludes, the console will contain a character indicating the outcome of the vote, and the input integers x, y, and z will remain unchanged. The function handles all potential cases, including edge cases where x equals y, or z is 0, or x is greater than or equal to y but less than or equal to the sum of y and z.

