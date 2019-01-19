import time #makes it look better instead of everything just appearing at the same time)
print("Welcome to Python Exchange".upper().center(56,'❀'))
print("="*80)
print("currency\tvalue")
print("JPY\t\t0.0110617 CAD")
print("BRL\t\t0.39133   CAD")
print("AUD\t\t0.975996  CAD")
print("CHF\t\t1.27544   CAD")
print("="*80)

#to ask for how much money he wishes to exchange
#to ask for what currency the user wishes to change from
amountOfMoney=float(input("Enter the amount of money you wish to exchange $"))
currency=input("\n\nEnter the currency you wish to chnage to canadian using the first letter of the currency,\n(J)PY,(B)RL,(A)UD,(C)HF")
if currency.upper()=="J":
    #ans stands for answer or just the final transaction
    ans=amountOfMoney*0.0110617
    print( "\n\nThe total sum is $%.2f CAD" %ans)
    
elif currency.upper()=="B":
    ans=amountOfMoney*0.39133
    print("\n\nThe total sum is $%.2f CAD" %ans)

elif currency.upper()=="A":
    ans=amountOfMoney*0.975996
    print("\n\nThe total sum is $%.2f CAD" %ans)

elif currency.upper()=="C":
    ans=amountOfMoney*1.27544 
    print("\n\nThe total sum is $%.2f CAD" %ans)

else:
    print("\n\nInavlid currency,try again")

time.sleep(0.5)

print("\n\nThank you for using Python exchanger :)")

#to keeo it friendly





    
    


