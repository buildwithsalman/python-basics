class student:
    def __init__(self,name , marks1, marks2, marks3):
        self.name = name 
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

s1 = student(input("Enter students name: "), int(input("subject 1 marks: ")), int(input("subject 2 marks: ")), int(input("subject 3 marks: ")))
average = (s1.marks1 + s1.marks2 + s1.marks3)/3
print(f"average of marks of {s1.name} is {average}")