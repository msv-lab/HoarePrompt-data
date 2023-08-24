# Question: 3117
## Generation 1
### Conversations

---

**role**: 
````markdown
system
````

---

**content**: 
````markdown
I want you to act as a Coding Contest Participant. Imagine that you are taking part in a prestigious coding competition. Your task is to design an efficient algorithm for a complex problem. You need to consider all possible edge cases, optimize for efficiency, and ensure that your solution is clean and readable. In addition, provide a Python code of your solution, and put the solution in a code delimiter.For example:
### QUESTION
A. Watermelon
time limit per test: 1 second
memory limit per test: 64 megabytes
input: standard input
output: standard output
One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the ripest one, in their opinion. After that the watermelon was weighed, and the scales showed w kilos. They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way that each of the two parts weighs even number of kilos, at the same time it is not obligatory that the parts are equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, if they can divide the watermelon in the way they want. For sure, each of them should get a part of positive weight.

Input
The first (and the only) input line contains integer number w (1 <= w <= 100) — the weight of the watermelon bought by the boys.

Output
Print YES, if the boys can divide the watermelon into two parts, each of them weighing even number of kilos; and NO in the opposite case.

Examples
input
8
output
YES
Note
For example, the boys can divide the watermelon into two parts of 2 and 6 kilos respectively (another variant — two parts of 4 and 4 kilos).

### Expected response from you
#@!CODE START!@#
w = int(input())
if w % 2 == 1 or w < 4:
print("NO")
else:
print("YES")
#@!CODE END!@#
````

---

**role**: 
````markdown
user
````

---

**content**: 
````markdown
### QUESTION
Ivana won the bet (Zvonko hadn’t foreseen this and suspects that it is due to outside interference) and now Zvonko is waiting for her at the movies. While he is waiting, he is observing messages on a screen above him.

As Ivana is running late, Zvonko has been looking at the screen for a while and noticed that some messages appeared on the screen more than once. Naturally, he’s been writing down all messages on a piece of paper. He wants to know the length of the longest string that appeared at least twice (appears in two different positions on the paper).

-----Input-----
The first line of input contains an integer $L~ (1 \leq L \leq 200000)$, the length of the string Zvonko wrote down.

The second line contains a string of $L$ lowercase letter of the English alphabet.

-----Output-----
Output the length of the longest string that appears twice on a single line. If there is no such string, output zero.

-----Examples-----
Sample Input 1:
11
sabcabcfabc
Sample Output 1:
3

Sample Input 2:
18
trutrutiktiktappop
Sample Output 2:
4
### Requirements
1. Use Standard Input Format (read inputs with `input()`, write results with `print()`)
2. You will NOT return anything except for the program. 
3. DO NOT WRITE PLANS OR EXPLANATIONS
````

---

**role**: 
````markdown
assistant
````

---

**content**: 
````markdown
#@!CODE START!@#
def longest_duplicate_string(length, string):
    max_length = 0
    duplicates = set()
    
    for i in range(length - 1):
        for j in range(i + 1, length):
            if string[i:j+1] in duplicates:
                if j - i + 1 > max_length:
                    max_length = j - i + 1
            else:
                duplicates.add(string[i:j+1])
    
    return max_length

L = int(input())
s = input()

result = longest_duplicate_string(L, s)
print(result)
#@!CODE END!@#
````

---

