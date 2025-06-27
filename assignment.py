class Course :
    def __init__(self , title , grade):
        self.title = title
        self.grade = grade
    def  is_failed(self):
            return self.grade < 51


class Student:
    def __init__(self, first_name , last_name , age , courses):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.courses = courses
    def get_full_name(self):
         return self.first_name + " " + self.last_name 
    def calculate_gpa(self):
         if not self.courses:
              return 0
         total = 0
         for course in self.courses:
              total += course.grade
         return total/len(self.courses) 
    def get_courses_by_status(self ,status):
         filtered_courses = []
         for course in self.courses:
            if status == 'failed'and course.is_failed() is True:
              filtered_courses.append(course.title)
            elif status == 'passed' and not course.is_failed():
                 filtered_courses.append(course.title)
         return filtered_courses
    def Calculate_gpa(self):
         if not self.courses:
              return 0 
         return sum(course.grade for course in self.courses)/len(self.courses)
import random
with open ('first_names.txt') as f:
     first_names = [line.strip() for line in f]
with open ('last_names.txt') as f:
     last_names = [line.strip() for line in f]
with open ('courses.txt') as f:
     courses = [line.strip() for line in f]
student_courses = []

first_name = random.choice(first_names)
last_name = random.choice(last_names)
age = random.randint(18,25)
for i in range(10):
     title = random.choice(courses)
     grade = random.randint(0,100)
     course = Course(title , grade)
     student_courses.append(course)
student = Student(first_name , last_name , age , student_courses)
print(student)
     
     