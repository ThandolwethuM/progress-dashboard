def load_student_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def load_marks_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def calculate_average_marks(marks_df):
    return marks_df.groupby('student_id')['marks'].mean().reset_index()

def get_student_progress(students_df, marks_df):
    average_marks = calculate_average_marks(marks_df)
    progress_df = students_df.merge(average_marks, on='student_id', how='left')
    progress_df.rename(columns={'marks': 'average_marks'}, inplace=True)
    return progress_df

def generate_progress_chart(progress_df):
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.figure(figsize=(10, 6))
    sns.barplot(data=progress_df, x='name', y='average_marks', palette='viridis')
    plt.title('Student Progress Dashboard')
    plt.xlabel('Student Name')
    plt.ylabel('Average Marks')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()