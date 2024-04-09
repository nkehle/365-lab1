#Index 0 LASTNAME: COOKUS, 
#Index 1 FIRSTNAME: XUAN, 
#Index 2 GRADE: 3, 
#Index 3 CLASSROOM: 107,
#Index 4 BUS ROUTE: 52,
#Index 5 GPA: 3.07, 
#Index 6 TEACHER LN: FAFARD,
#Index 7 TEACHER F: ROCIO
import re
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
        user_input = input("Please enter a command:\n")
        split_input = handle_input(user_input)
        #print(split_input)
        if split_input[0] == "S" or split_input[0] == "Student":
            if len(split_input) == 3:
                if split_input[2] == "B" or split_input[2] == "Bus": 
                    StudentSearchBus(split_input, lines)
            else:
                StudentSearch(split_input, lines)

        elif split_input[0] == "T" or split_input[0] == "Teacher":
            TeacherSearch(split_input, lines)
                
        elif split_input[0] == "B" or split_input[0] == "Bus":
            StudentSearchBus(split_input, lines)
                
        elif split_input[0] == "G" or split_input[0] == "Grade":
            if len(split_input) == 3:
                if split_input[2] == "H":
                    GradeSearchHigh(split_input, lines)
                elif split_input[2] == "L": 
                    GradeSearchLow(split_input, lines)
            else:
                GradeSearch(split_input, lines)
            

        elif split_input[0] == "A" or split_input[0] == "Average":
            return

        elif split_input[0] == "I" or split_input[0] == "Info":
            return

# handles the options of having a B or H or L
def handle_input(user_input):
    parts = user_input.split()
    
    command = parts[0]
    if ':' in command:
        command = command.split(':')[0]

    user_input = parts[1]
    letter = None
    if len(parts) > 2:
        letter = parts[2]

    if letter:
        return command, user_input, letter
    else: 
        return command, user_input

# searches through and finds all students with a given grade
def GradeSearch(atribute, lines):
    res_lst = []
    for lst in lines:
        if lst[2] == atribute[1]:
            found = [lst[0], lst[1]]
            result = ', '.join(found)
            res_lst.append(result)
    for item in res_lst:
        print(item)

# searches through and finds the highest gpa in a given grade
def GradeSearchHigh(atribute, lines):
    tmp = 0.0
    for lst in lines:
        if lst[2] == atribute[1]:
            val = float(lst[5])
            if val >= tmp:
                tmp = val
                res = [lst[0], lst[1]]
    print(res)

# searches through and finds the lowest gpa in a given grade
def GradeSearchLow(atribute, lines):
    tmp = 0.0
    for lst in lines:
        if lst[2] == atribute[1]:
            val = float(lst[5])
            if val <= tmp:
                tmp = val
                res = [lst[0], lst[1]]
    print(res)

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


