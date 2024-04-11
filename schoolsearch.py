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
    lines = [line.strip().split(',') for line in file]

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
            AverageSearch(split_input, lines)

        elif split_input[0] == "I" or split_input[0] == "Info":
            InfoSearch(lines)

# handles the options of having a B or H or L
def handle_input(user_input):
    parts = user_input.split()
    
    if len(parts) < 2:
        return parts

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

# searches through and finds the number of students in each grade
def InfoSearch(lines):
    res = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0]]
    for i in range(6):
        for lst in lines:
            if lst[2] == str(i):
                res[i][1] += 1
    cnt = 0
    for grade in res:
        print(grade[0], ":", grade[1])

# searches through computes the average gpa for students in a grade
# and ouputs the grade and average gpa
def AverageSearch(atribute, lines):
    total = 0.0
    cnt = 0
    for lst in lines:
        if lst[2] == atribute[1]:
            val = float(lst[5])
            cnt += 1
            total += val

    print(atribute[1], total/cnt)

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
    print(res[1], res[0])

# searches through and finds the lowest gpa in a given grade
def GradeSearchLow(atribute, lines):
    tmp = 4.0 # start at max gpa
    for lst in lines:
        if lst[2] == atribute[1]:
            val = float(lst[5])
            if val <= tmp:
                tmp = val
                res = [lst[0], lst[1]]
    print(res[1], res[0])

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


