import streamlit as st
import pandas as pd

# Load student data
students_df = pd.read_csv('src/data/students.csv')
marks_df = pd.read_csv('src/data/marks.csv')

# Merge dataframes on student ID
merged_df = pd.merge(students_df, marks_df, on='student_id')

# Calculate average marks for each student
average_marks = (
    merged_df
    .groupby(['student_id', 'name'], as_index=False)
    .mean(numeric_only=True)
)

# Streamlit app layout
st.title("Student Progress Dashboard")

# Display student information
st.header("Student Information")
st.dataframe(students_df)

# Display marks information
st.header("Marks Information")
st.dataframe(marks_df)

# Display average marks
st.header("Average Marks")
st.dataframe(average_marks)

# Optionally, add visualizations or additional features here