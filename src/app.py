import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

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

# Guage chart for overall average

# average = merged_df['marks'].mean()
average = 48 # Example average, replace with actual calculation




# Create a gradient of colors from red to yellow to green
def get_gradient_steps(start, end, n_steps):
    gradient = []
    for i in range(n_steps):
        ratio = i / (n_steps - 1)
        if ratio < 0.5:
            # Red to Yellow
            r = 255
            g = int(255 * (ratio / 0.5))
            b = 0
        else:
            # Yellow to Green
            r = int(255 * (1 - (ratio - 0.5) / 0.5))
            g = 255
            b = 0
        color = f"rgb({r},{g},{b})"
        gradient.append({'range': [start + i*(end-start)/n_steps, start + (i+1)*(end-start)/n_steps], 'color': color})
    return gradient

steps = get_gradient_steps(0, 100, 100)  # More steps for smoother gradient

fig = go.Figure(go.Indicator(
    mode="gauge",
    value=average,
    gauge={
        'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkgray"},
        'bar': {'color': "rgba(0,0,0,0)"},  # Hide default bar
        'steps': steps,
        'threshold': {
            'line': {'color': "rgba(0,0,0,0)", 'width': 0},  # Hide threshold
            'thickness': 0,
            'value': average
        }
    },
    domain={'x': [0, 1], 'y': [0, 1]},
    title=None
))

# Calculate the angle for the hand (in radians)
angle = (average / 100) * np.pi  # 0 to pi (180 degrees)
center_x, center_y = 0.5, 0.5
radius = 0.4

# Calculate end point of the hand
end_x = center_x + radius * np.cos(np.pi - angle)
end_y = center_y + radius * np.sin(np.pi - angle)

# Add the clock hand as a line shape
fig.add_shape(
    type="line",
    x0=center_x, y0=center_y,
    x1=end_x, y1=end_y,
    line=dict(color="black", width=6),
    xref="paper", yref="paper"
)

# Add a circle at the center for the clock hand base
fig.add_shape(
    type="circle",
    x0=center_x-0.025, y0=center_y-0.025,
    x1=center_x+0.025, y1=center_y+0.025,
    fillcolor="black",
    line_color="black",
    xref="paper", yref="paper"
)

fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    height=400
)

st.plotly_chart(fig, use_container_width=True)

# Display the average value below the gauge
st.markdown(
    f"<div style='text-align:center; font-size:2em; margin-top:-30px;'>Average: <b>{average}</b></div>",
    unsafe_allow_html=True
)


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