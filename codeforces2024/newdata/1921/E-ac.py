def solve():
    h,w,xA,yA,xB,yB=map(int, input().split())
    if (xA-xB)%2==0:
        winner="Bob"
        if xA>=xB:
            win=False
        elif yA==yB:
            win=True
        else:
            if yA<yB:
                n_turns=yB-1
            else:
                n_turns=w-yB
            win=xB-2*n_turns>=xA
    else:
        winner="Alice"
        xA+=1
        yA+=0 if yB-yA==0 else 1 if yB - yA > 0 else -1
        if xA>xB:
            win=False
        elif yA==yB:
            win=True
        else:
            if yA<yB:
                n_turns=w-yA
            else:
                n_turns=yA-1
            win=xB-2*n_turns>=xA
    print(winner if win else "Draw")
t=int(input())
for _ in range(t):
    solve()
   	 	  	   	   		  	    		  		