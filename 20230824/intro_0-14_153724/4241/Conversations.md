# Question: 4241
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
Given are two strings S and T.
Let us change some of the characters in S so that T will be a substring of S.
At least how many characters do we need to change?
Here, a substring is a consecutive subsequence. For example, xxx is a substring of yxxxy, but not a substring of xxyxx.

-----Constraints-----
 - The lengths of S and T are each at least 1 and at most 1000.
 - The length of T is at most that of S.
 - S and T consist of lowercase English letters.

-----Input-----
Input is given from Standard Input in the following format:
S
T

-----Output-----
Print the minimum number of characters in S that need to be changed.

-----Sample Input-----
cabacc
abc

-----Sample Output-----
1

For example, changing the fourth character a in S to c will match the second through fourth characters in S to T.
Since S itself does not have T as its substring, this number of changes - one - is the minimum needed.
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
def substring_changes(S, T):
    # Initialize the minimum_changes variable to keep track of the minimum number of changes needed
    minimum_changes = float('inf')

    # Iterate through each possible starting index in S
    for i in range(len(S) - len(T) + 1):
        changes = 0
        
        # Check if T is a substring of S starting from the current index
        for j in range(len(T)):
            if S[i+j] != T[j]:
                changes += 1
        
        # Update the minimum_changes if the current number of changes is smaller
        minimum_changes = min(minimum_changes, changes)

    return minimum_changes

# Read input S and T
S = input()
T = input()

# Call the substring_changes function and print the result
print(substring_changes(S, T))
#@!CODE END!@#
````

---

