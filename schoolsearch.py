#Index 0 LASTNAME: COOKUS, 
#Index 1 FIRSTNAME: XUAN, 
#Index 2 GRADE: 3, 
#Index 3 CLASSROOM: 107,
#Index 4 BUS ROUTE: 52,
#Index 5 GPA: 3.07, 
#Index 6 TEACHER LN: FAFARD,
#Index 7 TEACHER F: ROCIO
def main():
    # split into lines
    file = open('students.txt', 'r')
    #lines is a list of list, where each list is a line of the file. 
    # put into data structure
    lines = [line.strip().split(',') for line in file]
    #print(lines)


    # user_input = ""
    while(user_input != "Q"):
        user_input = input("Please enter a command:")
        split_input = user_input.split()
        if split_input[0] == "S" or split_input[0] == "Student":
            return
            #CODE
        elif split_input[0] == "T" or split_input[0] == "Teacher":
            return
        
        elif split_input[0] == "B" or split_input[0] == "Bus":
            return
        
        elif split_input[0] == "G" or split_input[0] == "Grade":
            return

        #Calculate the average of 
        elif split_input[0] == "A" or split_input[0] == "Average":
            return

        elif split_input[0] == "I" or split_input[0] == "Info":
            return
        # pass the data structure to the proper command


if __name__ == "__main__":
    main()


