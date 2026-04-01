#Input: Ask the user for the Product Name.
ProName = input("Please enter the product name : ")
ProName = ProName.capitalize()
#Input: Ask for the Price (it could be a decimal like 19.99).
ProPrice = input("Please enter the price of the product  : ")
#Input: Ask for the Quantity they want to buy (e.g., 3).
Qua = input("Please enter the Quantity that  you want to buy : ")
#Convert the Price to a float.
ProPrice  = float(ProPrice)
#Convert the Quantity to an integer.
Qua = int(Qua)
#Convert the Quantity to an integer.
Total = Qua * ProPrice
print(f"""----- RECEIPT -----
       Product : {ProName}
       Unit Price : {ProPrice}
       Quantity : {Qua}
       -----------------------
       Total {Total}
       -----------------------""")