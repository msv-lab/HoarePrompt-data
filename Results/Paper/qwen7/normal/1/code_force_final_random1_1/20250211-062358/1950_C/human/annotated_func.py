#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1440, and for each test case, s is a string of length 5 in the format "hh:mm" representing a valid time in the 24-hour format where hh is the hour from 00 to 23 and mm is the minute from 00 to 59.
def func_1():
    for t in range(int(input())):
        s = input()
        
        h = s[:2]
        
        if h == '00':
            print('12', end='')
        elif int(h) <= 12:
            print(h, end='')
        else:
            print('0{}'.format(int(h) - 12), end='')
        
        print(s[2:], ['AM', 'PM'][int(h) >= 12])
        
    #State: t is an integer such that 1 ≤ t ≤ 1440 + n, where n is the number of test cases provided, s is a new string input by the user for each iteration, and h is the first two characters of s.
#Overall this is what the function does:The function processes a series of times in the format "hh:mm" and converts them to a 12-hour clock format, printing the result along with "AM" or "PM". It reads the number of test cases from the user, then for each test case, it takes an input string `s`, extracts the hour part, and prints the corresponding 12-hour format time followed by "AM" or "PM". The function does not return any value; it only prints the converted times.

