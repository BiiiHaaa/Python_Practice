#Create a variable:
product = "Laptop"
price = 1500
#Create a list:
discounts = [100, 200, 300]
#Print:
#"The price of Laptop is 1500"
print(f"The price of {product} is {price}")
#Print the price after first discount
print(f"the price after first discount is : {price - discounts[0]}")
#Print the price after last discount
print(f"the price after last discount is : {price - discounts[-1]}")
