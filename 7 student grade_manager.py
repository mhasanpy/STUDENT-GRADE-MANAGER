# grade_manager.py
import json
import statistics
from datetime import datetime

class GradeManager:
    def __init__(self):
        self.students = {}
        self.filename = "grades.json"
        self.load_data()
    
    def add_student(self):
        """Add a new student"""
        name = input("\nStudent name: ").strip()
        
        if name in self.students:
            print("❌ Student already exists!")
            return
        
        self.students[name] = {
            "grades": {},
            "attendance": 0,
            "total_classes": 0
        }
        
        self.save_data()
        print(f"✅ Student '{name}' added!")
    
    def add_grade(self):
        """Add grade for a student"""
        name = input("\nStudent name: ").strip()
        
        if name not in self.students:
            print("❌ Student not found!")
            return
        
        subject = input("Subject: ").strip()
        
        try:
            grade = float(input("Grade (0-100): "))
            if not 0 <= grade <= 100:
                print("❌ Grade must be between 0 and 100!")
                return
            
            self.students[name]["grades"][subject] = grade
            self.save_data()
            print(f"✅ Grade {grade} added for {name} in {subject}")
        
        except ValueError:
            print("❌ Invalid grade!")
    
    def record_attendance(self):
        """Record student attendance"""
        name = input("\nStudent name: ").strip()
        
        if name not in self.students:
            print("❌ Student not found!")
            return
        
        present = input("Was student present? (y/n): ").lower()
        
        self.students[name]["total_classes"] += 1
        if present == 'y':
            self.students[name]["attendance"] += 1
        
        self.save_data()
        
        attendance_percentage = (self.students[name]["attendance"] / self.students[name]["total_classes"]) * 100
        print(f"✅ Attendance recorded! Current rate: {attendance_percentage:.1f}%")
    
    def view_student_report(self):
        """View detailed report for a student"""
        name = input("\nStudent name: ").strip()
        
        if name not in self.students:
            print("❌ Student not found!")
            return
        
        student = self.students[name]
        grades = student["grades"]
        
        print(f"\n📊 REPORT FOR {name.upper()}")
        print("="*50)
        
        if grades:
            print("\n📚 GRADES:")
            print("-"*30)
            for subject, grade in grades.items():
                print(f"  {subject:<15}: {grade:>5.1f}")
            
            avg_grade = statistics.mean(grades.values())
            print(f"\n📈 Average Grade: {avg_grade:.1f}")
            
            # Letter grade
            if avg_grade >= 90:
                letter = "A+"
            elif avg_grade >= 80:
                letter = "A"
            elif avg_grade >= 70:
                letter = "B"
            elif avg_grade >= 60:
                letter = "C"
            else:
                letter = "F"
            
            print(f"🎓 Letter Grade: {letter}")
        else:
            print("📚 No grades recorded yet!")
        
        # Attendance
        total = student["total_classes"]
        attended = student["attendance"]
        if total > 0:
            attendance_rate = (attended / total) * 100
            print(f"\n📅 ATTENDANCE:")
            print(f"   Classes held: {total}")
            print(f"   Classes attended: {attended}")
            print(f"   Attendance rate: {attendance_rate:.1f}%")
            
            if attendance_rate < 75:
                print("   ⚠️ Warning: Attendance below 75%!")
        else:
            print("\n📅 No attendance records yet!")
        
        print("="*50)
    
    def view_class_summary(self):
        """View summary statistics for the whole class"""
        if not self.students:
            print("No students in class!")
            return
        
        print("\n📊 CLASS SUMMARY")
        print("="*50)
        
        # Calculate class averages
        all_grades = []
        for student in self.students.values():
            all_grades.extend(student["grades"].values())
        
        if all_grades:
            avg_class_grade = statistics.mean(all_grades)
            print(f"📈 Class Average Grade: {avg_class_grade:.1f}")
            print(f"📚 Total Grades Recorded: {len(all_grades)}")
        
        # Attendance summary
        total_attendance = sum(s["attendance"] for s in self.students.values())
        total_classes = sum(s["total_classes"] for s in self.students.values())
        
        if total_classes > 0:
            overall_attendance = (total_attendance / total_classes) * 100
            print(f"📅 Overall Attendance Rate: {overall_attendance:.1f}%")
        
        # Student list
        print(f"\n👥 STUDENTS ({len(self.students)}):")
        print("-"*30)
        for i, name in enumerate(sorted(self.students.keys()), 1):
            student = self.students[name]
            if student["grades"]:
                avg = statistics.mean(student["grades"].values())
                print(f"  {i:2}. {name:<20} (Avg: {avg:.1f})")
            else:
                print(f"  {i:2}. {name:<20} (No grades)")
    
    def top_performers(self):
        """Show top performing students"""
        if not self.students:
            print("No students in class!")
            return
        
        # Calculate average for each student
        student_averages = []
        for name, data in self.students.items():
            if data["grades"]:
                avg = statistics.mean(data["grades"].values())
                student_averages.append((name, avg))
        
        if not student_averages:
            print("No grades recorded yet!")
            return
        
        # Sort by average (descending)
        student_averages.sort(key=lambda x: x[1], reverse=True)
        
        print("\n🏆 TOP PERFORMERS")
        print("="*50)
        for i, (name, avg) in enumerate(student_averages[:5], 1):
            medal = {1: "🥇", 2: "🥈", 3: "🥉"}.get(i, f"{i}.")
            print(f"{medal} {name:<20} - Average: {avg:.1f}")
    
    def save_data(self):
        """Save data to file"""
        with open(self.filename, 'w') as f:
            json.dump(self.students, f, indent=2)
    
    def load_data(self):
        """Load data from file"""
        try:
            with open(self.filename, 'r') as f:
                self.students = json.load(f)
        except FileNotFoundError:
            self.students = {}

def main():
    manager = GradeManager()
    
    while True:
        print("\n📚 GRADE MANAGER")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. Record Attendance")
        print("4. View Student Report")
        print("5. View Class Summary")
        print("6. View Top Performers")
        print("7. Exit")
        
        choice = input("Choose (1-7): ")
        
        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.add_grade()
        elif choice == "3":
            manager.record_attendance()
        elif choice == "4":
            manager.view_student_report()
        elif choice == "5":
            manager.view_class_summary()
        elif choice == "6":
            manager.top_performers()
        elif choice == "7":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()