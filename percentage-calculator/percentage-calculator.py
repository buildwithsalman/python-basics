sub_num = int(input("Enter the number of subjects you have: "))

obtained_list = []
out_of_list = []

n = 1
while n <= sub_num:
    print(f"Subject {n}:")
    obtained_list.append(int(input("  Marks obtained: ")))
    out_of_list.append(int(input("  Out of: ")))
    n += 1

m = 0
obtained_marks = 0
max_marks = 0
while m < sub_num:
    obtained_marks += obtained_list[m]
    max_marks += out_of_list[m]
    m += 1

percentage = (obtained_marks * 100) / max_marks
print("\nTotal Marks:", obtained_marks, "/", max_marks)
print("Percentage:", round(percentage, 2), "%")