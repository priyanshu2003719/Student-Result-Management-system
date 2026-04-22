# Student-Result-Management-System
Developed desktop application using Python (Tkinter) for managing student records and results. 

# 🎓 Student Result Management System
**An Advanced Academic Administration Suite** **with a robust, desktop-based management solution developed in Python to streamline student registration, course administration, and academic performance tracking.**

---

## 🏗️ Project Architecture & File Breakdown

### 🖥️ Core Interface & Application Flow
| File | Section | Description |
| :--- | :--- | :--- |
| **`login.py`** | **Security Gateway** | The primary entry point. Features a secure authentication system with login credentials, "Forgot Password" recovery, and a dynamic analog clock for a modern aesthetic. |
| **`register.py`** | **User Provisioning** | Handles administrative account creation. Includes form validation, security question integration, and encrypted-style password confirmation stored in the database. |
| **`dashboard.py`** | **Control Center** | The heart of the application. It provides a centralized GUI to navigate between students, courses, results, and reports. It features real-time data statistics and system-wide logout functionality. |

### 📂 Academic Management Modules
| File | Section | Description |
| :--- | :--- | :--- |
| **`student.py`** | **Enrollment Manager** | A comprehensive CRUD (Create, Read, Update, Delete) module for student profiles. Manages sensitive data including contact info, admission dates, and course affiliations. |
| **`course.py`** | **Curriculum Architect** | Facilitates the management of academic programs. Allows administrators to define course names, durations, and fee structures with an integrated search filter. |
| **`result.py`** | **Grading Engine** | Automates the calculation of academic results. It links student roll numbers with specific courses to compute percentages and grade distributions dynamically. |
| **`report.py`** | **Performance Analytics** | A dedicated view for searching and analyzing individual student progress. It generates a clean, readable summary of marks and academic standing. |

### ⚙️ Backend & Utility Services
| File | Section | Description |
| :--- | :--- | :--- |
| **`create_db.py`** | **Database Schema** | The automated setup script. It initializes the SQLite environment, defining relational tables for students, courses, results, and administrative credentials. |
| **`clock.py`** | **UI Components** | A reusable utility script that renders a high-precision analog clock using mathematical trigonometry and the Pillow (PIL) library. |
| **`rms.db`** | **Data Warehouse** | The persistent SQLite database engine storing all relational data, ensuring system integrity and lightning-fast query response times. |

---

## 🛠️ Tech Stack & Dependencies
* **Language:** Python 3.x
* **GUI Framework:** Tkinter (Standard Python Interface)
* **Image Processing:** Pillow (PIL)
* **Database:** SQLite3
* **Visual Assets:** Vector graphics for a professional UI/UX experience

## 🚀 Key Features
* ✅ **Real-time Synchronization:** Data updates across the dashboard instantly.
* ✅ **Secure Authentication:** Multi-layered login and registration system.
* ✅ **Dynamic Search:** Advanced filtering capabilities in every management module.
* ✅ **Automated Calculations:** Built-in logic for percentage and performance metrics.
* ✅ **Responsive UI:** A clean, orange-and-blue themed professional interface.
