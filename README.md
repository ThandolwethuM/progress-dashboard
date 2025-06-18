# Student Progress Dashboard

This project is a Streamlit application designed to display a progress dashboard for students. It provides an interactive interface for viewing student information and their academic performance.

## Project Structure

```
student-progress-dashboard
├── src
│   ├── app.py               # Main entry point of the Streamlit application
│   ├── data
│   │   ├── students.csv     # Contains dummy data for student information
│   │   └── marks.csv        # Contains dummy data for student marks
│   └── utils
│       └── dashboard.py     # Utility functions for processing and visualizing data
├── requirements.txt         # Required Python packages for the project
└── README.md                # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd student-progress-dashboard
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit application:
   ```
   streamlit run src/app.py
   ```

## Usage Guidelines

- Upon running the application, you will be presented with a dashboard displaying student information and their marks.
- You can filter and visualize data based on different criteria to gain insights into student performance.

## Features

- View student details such as ID, name, age, and class.
- Access marks obtained in various subjects.
- Interactive charts and visualizations to analyze student performance trends.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.