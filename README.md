# STUDENT-GRADE-MANAGER
Concepts: Dictionaries, file I/O, statistics, sorting
# 📚 Student Grade Manager

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Statistics](https://img.shields.io/badge/Statistics-Real--time-green.svg)]()
[![File I/O](https://img.shields.io/badge/File-JSON%20Storage-orange.svg)]()
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A **comprehensive student grade management system** that allows teachers and educators to track, analyze, and manage student grades efficiently. This is **Project 8** in my Python exercises series, demonstrating data management and statistical analysis.

## 🎯 Purpose

Provide an easy-to-use system for managing student academic records, calculating statistics, assigning letter grades, and tracking class performance. Perfect for teachers, tutors, or anyone learning Python data management.

## ✨ Features

### 📝 Student Management
- **Add Students** – Register new students with unique IDs
- **Record Grades** – Add multiple subjects and grades per student
- **Update Grades** – Modify existing grades when needed
- **Remove Students** – Delete student records with confirmation
- **View All Students** – See complete class roster

### 📊 Grade Analysis
- **Grade Calculator** – Automatic letter grade assignment (A, B, C, D, F)
- **GPA Calculation** – 4.0 scale GPA for each student
- **Class Statistics** – Average, highest, and lowest scores
- **Subject Analysis** – Performance breakdown by subject
- **Pass/Fail Tracking** – Identify struggling students

### 📈 Data Management
- **JSON Storage** – Persistent data保存在 `students.json`
- **Sorting Options** – Sort by name, GPA, or ID
- **Search Functionality** – Find students by name or ID
- **Data Export** – Export reports to CSV format
- **Backup System** – Automatic backup before modifications

### 🎨 User Interface
- **Clean Tables** – Formatted display with borders
- **Color Coding** – Visual grade indicators (A=Green, F=Red)
- **Progress Bars** – Visual representation of scores
- **Interactive Menu** – Easy-to-navigate options

## 🧠 Concepts Covered

| Concept | Implementation |
|---------|----------------|
| **Dictionaries** | Store student data with nested grade records |
| **File I/O** | JSON serialization for persistent storage |
| **Statistics** | Mean, median, mode calculations for grades |
| **Sorting Algorithms** | Multi-criteria sorting (name, GPA, ID) |
| **List Comprehensions** | Efficient data filtering and transformation |
| **Error Handling** | Try-except for file operations and input validation |
| **Data Validation** | Grade range checking (0-100) |
| **String Formatting** | Pretty table printing with alignment |

## 🚀 How to Run

### Prerequisites
- Python 3.6 or higher
- No external libraries required! (uses only standard library)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mhasanpy/STUDENT-GRADE-MANAGER.git
   cd STUDENT-GRADE-MANAGER
