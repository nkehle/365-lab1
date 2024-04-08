#Index 0 LASTNAME: COOKUS, 
#Index 1 FIRSTNAME: XUAN, 
#Index 2 GRADE: 3, 
#Index 3 CLASSROOM: 107,
#Index 4 BUS ROUTE: 52,
#Index 5 GPA: 3.07, 
#Index 6 TEACHER LN: FAFARD,
#Index 7 TEACHER F: ROCIO

#import sys
# Coded each search individually which I realize is inneficient since duplicate code but ultimatly i could copy and paste and I was lazy
def main():
    # split into lines
    file = open('students.txt', 'r')
    #lines is a list of list, where each list is a line of the file. 
    # put into data structure
    lines = [line.strip().split(',') for line in file]
   # print(lines)


    user_input = ""
    while(user_input != "Q"):
        user_input = input("Please enter a command:")
        split_input = user_input.split()
        if split_input[0] == "S" or split_input[0] == "Student":
            if len(split_input) == 3:
                if split_input[2] == "B" or split_input[2] == "Bus": 
                    StudentSearchBus(split_input, lines)
            else:
                StudentSearch(split_input, lines)

        elif split_input[0] == "T" or split_input[0] == "Teacher":
            TeacherSearch(split_input, lines)
                
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

#print the last name, first name, grade and classroom assignment for
#each student found and the name of their teacher (last and first name).
def StudentSearch(atribute, lines):
    res_lst = []
    for lst in lines:
                for item in lst:
                    if item == atribute[1]:
                         found = [lst[0], lst[1], lst[2], lst[3], lst[6], lst[7]]
                         result = ', '.join(found)
                         res_lst.append(result)
    for item in res_lst:
        print(item)

def StudentSearchBus(atribute, lines):
    res_lst = []
    for lst in lines:
                for item in lst:
                    if item == atribute[1]:
                         found = [lst[0], lst[1], lst[4]]
                         result = ', '.join(found)
                         res_lst.append(result)
    for item in res_lst:
        print(item)

def TeacherSearch(atribute, lines):
    res_lst = []
    for lst in lines:
                for item in lst:
                    if item == atribute[1]:
                         found = [lst[0], lst[1]]
                         result = ', '.join(found)
                         res_lst.append(result)
    for item in res_lst:
        print(item)

if __name__ == "__main__":
    main()


