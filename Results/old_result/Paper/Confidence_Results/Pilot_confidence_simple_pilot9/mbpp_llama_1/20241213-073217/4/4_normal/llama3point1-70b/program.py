def differ_At_One_Bit_Pos(num1, num2):
    return bin(num1 ^ num2).count('1') == 1
