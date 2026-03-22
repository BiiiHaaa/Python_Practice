#Create:
skills = ["Python", "HTML", "CSS", "Python", "CSS"]
#1. Convert the list to a set
unique_skills = {"Python", "HTML", "CSS", "Python", "CSS"}

#2. Print:
#My skills are: ___
print(unique_skills)
#PS C:\Users\BiiiHaaa\Desktop\python> python -u "c:\Users\BiiiHaaa\Desktop\Python_Practice\0007\Main.py"
#{'CSS', 'Python', 'HTML'}
#3. Print the number of unique skills
print(len(unique_skills))
#4. Add a new skill:
unique_skills.add("JavaScript")
print(unique_skills)
#5. Create another set:
other_skills = {"Python", "C++", "JavaScript"}
#6. Print the common skills between the two sets
print(unique_skills.intersection(other_skills))