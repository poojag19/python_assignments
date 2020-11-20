# Project 1: NSTI Students Administration
# This program is used to store the data of students while admission which can be used to upload the National portal.
import csv

def write_info_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "DOB", "Gender", "Aadhar_Number", "Email_Id", "Mobile_Number", "Trade_Name", "Candidate_Type"])
            
        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True
    student_num = 1

    while(condition):
        student_info = input("Enter student information for student #{} in the following format(Name DOB Gender Aadhar_Number Email_Id Mobile_Number Trade_Name Candidate_Type): ".format(student_num))

        # split
        student_info_list = student_info.split(' ')

        print("\nThe entered information is -\nName: {}\nDob: {}\nGender: {}\nAadhar_Number: {}\nEmail_Id: {}\nMobile_Number: {}\nTrade: {}\nCandidate_Type: {}"
                 .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3],student_info_list[4],student_info_list[5],student_info_list[6],student_info_list[7]))

        choice_check = input("Is the entered information are correct? (yes/no):  ")

        if choice_check == "yes":
            write_info_csv(student_info_list)

            condition_check = input("Enter (yes/no) if you want to enter information for another student: ")
            if condition_check == "yes":
                condition = True
                student_num = student_num + 1
            elif condition_check == "no":
                condition = False
        elif choice_check == "no":
            print("\nPlease re-enter the values correctly!")

# Program ends here...
            
            
                             
                             
                    
