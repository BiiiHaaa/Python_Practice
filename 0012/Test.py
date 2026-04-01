#The List: Start with a list of 3 friends: ["Osama", "Ahmed", "Sayed"].
friends = ["Osama", "Ahmed", "Sayed"]
#Input 1: Ask the user for a New Friend to add to the list.
Addfriend = input("Please enter the friend that you want to add : ")
#Input 2: Ask the user for a Friend to Remove from the list (assume they type the name correctly).
Rmfriend = input("Please enter the friend that you want to remove : ")
#Add the new friend to the beginning of the list.
friends.insert(0 , Addfriend)
#Remove the other friend from the list.
friends.remove(Rmfriend)
#Sort the final list alphabetically.
friends.sort()
print(friends)
#Output: * Print how many friends are currently in the list using len().
print(len(friends))