def calculate_max_beauty(ribbon, n):
    from collections import Counter

    # Count the frequency of each character in the ribbon
    freq = Counter(ribbon)
    
    # Find the maximum frequency of any character in the ribbon
    max_freq = max(freq.values())
    
    # If the length of the ribbon is more than the maximum frequency plus n changes,
    # we can make all characters the same
    if len(ribbon) == max_freq and n == 1:
        return max_freq - 1
    else:
        return min(len(ribbon), max_freq + n)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    ribbons = data[1:]
    
    kuro_ribbon = ribbons[0]
    shiro_ribbon = ribbons[1]
    katie_ribbon = ribbons[2]
    
    # Calculate the maximum beauty for each ribbon
    kuro_beauty = calculate_max_beauty(kuro_ribbon, n)
    shiro_beauty = calculate_max_beauty(shiro_ribbon, n)
    katie_beauty = calculate_max_beauty(katie_ribbon, n)
    
    # Determine the winner
    beauties = [kuro_beauty, shiro_beauty, katie_beauty]
    max_beauty = max(beauties)
    
    if beauties.count(max_beauty) > 1:
        print("Draw")
    else:
        if max_beauty == kuro_beauty:
            print("Kuro")
        elif max_beauty == shiro_beauty:
            print("Shiro")
        else:
            print("Katie")

if __name__ == "__main__":
    main()
