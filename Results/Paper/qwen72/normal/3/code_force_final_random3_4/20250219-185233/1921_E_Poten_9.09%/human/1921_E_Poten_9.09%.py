test_cases = int(input())
answers = []
for i in range(test_cases):
    clues = list(map(int,input().split(" ")))
    if clues[2] > clues[4] or clues[0]==1:
        answers.append("Draw")
    elif(clues[2]%2==0 and clues[4]%2==0) or (clues[2]%2!=0 and clues[4]%2!=0):
        if clues[3] == clues[5]:
            answers.append("Bob")
        elif clues[3]<clues[5]:
            if abs(clues[3]-clues[5])>1:
                if clues[3]-1 >= abs((clues[2]-clues[4])//2) or clues[5]-clues[3] >= abs((clues[2]-clues[4])//2):
                    answers.append("Draw")
                else:
                    answers.append("Bob")
            else:
                if clues[3]-1 > abs((clues[2]-clues[4])//2) or clues[5]-clues[3] > abs((clues[2]-clues[4])//2):
                    answers.append("Draw")
                else:
                    answers.append("Bob")
        elif clues[3]>clues[5]:
            if abs(clues[3]-clues[5])>1:
                if clues[1]-clues[3]>= abs((clues[2]-clues[4])//2) or clues[3]-clues[5] >= abs((clues[2]-clues[4])//2):
                    answers.append("Draw")
                else:
                    answers.append("Bob")
            else:
                if clues[1]-clues[3]> abs((clues[2]-clues[4])//2) or clues[3]-clues[5] > abs((clues[2]-clues[4])//2):
                    answers.append("Draw")
                else:
                    answers.append("Bob")
    else:
        if clues[3] == clues[5]:
            answers.append("Alice")
        elif clues[3]<clues[5]:
            if abs(clues[3]-clues[5])>1:
                if clues[1]-clues[5] > abs((clues[2]-clues[4])//2) or clues[5]-clues[3] > abs((clues[2]-clues[4])//2):
                    answers.append("Draw")
                else:
                    answers.append("Alice")
            else:
                if clues[1]-clues[5]-1 > abs((clues[2]-clues[4])//2) or clues[5]-clues[3]-1 > abs((clues[2]-clues[4])//2):
                    answers.append("Draw")
                else:
                    answers.append("Alice")
        elif clues[3]>clues[5]:
            if abs(clues[3]-clues[5])>1:
                if clues[5]-1 > abs((clues[2]-clues[4])//2) or clues[3]-clues[5] > abs((clues[2]-clues[4])//2):
                    answers.append("Draw")
                else:
                    answers.append("Alice")
            else:
                if clues[5]-1-1 > abs((clues[2]-clues[4])//2) or clues[3]-clues[5]-1 > abs((clues[2]-clues[4])//2):
                    answers.append("Draw")
                else:
                    answers.append("Alice")
for j in answers:
    print(j)