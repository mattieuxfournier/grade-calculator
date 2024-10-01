#Mattieux Fournier
import math #to extend the list of math functions
#open function
def PyGradeCalc():
#Start loop for input to repeat until a number within the domain is met
#accept for anything greater than 0 and return 100 for numbers 6 or more
        while True:
                lab = float(input("Enter the number of labs completed: "))
                lab = int(lab)
                if 0 <= lab:
                        break
                else:
                        print("Please enter a real number")
        if lab >= 6:
                lab = 100
        else:
                lab = (lab/6)*100
#same input requirements as lab
        while True:
                quiz = float(input("Enter the number of quizzes completed: "))
                quiz = int(quiz)
                if 0 <= quiz:
                        break
                
                else:
                        print("Please enter a real number")
        if quiz >= 6:
                quiz = 100
        else:
                quiz = (quiz/6) *100
#grades are limited from 0 to 100 percent as an acceptable input
        while True:
                a1 = float(input("Enter grade for Assignment 1: "))
                if 0 <= a1 <= 100:
                        break
                else:
                        print("The number must be out of 100")
#
        while True:
                a2 = float(input("Enter grade for Assignment 2: "))
                if 0 <= a2 <= 100:
                        break
                else:
                        print("The number must be out of 100")
#
        while True:
                a3 = float(input("Enter grade for Assignment 3: "))
                if 0 <= a3 <= 100:
                        break
                else:
                        print("The number must be out of 100")
        while True:
                a4 = float(input("Enter grade for Assignment 4: "))
                if 0 <= a4 <= 100:
                        break
                else:
                        print("The number must be out of 100")
#
        while True:
                mid1 = float(input("Enter grade for Midterm 1: "))
                if 0 <= mid1 <= 100:
                        break
                else:
                        print("The number must be out of 100")
#
        while True:
                mid2 = float(input("Enter grade for Midterm 2: "))
                if 0 <= mid2 <= 100:
                        break
                else:
                        print("The number must be out of 100")
#
        while True:
                final = float(input("Enter grade for Final Exam: "))
                if 0 <= final <= 100:
                        break
                else:
                        print("The number must be out of 100")
#
        while True:
                prep = float(input("Enter grade for Midterms and Final Preperation: "))
                if 0 <= prep <= 100:
                        break
                else:
                        print("The number must be out of 100")
#assigns the calculation to a variable
        total = 0.2*(lab) + 0.15*(quiz) + 0.04*a1 + 0.04*a2 + 0.04*a3 + 0.04*a4 + 0.125*mid1 + 0.125*mid2 + 0.18*final + 0.06*prep
        total = round(total,2)
#return variable
        print("Your grade is: " + str(total) + "%" )
#close function
PyGradeCalc()

