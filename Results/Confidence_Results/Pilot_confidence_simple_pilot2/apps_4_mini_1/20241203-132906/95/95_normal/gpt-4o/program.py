def convert_to_decimal(n, k):
    decimal_value = 0
    k_str = str(k)
    power = 0
    
    for digit in reversed(k_str):
        decimal_value += int(digit) * (n ** power)
        power += 1
        
    return decimal_value

if __name__ == "__main__":
    n = int(input().strip())
    k = input().strip()
    result = convert_to_decimal(n, k)
    print(result)
