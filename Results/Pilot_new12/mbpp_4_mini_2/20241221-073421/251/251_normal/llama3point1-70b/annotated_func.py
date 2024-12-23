#State of the program right berfore the function call: x and y are real numbers representing rectangular coordinates.
def func_1(x, y):
    r = math.hypot(x, y)
    phi = math.atan2(y, x)
    return r, phi
    #The program returns r which is the positive value equal to math.hypot(x, y) and phi which is equal to math.atan2(y, x)
#Overall this is what the function does:The function accepts two real numbers, x and y, representing rectangular coordinates. It calculates the polar coordinates (r, phi) where r is the hypotenuse computed using the Euclidean distance formula from (x, y) and is always a non-negative value. Phi is the angle in radians calculated from the coordinates (y, x) using the arctangent function. The function returns the computed values (r, phi). Edge cases considered include instances where x and y are both zero, resulting in r being zero and phi being undefined, which the atan2 function correctly handles by returning zero in this case.

