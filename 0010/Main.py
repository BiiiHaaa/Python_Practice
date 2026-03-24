#Create a dictionary:

product = {
    "name": "Laptop",
    "price": 1500,
    "brand": "HP"
}
#1. Print:
print(f"Product name is : {product['name']}") 
#2. Print:
print(f"Product price is : {product['price']}") 
#3. Add a new key:
product['stock'] = 10

#Then print the whole dictionary
print(product)
#4. Print only the keys of the dictionary
print(product.keys())
#5. Print only the values
print(product.values())
#6. Create a list of products:
products = [
    {"name": "Laptop", "price": 1500},
    {"name": "Phone", "price": 800}
]
#Print:
print(f"First product is: {products[0]['name']} and its price is: {products[0]['price']}")