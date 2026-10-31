AIM:
To create a student dataset using Pandas and display the dataset containing students' marks in Mathematics, Science, and English, along with their study hours.

ALGORITHM:
1. Import the Pandas and NumPy libraries.
2. Create a dictionary containing student names, subject marks, and hours studied.
3. Convert the dictionary into a Pandas DataFrame.
4. Display the dataset.

PROGRAM:
import pandas as pd
import numpy as np
data = {
    "student": [
        "thrisha", "vaishnavi", "dhanushka", "dhatri",
        "ravi", "bharath", "ani", "prudhvi",
        "ammu", "purushotham"
    ],
    "math": [93, 83, 74, 96, 84, 91, 98, 83, 74, 99],
    "science": [82, 94, 72, 84, 95, 83, 77, 88, 97, 88],
    "english": [84, 99, 88, 77, 83, 95, 86, 97, 83, 91],
    "Hours Studied": [5, 4, 3, 6, 4, 5, 7, 3, 2, 8]
}
df = pd.DataFrame(data)
print(df)

RESULT :
The student dataset was successfully created using Pandas and displayed with student names, subject marks, and hours studied.
