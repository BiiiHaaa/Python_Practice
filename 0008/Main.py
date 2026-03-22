#Create:

my_skills = {"Python", "HTML", "CSS"}
friend_skills = {"CSS", "JavaScript", "C++"}

#1. Print all skills (both sets together)
print(my_skills.union(friend_skills))
#2. Print skills that are in my_skills but NOT in friend_skills
print(my_skills.difference(friend_skills))
#3. Remove "HTML" from my_skills
my_skills.remove("HTML")
#4. Print the updated my_skills
print(my_skills)