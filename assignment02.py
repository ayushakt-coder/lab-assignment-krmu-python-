"""
GradeBook Analyzer
Course: Programming for Problem Solving using Python
Assignment: Analyzing and Reporting Student Grades
Author: [Ayush Kumar Thakur]
Date: [05 November 2025]
"""

import csv
import statistics
# Welcome Message and Menu
def print_welcome():
    print("=" * 50)
    print("      🎓 GRADEBOOK ANALYZER - CLI VERSION 🎓      ")
    print("=" * 50)
    print("Choose an option:")
    print("1. Enter marks manually")
    print("2. Load marks from CSV file")
    print("3. Exit")
    print("=" * 50)

# Task 2: Data Entry or CSV Import

def manual_input():
    marks_dict = {}
    n = int(input("Enter number of students: "))
    for _ in range(n):
        name = input("Enter student name: ")
        marks = float(input(f"Enter marks for {name}: "))
        marks_dict[name] = marks
    return marks_dict


def csv_input():
    marks_dict = {}
    file_path = input("Enter CSV file path (e.g., marks.csv): ")
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip header if exists
            for row in reader:
                if len(row) >= 2:
                    name, marks = row[0], float(row[1])
                    marks_dict[name] = marks
        print("✅ CSV data loaded successfully!")
    except FileNotFoundError:
        print("❌ File not found. Please check the path.")
    return marks_dict

# Task 3: Statistical Analysis Functions

def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)


def calculate_median(marks_dict):
    return statistics.median(marks_dict.values())


def find_max_score(marks_dict):
    return max(marks_dict.values())


def find_min_score(marks_dict):
    return min(marks_dict.values())

# Task 4: Grade Assignment and Distribution

def assign_grades(marks_dict):
    grades = {}
    for name, mark in marks_dict.items():
        if mark >= 90:
            grades[name] = "A"
        elif mark >= 80:
            grades[name] = "B"
        elif mark >= 70:
            grades[name] = "C"
        elif mark >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"
    return grades


def grade_distribution(grades):
    dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for g in grades.values():
        if g in dist:
            dist[g] += 1
    return dist

# Task 5: Pass/Fail Filter with List Comprehension

def pass_fail_filter(marks_dict):
    passed_students = [name for name, score in marks_dict.items() if score >= 40]
    failed_students = [name for name, score in marks_dict.items() if score < 40]

    print(f"\n✅ Passed Students ({len(passed_students)}): {', '.join(passed_students)}")
    print(f"❌ Failed Students ({len(failed_students)}): {', '.join(failed_students)}")

# Task 6: Results Table and User Loop

def display_results(marks_dict, grades):
    print("\n---------------------------------------------")
    print(f"{'Name':<15}{'Marks':<10}{'Grade':<10}")
    print("---------------------------------------------")
    for name in marks_dict:
        print(f"{name:<15}{marks_dict[name]:<10}{grades[name]:<10}")
    print("---------------------------------------------")


def show_statistics(marks_dict):
    print("\n📊 Statistical Summary:")
    print(f"Average Marks : {calculate_average(marks_dict):.2f}")
    print(f"Median Marks  : {calculate_median(marks_dict):.2f}")
    print(f"Highest Marks : {find_max_score(marks_dict):.2f}")
    print(f"Lowest Marks  : {find_min_score(marks_dict):.2f}")


def main():
    while True:
        print_welcome()
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            marks_dict = manual_input()
        elif choice == "2":
            marks_dict = csv_input()
            if not marks_dict:
                continue
        elif choice == "3":
            print("👋 Exiting GradeBook Analyzer. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            continue

        grades = assign_grades(marks_dict)
        show_statistics(marks_dict)
        pass_fail_filter(marks_dict)
        display_results(marks_dict, grades)

        dist = grade_distribution(grades)
        print("\n📈 Grade Distribution:")
        for g, count in dist.items():
            print(f"Grade {g}: {count} student(s)")

        repeat = input("\nDo you want to analyze again? (y/n): ").lower()
        if repeat != "y":
            print("👋 Thank you for using GradeBook Analyzer!")
            break

if __name__ == "__main__":
    main()