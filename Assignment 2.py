class University:
    def __init__(self):
        self.students_list = []
        self.courses_list = []
        self.lecturers_list = []

    def add_student(self, student_name):
        """Add a student to the university."""
        self.students_list.append(student_name)
        print(f"Student '{student_name}' added.")

    def get_students(self):
        """Return the list of students."""
        return self.students_list

    def add_course(self, course_name):
        """Add a course to the university."""
        self.courses_list.append(course_name)
        print(f"Course '{course_name}' added.")

    def get_courses(self):
        """Return the list of courses."""
        return self.courses_list

    def add_lecturer(self, lecturer_name):
        """Add a lecturer to the university."""
        self.lecturers_list.append(lecturer_name)
        print(f"Lecturer '{lecturer_name}' added.")

    def get_lecturers(self):
        """Return the list of lecturers."""
        return self.lecturers_list
