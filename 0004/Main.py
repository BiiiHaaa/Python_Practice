#Create a tuple:
product_info = ("Laptop", 1500)
#Create a list:
discounts = [100, 250, 400]
#Print the product name from the tuple
print(f"The product name is : {product_info[0]}")
print(f"The original price is : {product_info[1]}")
#Print:
#Final price after first discount: ___
print(f"Final price after first discount is : {product_info[1] - discounts[0]}")
#Print:
#Final price after last discount: ___
print(f"Final price after last discount:{product_info[1] - discounts[-1]}")
#Print the type of product_info
print(type(product_info))

#Try to add a new discount to the list (example: 500) and print the updated 
discounts.append(500)
print(discounts)