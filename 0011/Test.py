#Input: Ask the user for their Full Name (example: "  osama mohamed elzero  ").
Fname = input("Please enter you Full Name :")
#Input: Ask the user for their Age.
Age = input("Please enter you Age : ")
#Input: Ask the user for their Country.
Country = input("Please enter you Country : ")
#Name: Strip any extra spaces, then capitalize the first letter of every word (Title Case).
Fname = Fname.strip().title()
#Age: Convert the input to an integer and calculate how many years are left until they reach 100 years old.
Age = int(Age)
print(f"You have {100- Age} years to go to reach the age of 100 ")
#Country: Strip spaces and make it all Uppercase.
Country = Country.strip().upper()
#Output: Print a formatted message using f-strings like this:
print(f"Hello {Fname}, Your Age is {Age}. You have {100-Age} years left to reach 100. Welcome to {Country}!")