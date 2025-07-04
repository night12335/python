
# ≈‰‘«¡ Dictionary ›«—€…
empty_dict = {}

# ≈‰‘«¡ Dictionary „⁄ √“Ê«Ã «·„› «Õ Ê«·ﬁÌ„…
student = {"name": "Ali",
           "age": 20,
           "grade": "A"
}

# «” Œœ«„ «·œ«·… dict()
person = dict(name="Sara", age=25, city="Cairo")

# «·ﬁÌ„ Ì„ﬂ‰ √‰  ﬂÊ‰ √Ì ‰Ê⁄ „‰ «·»Ì«‰« 
info = {
    "name": "Omar",
    "scores": [90, 85, 88],
    "details": {"gender": "male", "height": 180}
}


# to reach the values

student = {"name": "Ali", "age": 20, "grade": "A"}
print(student["name"])  # Ali
print(student["age"])   # 20

#get()

print(student.get("grade"))  # A
print(student.get("school", "Not specified"))  # Not specified



#Add or modify items

#Add a new item:
student["school"] = "High School"
print(student)  # {'name': 'Ali', 'age': 20, 'grade': 'A', 'school': 'High School'}

#Modify an existing value:

student["age"] = 21
print(student)  # {'name': 'Ali', 'age': 21, 'grade': 'A'}


#DELETING items

#1 pop()

age = student.pop("age")
print(age)      # 21
print(student)  # {'name': 'Ali', 'grade': 'A'}


#2 del

del student["grade"]
print(student)  # {'name': 'Ali'}


#Basic operations on Dictionaries


#Get the keys:

print(student.keys())  # dict_keys(['name', 'age', 'grade'])


#Get values:

print(student.values())  # dict_values(['Ali', 20, 'A'])

#Get key and value pairs:

print(student.items())  # dict_items([('name', 'Ali'), ('age', 20), ('grade', 'A')])


#Merge Dictionaries

#update()

dict1 = {"name": "Ali", "age": 20}
dict2 = {"grade": "A", "school": "High School"}
dict1.update(dict2)
print(dict1)  # {'name': 'Ali', 'age': 20, 'grade': 'A', 'school': 'High School'}










