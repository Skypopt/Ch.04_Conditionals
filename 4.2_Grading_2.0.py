'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
semgrade=float(input("what is the semester grade? "))
finalexam=float(input("what is the final exam grade? "))
examworth=float(input("what is the exam worth? "))
leftoverweight=1-examworth
overall= (semgrade*leftoverweight)+(finalexam*examworth)
print(overall)
if overall >= 0.90:
    print("Final Grade: -A / A")
if overall >= 0.80 and overall < 0.90:
    print("Final Grade: -B / B / B+")
if overall >= 0.70 and overall <0.80:
    print("Final Grade: -C / C / C+")
if overall >=0.60 and overall <0.70:
    print("Final Grade: -D / D / D+")
if overall <0.60:
    print("Final Grade: F")
    print("Transfer to Johnston!")