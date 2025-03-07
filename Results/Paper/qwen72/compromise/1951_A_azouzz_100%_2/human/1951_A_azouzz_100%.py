def main():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        s = input()
        cnt1 = s.count('1')
        
        if cnt1 > 2 and cnt1 % 2 == 0:
            print("YES")
        elif cnt1 > 2 :
            print("NO")
        else:
            if (cnt1 == 1 ):
              print("NO")
            elif ("11" in s):
                print("NO")
            else:
                print("YES")
 
if __name__ == "__main__":
    main()