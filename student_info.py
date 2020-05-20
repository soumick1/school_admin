import csv

def write_into_csvfile(list):
    with open('student_info.csv','a',newline='')as csv_file:
        f=csv.writer(csv_file)

        if csv_file.tell()==0:
            f.writerow(["Name","Age","Contact Number","Email ID"])

        f.writerow(list)    

if __name__=='__main__':
    condition=True
    student_no=1

    while(condition):
        student_data=input("Enter the student data for the student no.{} in the format (Name Age Contact_no Email_ID): ".format(student_no))
        student_data_list=student_data.split(' ')

        print("\nThe entered info is:\nName: {}\nAge: {}\nContact no.: {}\nEmail ID: {}\n".format(student_data_list[0],student_data_list[1],student_data_list[2],student_data_list[3]))
     
        b=True
        while(b):
            check=input("Is the entered data correct?(yes/no): ") 

            if check=="yes":
                write_into_csvfile(student_data_list)
                b=False
                a=True
                while(a):
                    condition_check=input("Do you want to enter data for another student?(yes/no): ")
                    if condition_check=="yes":
                        condition=True
                        student_no+=1
                        a=False
                    elif condition_check=="no":
                        condition=False
                        a=False
                    else:
                        print("Invalid entry\nPlease enter valid answer!\n")
                
            elif check=="no":
                print("Please re-enter the data")
                b=False

            else:
                print("Invalid entry\nPlease enter valid answer!\n")
    
