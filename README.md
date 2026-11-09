# 🎓 Student Result Processor

![Python](https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-Educational-green)
![Status](https://img.shields.io/badge/Status-Learning%20Project-orange)

A Python command-line application for managing student academic results: register students, record examination scores, calculate averages, and classify performance automatically.

---

## 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Technologies Used](#️-technologies-used)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [Installation and Setup](#️-installation-and-setup)
- [How to Use the Application](#-how-to-use-the-application)
- [Grading and Result Classification](#-grading-and-result-classification)
- [Object-Oriented Programming (OOP) Concepts](#-object-oriented-programming-oop-concepts)
- [Current System Limitations](#️-current-system-limitations)
- [Future Enhancements](#-future-enhancements)
- [Learning Objectives](#-learning-objectives)
- [Developer Information](#-developer-information)
- [License](#-license)

---

## 📌 Project Overview

The **Student Result Processor** is a Python-based application developed to simplify the management and processing of student academic results.

The system allows users to register students, enter examination scores, calculate average marks, and automatically classify academic performance.

The project demonstrates fundamental Python programming concepts, particularly Object-Oriented Programming (OOP), modular programming, functions, lists, loops, and conditional statements.

It provides a simple command-line interface (CLI) through which users can interact with the application.

---

## ✨ Key Features

- **Student Registration:** Add new students using their names and registration numbers.
- **Examination Score Management:** Enter multiple examination scores for each student.
- **Automatic Average Calculation:** Calculate the average marks for every student.
- **Result Classification:** Automatically classify students based on their average scores.
- **Student Reports:** Display student details and academic performance.
- **Interactive Menu:** Navigate through the application using a simple menu-driven system.
- **Sample Student Records:** Includes sample data for testing and demonstration.

---

## 🛠️ Technologies Used

| Technology | Description |
|---|---|
| Python 3 | Main programming language |
| OOP | Organizing code using classes and objects |
| Lists | Storing student records and examination scores |
| Functions | Organizing application operations |
| Conditional Statements | Processing academic classifications |
| Command-Line Interface | User interaction |

---

## 📂 Project Structure

```text
Student-Result-Processor/
│
├── main.py
│   └── Main application logic, menu,
│       student registration and reports.
│
├── student.py
│   └── Student class, average calculation
│       and result classification.
│
└── README.md
    └── Project documentation.
```

---

## 📋 Requirements

- **Python 3** installed on your system
- A terminal or command prompt
- Git (optional, only needed to clone the repository)
- No external libraries or additional dependencies

---

## ⚙️ Installation and Setup

Follow the steps below to install and run the application.

### Step 1: Install Python

Download Python 3 from the official website:

https://www.python.org/downloads/

Verify the installation by running:

```bash
python --version
```

### Step 2: Clone the Repository

Open your terminal and execute:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate into the project directory:

```bash
cd Student-Result-Processor
```

### Step 3: Run the Application

Execute the following command:

```bash
python main.py
```

For Linux or macOS, you can use:

```bash
python3 main.py
```

> **Note:** No external libraries or additional dependencies are required.

---

## 💻 How to Use the Application

After running the program, an interactive menu will appear:

```text
Menu:
  1. View report
  2. Add a student
  3. Exit

Choose an option (1-3):
```

### Option 1: View Report

Select `1` to display all registered students, their registration numbers, average marks, and academic classifications.

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

### Option 2: Add a Student

Select `2` to register a new student.

The system will request:

1. Student's full name.
2. Registration number.
3. Examination scores.

Example session:

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

### Option 3: Exit

Select `3` to terminate the application.

```text
Goodbye!
```

---

## 📊 Grading and Result Classification

The application automatically determines student performance using their average examination scores.

| Average Score | Classification |
|---|---|
| 80 – 100 | Distinction |
| 70 – 79.99 | Credit |
| 50 – 69.99 | Pass |
| Below 50 | Fail |

### Average Calculation Formula

\[
Average = \frac{\text{Total Scores}}{\text{Number of Subjects}}
\]

**Example:**

A student obtains the following marks:

- Mathematics: 80
- Programming: 75
- Networking: 90

\[
Average = \frac{80+75+90}{3}=81.67
\]

**Final classification:** Distinction

---

# 🧠 Object-Oriented Programming (OOP) Concepts

The Student Result Processor uses Object-Oriented Programming principles to organize student information and result-processing operations.

The following concepts are relevant to understanding the project and its implementation.

## 1. Encapsulation

Encapsulation is the concept of combining data (attributes) and the methods that operate on that data within a single class.

In this project, the `Student` class combines student information and result-processing methods.

Example:

```python
class Student:
    def __init__(self, name, reg_number, scores):
        self.name = name
        self.reg_number = reg_number
        self.scores = scores

    def calculate_average(self):
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)
```

**Explanation:**

The student's name, registration number, and examination scores are stored inside the `Student` class. The `calculate_average()` method operates on the student's stored scores.

This demonstrates encapsulation by grouping related data and functionality together.

## 2. Inheritance

Inheritance is an OOP concept that allows one class to acquire attributes and methods from another class.

**Current implementation:** The project does not explicitly implement inheritance because it contains only one main class, `Student`.

However, inheritance could be introduced by creating different student categories that inherit from a common parent class.

Example of a possible extension:

```python
class Student:
    def __init__(self, name, reg_number, scores):
        self.name = name
        self.reg_number = reg_number
        self.scores = scores

    def calculate_average(self):
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)


class UndergraduateStudent(Student):
    def get_student_type(self):
        return "Undergraduate"


class PostgraduateStudent(Student):
    def get_student_type(self):
        return "Postgraduate"
```

**Explanation:**

`UndergraduateStudent` and `PostgraduateStudent` inherit the attributes and methods of the parent `Student` class.

This allows different student categories to share common functionality while having their own specialized behavior.

## 3. Polymorphism

Polymorphism means "many forms." It allows different classes to implement the same method in different ways.

**Current implementation:** The project does not explicitly demonstrate polymorphism through multiple related classes.

However, it can be demonstrated by extending the application as follows:

```python
class Student:
    def classify_result(self):
        return "General Student Result"


class UndergraduateStudent(Student):
    def classify_result(self):
        return "Undergraduate Result"


class PostgraduateStudent(Student):
    def classify_result(self):
        return "Postgraduate Result"
```

**Explanation:**

All three classes have a method called `classify_result()`, but each class provides a different implementation.

This demonstrates polymorphism because the same method name produces different behavior depending on the object calling it.

## 4. Abstraction

Abstraction involves hiding unnecessary implementation details and exposing only the essential functionality to the user.

In this project, users interact with the application through simple functions such as:

- `calculate_average()`
- `classify_result()`
- `print_report()`

Users do not need to understand the internal calculations to obtain student results.

For a formal implementation of abstraction in Python, the `abc` module can be used to define abstract classes and methods.

**Explanation:**

The application simplifies result processing by allowing users to interact with straightforward operations without needing to understand all the underlying programming logic.

## 5. Summary of OOP Concepts

| OOP Concept | Meaning | Application in Project |
|---|---|---|
| Encapsulation | Combining data and methods in a class | Student class stores information and processes results |
| Inheritance | Acquiring properties and methods from another class | Can be implemented using different student categories |
| Polymorphism | Same method name with different implementations | Can be implemented through specialized student classes |
| Abstraction | Hiding internal complexity | Users interact with simple result-processing operations |

> **Important:** Encapsulation and basic abstraction are demonstrated in the existing application. Inheritance and polymorphism are illustrated as possible extensions rather than features already implemented in the original two-file code.

---

## ⚠️ Current System Limitations

The current version has the following limitations:

- Student information is temporarily stored in memory.
- Newly added students are lost when the program is closed.
- The system does not support editing student records.
- The system does not support deleting student records.
- Examination scores are not fully validated.
- There is no database integration.

---

## 🔮 Future Enhancements

The system can be improved by introducing:

1. SQLite or MySQL database integration.
2. Student record searching and filtering.
3. Updating and deleting student information.
4. Exporting student reports to PDF or Excel.
5. Graphical User Interface (GUI).
6. User authentication and access control.
7. Class performance statistics and analytics.
8. Full implementation of inheritance and polymorphism.

---

## 🎯 Learning Objectives

This project provides practical experience in:

- Understanding Python programming fundamentals.
- Implementing Object-Oriented Programming.
- Working with classes and objects.
- Understanding encapsulation, inheritance, polymorphism, and abstraction.
- Developing modular Python applications.
- Processing and analyzing student examination results.
- Building interactive command-line applications.

---

## 👨‍💻 Developer Information

**Developer:** Stanley Okesa

**Project:** Student Result Processor

**Programming Language:** Python

**Project Type:** Academic / Educational Project

**GitHub:** [Visit My GitHub Profile](https://github.com/stanokesa-debug)

---

## 📜 License

This project is intended for educational and learning purposes. You are free to explore, modify, and improve the source code.

---

⭐ If you find this project useful, consider giving the repository a star!

**Student Result Processor – Simplifying Student Academic Result Management.**
