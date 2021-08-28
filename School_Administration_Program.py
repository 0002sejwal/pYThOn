import csv


def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(['Name', 'Age', 'Contact_Number', 'E-Mail_I'])
        writer.writerow(info_list)


condition = True

while (condition):
    student_info = input(
        "Enter student info in the following format (Name Age Contact_Number E-Mail_Id) : ")

    # print(f"Entered information is  :  {student_info}")

    student_info_list = student_info.split(' ')
    # print(f"The split us information is {student_info_list}")
    print(
        f"\nThe Entered information is -\nName : {student_info_list[0]}\nAge : {student_info_list[1]}\nContact Number : {student_info_list[2]}\nEmail Id : {student_info_list[3]}\n")
    choice_check = input(
        "Is the entered information is correct ? (yes/no) : ").lower()
    if choice_check == 'yes':
        write_into_csv(student_info_list)

        condition_check = input(
            "Enter yes/no if you want to add info. for another student : ").lower()

        if condition_check == 'yes':
            condition = True
        elif condition_check == 'no':
            condition = False

    elif choice_check == 'no':
        print("Please enter the valid information !!")
