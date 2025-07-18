import pandas as pd


students_data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [20, 22, 19, 21, 20],
    'Grade': ['A', 'B', 'A', 'C', 'B'],
    'Marks': [85, 78, 92, 65, 74]
})



print("First 3 rows:")
print(students_data.head(3))


print("\nOnly Name and Marks columns:")
print(students_data[['Name', 'Marks']])

print("\nStudents with Grade 'A':")
print(students_data[students_data['Grade'] == 'A'])
