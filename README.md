# 🎓 Student Result Processor

## 📌 Project Description

**Student Result Processor** is a simple Python-based application designed to manage and process students' academic results. The system allows users to view student records, add new students, calculate their average scores, and automatically classify their academic performance.

The project demonstrates basic Python programming concepts, including Object-Oriented Programming (OOP), classes, functions, lists, loops, conditional statements, user input, and data processing.

It is designed to make student result management easier, faster, and more organized.

## ✨ Features

The Student Result Processor provides the following features:

- **View Student Reports:** Display all registered students alongside their registration numbers, average scores, and academic classifications.
- **Add New Students:** Allow users to enter a student's name and registration number.
- **Enter Exam Scores:** Accept multiple examination scores for each student.
- **Automatic Average Calculation:** Calculate the average score using the student's entered marks.
- **Automatic Result Classification:** Classify students according to their average performance.
- **Interactive Menu:** Provide a simple menu-driven interface for easy navigation.
- **Sample Student Records:** Include sample student data for testing and demonstration.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| Object-Oriented Programming | Organizing student records using classes |
| Lists | Storing student records and examination scores |
| Functions | Organizing program operations |
| Conditional Statements | Determining student performance |
| Terminal/Command Prompt | Running the application |

## 📂 Project Structure

Organize your project files as follows:

```text
Student-Result-Processor/
│
├── main.py
│   └── Main application file containing
│       the menu and program functionality.
│
├── student.py
│   └── Contains the Student class,
│       average calculation and result classification.
│
└── README.md
    └── Project documentation.
```

**Important:** Both `main.py` and `student.py` should be saved in the same project folder because the main application imports the Student class from `student.py`.

## ⚙️ Requirements

Before running the application, make sure you have:

1. Python 3 installed on your computer.
2. A code editor such as Visual Studio Code (VS Code), PyCharm, or any text editor.
3. A terminal or command prompt.

No external Python libraries are required because the application uses Python's built-in functionality.

## 🚀 How to Install and Run the Project

Follow these steps to get the application running on your computer.

### Step 1: Install Python

Download and install Python 3 from the official website:

https://www.python.org/downloads/

After installation, verify that Python is working by opening your terminal and typing:

```bash
python --version
```

On some systems, use:

```bash
python3 --version
```

### Step 2: Download or Clone the Repository

You can download the project directly from GitHub or clone it using Git.

Run the following command:

```bash
https://github.com/stanokesa-debug/StudentResultProcessor
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

Navigate into the project directory:

```bash
cd Student-Result-Processor
```

### Step 3: Check Your Project Files

Make sure your folder contains:

- `main.py`
- `student.py`
- `README.md`

### Step 4: Run the Application

Open your terminal inside the project directory and execute:

```bash
python main.py
```

Alternatively, use:

```bash
python3 main.py
```

The application will start and display an interactive menu.

## 💻 How to Use the Application

When you run the program, the following menu appears:

```text
Menu:
  1. View report
  2. Add a student
  3. Exit

Choose an option (1-3):
```

### Option 1: View Student Report

Enter `1` to display all available student records.

Example output:

```text
======================================================================
STUDENT RESULT REPORT
======================================================================
REG005 | Brian Mwangi         | Average:  82.00 | Result: Distinction
REG006 | Mercy Achieng         | Average:  70.00 | Result: Credit
REG007 | Kevin Kamau           | Average:  90.33 | Result: Distinction
REG008 | Faith Njeri           | Average:  61.00 | Result: Pass
REG009 | Collins Kiptoo        | Average:  48.33 | Result: Fail
REG010 | Sharon Wambui         | Average:  79.00 | Result: Credit
======================================================================
```

### Option 2: Add a New Student

Enter `2` to register a new student.

The application will request:

1. Student's name.
2. Registration number.
3. Examination scores.

Example:

```text
Student name: John Kamau
Registration number: REG011

Enter scores one at a time. Type 'done' when finished.

Score: 80
Score: 75
Score: 90
Score: done

Added John Kamau.
```

The application automatically calculates the student's average and classifies their results when you view the report.

### Option 3: Exit the Application

Enter `3` to close the application.

```text
Goodbye!
```

## 📊 Student Result Classification

The application automatically classifies students according to their average examination scores.

The grading criteria are:

| Average Score | Classification |
|---|---|
| 80 – 100 | Distinction |
| 70 – 79.99 | Credit |
| 50 – 69.99 | Pass |
| Below 50 | Fail |

### How Average Scores Are Calculated

The application calculates the average by adding all examination scores and dividing the total by the number of scores entered.

**Formula:**

```text
Average = Total Examination Scores / Number of Subjects
```

**Example:**

A student obtains the following scores:

- Mathematics: 80
- Programming: 75
- Networking: 90

Calculation:

```text
Average = (80 + 75 + 90) / 3

Average = 81.67
```

Final classification: **Distinction**

## 🧠 Understanding the Student Class

The application uses Object-Oriented Programming (OOP) to organize student information.

The `Student` class is responsible for representing individual students and processing their academic results.

It contains the following attributes:

| Attribute | Description |
|---|---|
| name | Stores the student's full name |
| reg_number | Stores the student's registration number |
| scores | Stores the student's examination marks |

It also contains the following methods:

| Method | Function |
|---|---|
| `calculate_average()` | Calculates the average examination score |
| `classify_result()` | Determines the student's academic classification |
| `__str__()` | Formats student information for display |

## ⚠️ Important Notes

- The application comes with six sample student records.
- Newly added students are available during the current program session.
- Student records are stored in memory and are not permanently saved to a database or file.
- Restarting the application restores the original sample records and removes students added during the previous session.
- The program accepts numerical scores but does not currently enforce a maximum score of 100.
- The program does not require an internet connection to operate.

## 🔮 Future Improvements

The project can be improved by introducing additional functionality, including:

- Permanent storage of student records using a database such as SQLite or MySQL.
- Editing existing student information.
- Deleting student records.
- Searching for students using registration numbers.
- Generating downloadable student result reports.
- Adding input validation for examination scores.
- Creating a graphical user interface (GUI).
- Generating class performance statistics.

## 🎯 Learning Objectives

This project demonstrates practical application of the following programming concepts:

1. Object-Oriented Programming (OOP).
2. Python classes and objects.
3. Functions and methods.
4. Lists and data structures.
5. Loops and conditional statements.
6. User input and output.
7. Basic data processing and calculations.
8. Modular programming using multiple Python files.

## 👨‍💻 Author

**Stanley Okesa**

Computer Science / Information Technology Student

GitHub: [Your GitHub Profile](https://github.com/)

## 📜 License

This project is available for educational and learning purposes. You are welcome to study, modify, and improve the source code.

---

⭐ **If you find this project useful, consider giving the repository a star on GitHub!**

