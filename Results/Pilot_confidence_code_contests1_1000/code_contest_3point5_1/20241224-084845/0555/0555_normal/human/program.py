def solution(count, s):      
    dup = 0                  
    for i in range(0, count+1, 2):                         
        if s[:i/2] == s[i/2:i]:                            
            dup = i/2        
    if dup == 0:             
        return count         
    return count - dup + 1   

if __name__ == '__main__':   
    c = int(raw_input())     
    s = raw_input()          
    print(solution(c, s))