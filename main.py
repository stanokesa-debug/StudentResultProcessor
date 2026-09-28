from student import Student


def build_sample_students() -> list[Student]:
    return [
        Student("Brian Mwangi", "REG005", [81, 76, 89]),
        Student("Mercy Achieng", "REG006", [67, 73, 70]),
        Student("Kevin Kamau", "REG007", [92, 85, 94]),
        Student("Faith Njeri", "REG008", [58, 64, 61]),
        Student("Collins Kiptoo", "REG009", [45, 52, 48]),
        Student("Sharon Wambui", "REG010", [76, 82, 79]),
    ]


def add_student_interactively(students: list[Student]) -> None:
    name = input("Student name: ").strip()
    reg_number = input("Registration number: ").strip()

    scores = []
    print("Enter scores one at a time. Type 'done' when finished.")
    while True:
        raw = input("  Score: ").strip()
        if raw.lower() == "done":
            break
        try:
            scores.append(float(raw))
        except ValueError:
            print("  Please enter a number, or 'done' to finish.")

    students.append(Student(name, reg_number, scores))
    print(f"Added {name}.\n")


def print_report(students: list[Student]) -> None:
    if not students:
        print("No students to display yet.")
        return

    print("\n" + "=" * 70)
    print("STUDENT RESULT REPORT")
    print("=" * 70)
    for student in students:
        print(student)
    print("=" * 70 + "\n")


def main() -> None:
    students = build_sample_students()

    while True:
        print("Menu:")
        print("  1. View report")
        print("  2. Add a student")
        print("  3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            print_report(students)
        elif choice == "2":
            add_student_interactively(students)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")


if __name__ == "__main__":
    main()