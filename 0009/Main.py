#Create:

products = ["Laptop", "Phone", "Laptop", "Tablet", "Phone"]
prices = [1500, 800, 1500, 600, 800]
#1. Remove duplicate products using set
unique_products = set(products)
#2. Print:
#Unique products: ___
print(f"Unique products : {unique_products}")
#3. Print the number of unique products
print(f"The number of unique products is : {len(unique_products)}")
#4. Print:
#First product is ___ and its price isq ___
print(f"First product is : {products[0]} and its price is : {prices[0]}")
#5. Add a new product "Monitor" to products list
products.append("Monitor")
print(products)