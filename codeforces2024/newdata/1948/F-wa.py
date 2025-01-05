import sys

MOD = 998244353

def mod_inverse(a, p):
    # Calculate the modular inverse using Fermat's little theorem
    return pow(a, p-2, p)

def calculate_total_value(a, b):
    # Calculate the total value of gold and silver coins for each bag
    total_value = [a[i] + b[i] for i in range(len(a))]
    return total_value

def process_query(l, r, total_value, n):
    # Calculate the total value in the specified range and compare it to the total value in the remaining bags
    range_value = sum(total_value[i-1] for i in range(l, r+1))
    other_value = sum(total_value) - range_value
    
    # Calculate the probability that the total value in the specified range is strictly greater than the total value in the remaining bags
    if range_value > other_value:
        return 1
    else:
        return 0

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    q = int(data[1])
    
    a = [int(data[2+i]) for i in range(n)]
    b = [int(data[2+n+i]) for i in range(n)]
    
    total_value = calculate_total_value(a, b)
    
    for i in range(q):
        l = int(data[2+2*n+i*2])
        r = int(data[2+2*n+i*2+1])
        
        probability = process_query(l, r, total_value, n)
        print(probability)

if __name__ == "__main__":
    main()