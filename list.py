students = ["kaisamba", "Foday", "Sharon"]
print(students)

#Accessing items in list by there index
print(f"My best friend is {students[0]} ")
print(f"My best friend is {students[1]} ")
print(f"My best friend is {students[2]} ")

#Get the index of an item in the list
index = students.index("Foday")
print(f"The index of Foday is {index}")

index = students.index("Sharon")
print(f"The index of Sharon is {index}")

index = students.index("kaisamba")
print(f"The index of kaisamba is {index}")

# know the number of items in the list
print(f"The number of students in the list is {len(students)}")

# Add items to a list
students.append("Musa")
print(students)

students += ["kadiatu", "John", "Bintu"]

print(students)
students.insert(4, "Abubakarr")
print(students)

# Extending a list
fruits = ["banana", "mango", "orange"]
students.extend(fruits)
print(students)

#Removing items from a list
students.remove("Musa")
print(students)

fruits.remove("banana")
print(fruits)

students.pop()
print(students)
thirditem = students.pop()
print(students)
print(thirditem)