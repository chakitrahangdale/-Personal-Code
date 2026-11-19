
import json
import random
from pathlib import Path

DATA_FILE = "students.json"


class Student:
    def __init__(self):
        self.rollNo = ""
        self.name = ""
        self.course = ""
        self.dob = ""
        self.address = ""

        self.semester = 1
        self.age = 18
        self.semestersCompleted = 1
        self.attendance = 75

        self.grades = ["-"] * 8
        self.marks = [0.0] * 8

    def totalMarks(self):
        return sum(self.marks[:self.semestersCompleted])

    def cgpa(self):
        if self.semestersCompleted <= 0:
            return 0.0

        gp = 0

        for mark in self.marks[:self.semestersCompleted]:
            if mark >= 90:
                gp += 10
            elif mark >= 75:
                gp += 8
            elif mark >= 60:
                gp += 6
            elif mark >= 40:
                gp += 4

        return gp / self.semestersCompleted

    def isPass(self):
        return all(
            mark >= 40
            for mark in self.marks[:self.semestersCompleted]
        )

    def display(self):
        print("\nRoll No    :", self.rollNo)
        print("Name       :", self.name)
        print("Course     :", self.course)
        print("Semester   :", self.semester)
        print("Age        :", self.age)
        print("DOB        :", self.dob)
        print("Address    :", self.address)
        print("Attendance :", self.attendance, "%")

        for i in range(self.semestersCompleted):
            print(
                f"Sem {i+1} | Grade: {self.grades[i]} | Marks: {self.marks[i]}"
            )

        print("Total Marks:", self.totalMarks())
        print("CGPA       :", round(self.cgpa(), 2))
        print("Result     :", "PASS" if self.isPass() else "FAIL")
        print("-------------------------")

    def inputAdd(self):
        self.rollNo = input("Enter Roll No: ")
        self.name = input("Enter Name: ")
        self.course = input("Enter Course: ")
        self.dob = input("Enter DOB: ")

        self.age = int(input("Enter Age: "))
        self.semester = int(input("Enter Current Semester: "))

        self.semestersCompleted = int(
            input("Enter Semesters Completed (1-8): ")
        )

        self.semestersCompleted = max(
            1, min(8, self.semestersCompleted)
        )

        self.address = input("Enter Address: ")

        for i in range(self.semestersCompleted):
            self.grades[i] = input(f"Grade Sem {i+1}: ")
            self.marks[i] = float(input(f"Marks Sem {i+1}: "))

    def inputUpdate(self):
        print(
            "\nUpdating Semester / Semesters Completed / Address / Grades / Marks"
        )

        self.semester = int(input("Enter New Semester: "))

        self.semestersCompleted = int(
            input("Enter Semesters Completed (1-8): ")
        )

        self.semestersCompleted = max(
            1, min(8, self.semestersCompleted)
        )

        self.address = input("Enter New Address: ")

        for i in range(self.semestersCompleted):
            self.grades[i] = input(f"Grade Sem {i+1}: ")
            self.marks[i] = float(input(f"Marks Sem {i+1}: "))


class StudentManager:

    def __init__(self):
        self.students = []

    def loadDefaultData(self):
        names = [
            "AARTI THAKRE", "AAYUSH BHAGAT",
            "AISHWARYA SONWANE", "ALOK UIKEY",
            "ANEESA KARPETI", "ANSHIKA PATEL",
            "AYUSHI RAI", "CHAHAT PATHAK",
            "CHAKIT RAHANGDALE", "DEVESH KUMAR SHIVAM",
            "GOPAL SHILPI", "HARSH SAHU",
            "HIMANSHU SOLANKI", "KAJAL PATLE",
            "MANSI AHIRWAR", "NEELESH KORI",
            "NIKHIL MISHRA", "NITISH KUMAR",
            "PRACHI THAKRE", "SANU PATLE"
        ]

        dob = [
            "22/08/2004", "10/12/2005", "03/07/2004",
            "18/09/2005", "25/11/2004", "07/04/2005",
            "14/06/2004", "29/01/2005", "12/03/2004",
            "21/10/2005", "05/02/2004", "30/07/2005",
            "16/11/2004", "09/08/2005", "27/12/2004",
            "04/05/2005", "19/09/2004", "02/06/2005",
            "13/10/2004", "02/09/2005"
        ]

        addresses = [
            "Bhopal", "Indore", "Jabalpur", "Raipur",
            "Bilaspur", "Korba", "Raigarh", "Durg",
            "Bhilai", "Ambikapur", "Jagdalpur",
            "Rajnandgaon", "Kawardha", "Mahasamund",
            "Dhamtari", "Balod", "Gariaband",
            "Bemetara", "Mungeli", "Seoni"
        ]

        grades = [
            ['B', 'A', 'B'], ['A', 'A', 'A'],
            ['B', 'B', 'A'], ['A', 'B', 'B'],
            ['B', 'A', 'A'], ['A', 'A', 'B'],
            ['B', 'B', 'A'], ['A', 'B', 'A'],
            ['B', 'A', 'B'], ['A', 'A', 'A'],
            ['B', 'B', 'B'], ['A', 'B', 'A'],
            ['B', 'A', 'A'], ['A', 'A', 'B'],
            ['B', 'B', 'A'], ['A', 'B', 'B'],
            ['B', 'A', 'A'], ['A', 'A', 'A'],
            ['B', 'B', 'B'], ['A', 'B', 'B']
        ]

        marks = [
            [79, 88, 75], [90, 95, 89], [76, 82, 87],
            [88, 80, 84], [81, 91, 86], [93, 89, 78],
            [77, 85, 90], [87, 79, 91], [80, 86, 76],
            [92, 94, 88], [75, 83, 81], [89, 78, 93],
            [82, 90, 85], [91, 87, 79], [78, 84, 92],
            [86, 81, 83], [79, 89, 87], [94, 92, 90],
            [76, 80, 82], [91, 81, 80]
        ]

        self.students.clear()

        for i in range(20):
            s = Student()

            s.rollNo = f"0546CL2410{i+1:02d}"
            s.name = names[i]
            s.course = "AIML"
            s.semester = 3
            s.age = random.randint(18, 21)
            s.semestersCompleted = 3
            s.dob = dob[i]
            s.address = addresses[i]
            s.attendance = random.randint(70, 94)

            for j in range(3):
                s.grades[j] = grades[i][j]
                s.marks[j] = marks[i][j]

            self.students.append(s)

    def addStudent(self):
        s = Student()
        s.inputAdd()
        self.students.append(s)
        print("Student Added Successfully")

    def updateStudent(self):
        print("\nUpdate Student By:")
        print("1. Roll No")
        print("2. Name")

        ch = input("Enter choice: ")

        if ch == "1":
            r = input("Enter Roll No: ")

            for s in self.students:
                if s.rollNo == r:
                    s.inputUpdate()
                    print("Student Updated")
                    return

        elif ch == "2":
            n = input("Enter Name: ")

            for s in self.students:
                if s.name.lower() == n.lower():
                    s.inputUpdate()
                    print("Student Updated")
                    return

        print("Student Not Found")

    def deleteStudent(self):
        n = input("Enter Name to Delete: ")

        old_count = len(self.students)

        self.students = [
            s for s in self.students
            if s.name.lower() != n.lower()
        ]

        if len(self.students) < old_count:
            print("Student Deleted")
        else:
            print("Student Not Found")

    def viewAll(self):
        if not self.students:
            print("No Students Found")
            return

        for s in self.students:
            s.display()

    def sortStudents(self):
        print("\nSort By:")
        print("1. Roll")
        print("2. Name")
        print("3. Total Marks")

        c = input("Choice: ")

        if c == "1":
            self.students.sort(key=lambda s: s.rollNo)

        elif c == "2":
            self.students.sort(key=lambda s: s.name)

        elif c == "3":
            self.students.sort(
                key=lambda s: s.totalMarks(),
                reverse=True
            )

        else:
            print("Invalid Choice")
            return

        print("Sorted Successfully")

    def searchByRoll(self):
        r = input("Enter Roll No: ")

        for s in self.students:
            if s.rollNo == r:
                s.display()
                return

        print("Not Found")

    def searchByName(self):
        key = input("Enter Name to Search: ").lower()
        found = False

        for s in self.students:
            if key in s.name.lower():
                s.display()
                found = True

        if not found:
            print("Not Found")

    def saveToFile(self):
        data = []

        for s in self.students:
            data.append({
                "rollNo": s.rollNo,
                "name": s.name,
                "course": s.course,
                "dob": s.dob,
                "address": s.address,
                "semester": s.semester,
                "age": s.age,
                "semestersCompleted": s.semestersCompleted,
                "attendance": s.attendance,
                "grades": s.grades,
                "marks": s.marks
            })

        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

        print("Saved Successfully:", DATA_FILE)

    def loadFromFile(self):
        if not Path(DATA_FILE).exists():
            print("File Not Found")
            return

        try:
            with open(DATA_FILE, "r") as file:
                data = json.load(file)

            loaded_students = []

            for item in data:
                s = Student()

                s.rollNo = item["rollNo"]
                s.name = item["name"]
                s.course = item["course"]
                s.dob = item["dob"]
                s.address = item["address"]
                s.semester = item["semester"]
                s.age = item["age"]
                s.semestersCompleted = item["semestersCompleted"]
                s.attendance = item["attendance"]
                s.grades = item["grades"]
                s.marks = item["marks"]

                loaded_students.append(s)

            self.students = loaded_students
            print("Loaded Successfully:", DATA_FILE)

        except (json.JSONDecodeError, KeyError, TypeError) as e:
            print("Unable to load data:", e)

    def top3(self):
        temp = sorted(
            self.students,
            key=lambda s: s.totalMarks(),
            reverse=True
        )

        print("\n--- TOP 3 STUDENTS ---")

        for s in temp[:3]:
            s.display()

    def exportReport(self):
        r = input("Enter Roll No: ")

        for s in self.students:
            if s.rollNo == r:
                filename = f"{r}_report.txt"

                with open(filename, "w") as file:
                    file.write(f"Roll No: {s.rollNo}\n")
                    file.write(f"Name: {s.name}\n")
                    file.write(f"Course: {s.course}\n")
                    file.write(f"Semester: {s.semester}\n")
                    file.write(f"Address: {s.address}\n")
                    file.write(f"Total Marks: {s.totalMarks()}\n")
                    file.write(f"CGPA: {s.cgpa():.2f}\n")
                    file.write(
                        f"Result: {'PASS' if s.isPass() else 'FAIL'}\n"
                    )

                    for i in range(s.semestersCompleted):
                        file.write(
                            f"Sem {i+1} | Grade: {s.grades[i]} | "
                            f"Marks: {s.marks[i]}\n"
                        )

                print("Report Generated:", filename)
                return

        print("Student Not Found")

    def searchByCourse(self):
        c = input("Enter Course: ").lower()
        found = False

        for s in self.students:
            if s.course.lower() == c:
                s.display()
                found = True

        if not found:
            print("Not Found")

    def searchBySemester(self):
        sem = int(input("Enter Semester: "))
        found = False

        for s in self.students:
            if s.semester == sem:
                s.display()
                found = True

        if not found:
            print("Not Found")


def login():
    print("\n--- ADMIN LOGIN ---")

    u = input("Username: ")
    p = input("Password: ")

    return u == "VGI" and p == "0546"


def main():
    if not login():
        print("Access Denied")
        return

    manager = StudentManager()
    manager.loadDefaultData()

    while True:
        print("\n--- STUDENT MANAGEMENT SYSTEM ---")
        print("1. Add Student")
        print("2. View All Student")
        print("3. Search by Roll No")
        print("4. Search by Name")
        print("5. Update Student")
        print("6. Delete Student")
        print("7. Sort Student")
        print("8. Save to File")
        print("9. Load from File")
        print("10. Student CGPA/Result")
        print("11. Advanced Search")
        print("12. Top 3 Student")
        print("13. Export Report")
        print("14. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                manager.addStudent()

            elif choice == 2:
                manager.viewAll()

            elif choice == 3:
                manager.searchByRoll()

            elif choice == 4:
                manager.searchByName()

            elif choice == 5:
                manager.updateStudent()

            elif choice == 6:
                manager.deleteStudent()

            elif choice == 7:
                manager.sortStudents()

            elif choice == 8:
                manager.saveToFile()

            elif choice == 9:
                manager.loadFromFile()

            elif choice == 10:
                manager.viewAll()

            elif choice == 11:
                print("\n1. Search by Course")
                print("2. Search by Semester")

                opt = input("Enter option: ")

                if opt == "1":
                    manager.searchByCourse()

                elif opt == "2":
                    manager.searchBySemester()

                else:
                    print("Invalid Option")

            elif choice == 12:
                manager.top3()

            elif choice == 13:
                manager.exportReport()

            elif choice == 14:
                print("Exiting Program...")
                break

            else:
                print("Invalid Choice")

        except ValueError:
            print("Invalid Input! Enter a valid number.")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
