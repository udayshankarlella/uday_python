import sys
def discount(amount):
    amount = amount-(amount*10)/100
    return amount
x = int(input("Enter how many Aproduts somu want:"))
y = int(input("Enter how many Bproducts somu want:"))
costof_A=int(sys.argv[1])
costof_B=int(sys.argv[2])
amount = (x*costof_A)+(y*costof_B)

amount=discount(amount)
print("total amount is :",amount)
