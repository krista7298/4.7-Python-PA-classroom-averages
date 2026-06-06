print("kriagu7298")

import pandas as pd
import matplotlib.pyplot as plt

# Create an array/list of students and subjects for the MultiIndex.
studentsAndSubjects = [
    ["Krista", "Krista", "Connor", "Connor", "Tina", "Tina", "Jeremy", "Jeremy", "Wyatt", "Wyatt",
     "Rylan", "Rylan", "Brittney", "Brittney", "Wren", "Wren", "Tobi", "Tobi", "Alex", "Alex"],
    ["Math", "Science", "Math", "Science", "Math", "Science", "Math", "Science", "Math", "Science",
     "Math", "Science", "Math", "Science", "Math", "Science", "Math", "Science", "Math", "Science"]
]

# Create an index for student and subject using the MultiIndex function.
index = pd.MultiIndex.from_arrays(studentsAndSubjects, names=("Student", "Subject"))

# Create a DataFrame of grades for each student for two subjects.
df = pd.DataFrame(
    {"Grade": [99, 87, 99, 75, 89, 54, 67, 77, 88, 99,
               99, 87, 99, 75, 89, 54, 67, 77, 88, 99]},
    index=index
)

# Display the DataFrame.
print(df)

# Group the grades by subject and calculate the mean.
averageGrades = df.groupby(by=["Subject"]).mean()

# Display the grouped mean grades.
print(averageGrades)

# Create a vertical bar graph showing the average grade by subject.
averageGrades["Grade"].plot(kind="bar")

plt.xlabel("Average Grade by Subject")
plt.ylabel("Grade")
plt.xticks(rotation=0)
plt.title("kriagu7298 Average Grade by Subject")

plt.show()
