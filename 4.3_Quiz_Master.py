'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
score=0
lettergrade=0
#Question 1!!!
a = float(input("Question 1: What is 29+420?"))
if a==449:
    print("Correct! Next question.")
    score=score+1
else:
    print("That is incorrect, the answer is 449, next question :(")
#Question 2!!!
b = str(input("Question 2: What is the name of the first star wars movie released"))
correct=["A new hope", "A New Hope", "a new hope", "A NEW HOPE"]
if b in correct:
    print("That is correct!")
    score = score + 1
else:
    print("That isn't correct, the answer is A new hope! Next question")
#Question 3!!!
c = str(input("Question 3: Multiple choice, chose the right answer, what is 2+17. A:19, B:29, or C:12"))
correct2=["A", "a"]
if c in correct2:
    print("That is correct!")
    score = score + 1
else:
    print("That is not correct, the answer is A, next question")
#Question 4
d = float(input("Question 4: How many planets are in the solar system?"))
if d == 8:
    print("Correct! Next question")
    score = score + 1
else:
    print("Incorrect, the answer is 8, next question")
#Question 5
e = str(input("Question 5: What is the main character of demon slayer?"))
correct3 = ["Tanjiro", "tanjiro", "Tanjiro Kamado", "tanjiro Kamado", "tanjiro kamado", "Tanjiro kamado"]
if e in correct3:
    print("That is correct, next question")
    score = score + 1
else:
    print("That is not correct, the answer is Tanjiro Kamado, next question")
#Question 6
f = float(input("What is 12+72"))
if f == 84:
    print("That is correct, next question")
    score = score + 1
else:
    print("That is not correct, the answer is 84, next question")
#Question 7
g = float(input("What is 8*8/2"))
if g == 32:
    print("That is correct, next question")
    score = score + 1
else:
    print("That is not correct, the answer is 32, next question")
print("")
print("YOUR SCORE ISSSSSSSS")
print(score)
print("OUT OF 7 POINTS")
print(score//0.07,"%")
print("")
if score==7:
    print("Grade: A+")
if score==6:
    print("Grade: B")
if score==5:
    print("Grade: C-")
if score==4:
    print("Grade: F")
if score==3:
    print("Grade: F")
if score==2:
    print("Grade: F")
if score==1:
    print("Grade: F")
if score==0:
    print("Grade: F")
if score<5:
    print("")
    print("LOL YOU SUCKKKKK")