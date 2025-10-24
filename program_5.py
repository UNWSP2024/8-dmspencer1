# Title: Course Info
# Author: Dalila Spencer
# Date: 2025-10-23

# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.

courses = {}
repeat = 'y'

while repeat.lower() == 'y':

    courseID = input("Enter a course ID: ")
    courseName = input("Enter the course name: ")

    courses[courseID] = courseName

    repeat = input("Would you like to enter another course? y/n: ")

subject = input("Which subject would you like to see the courses for?: ")

for course in courses:
    if subject in course:
        print(course.strip(), courses[course].strip())
