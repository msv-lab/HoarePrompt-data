str = raw_input();
n = len(str);
count = 0;
hand = [];
for i in range(0, n):
    if hand.__len__() == 0:
        hand.append(str[i]);
    elif str[i] == hand[-1] and hand.__len__() < 5:
        hand.append(str[i]);
    else:
        count = count + 1;
        hand = [str[i]];
print (count + (hand.__len__() != 0))
        
    
