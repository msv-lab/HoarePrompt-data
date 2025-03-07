def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    for _ in range(t):
        n = int(data[index])
        s = data[index + 1]
        index += 2
        
        count_u = s.count('U')
        if count_u % 2 == 1:
            print("YES")
        else:
            print("NO")
 
if __name__ == "__main__":
    main()