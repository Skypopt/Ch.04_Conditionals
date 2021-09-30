'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
semgrade=float(input("what is the semester grade? "))
finalexam=float(input("what is the final exam grade? "))
examworth=float(input("what is the exam worth? "))
leftoverweight=100-examworth
overall= ((semgrade*leftoverweight)+(finalexam*examworth))/100
print(overall)
if overall >= 90:
    print("Final Grade: -A / A")
elif overall >= 80:
    print("Final Grade: -B / B / B+")
elif overall >= 70:
    print("Final Grade: -C / C / C+")
elif overall >=60:
    print("Final Grade: -D / D / D+")
else:
    print("Final Grade: F")
    print("Transfer to Johnston!")