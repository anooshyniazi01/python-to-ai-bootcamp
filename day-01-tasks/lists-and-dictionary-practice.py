#List
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print(fruits)
fruits.remove("banana")
print(fruits)
print("First fruit:", fruits[0])
print("Total fruits:", len(fruits))

#Dictionary
student = {
    "name": "Anosh",
    "age": 19,
    "semester": 4
}
print(student["name"])
student["age"] = 20
student["department"] = "CS"
print(student)
student.pop("semester")
print(student)
