print("Welcome to python transport".upper().center(56,'❀'))
print("\n\n")
print("✾"*45)
print("Category\t\t1 Ticket\t\t5 Tickets\tMonthly")
print("Adult\t\t\t$3.00\t\t\t$12.65\t\t$95.70")
print("Senior\t\t\t$2.00\t\t\t$9.90\t\t$48.40")
print("Student\t\t\t$2.20\t\t\t$9.90\t\t$66.00")
print("✾"*45)
import time
#to ask for age
age=input("Are you an adult senior or student, respond with the full word")

if age.lower()=="adult":
    #tickets or monthly
    itemWanted=input("Do you want (1) Ticket (5) Tickets or a monthly pass?,\nkindly respond with 1,5,or 30")
    if itemWanted=="1":
        print("That will be $3.00 CAD")
    elif itemWanted=="5":
        print("That will be $12.65 CAD")
    elif itemWanted=="30":
        print("That will be $95.70 CAD")

elif age.lower()=="senior" :
     itemWanted=input("Do you want (1) Ticket (5) Tickets or a monthly pass?,\nkindly respond with 1,5,or 30")
     if itemWanted=="1":
        print("That will be $2.00 CAD")
     elif itemWanted=="5":
        print("That will be $9.90 CAD")
     elif itemWanted=="30":
        print("That will be $48.40 CAD")

elif age.lower()=="student" :
     itemWanted=input("Do you want (1) Ticket (5) Tickets or a monthly pass?,\nkindly respond with 1,5,or 30")
     if itemWanted=="1":
        print("That will be $2.20 CAD")
     elif itemWanted=="5":
        print("That will be $9.90 CAD")
     elif itemWanted=="30":
        print("That will be $66.00 CAD")
#to allow for another try
else:
    print("Invalid.Try again")

time.sleep(0.5)
print("\n\nThank you for using python transportation")


                     
