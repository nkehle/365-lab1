import students.txt

def main():
    # split into lines
    file = students.txt
    lines = file.split()

    # put into data structure

    user_input = ""
    while(user_input != "Q"):
        user_input = input("Please enter a command:")

        # pass the data structure to the proper command


if __name__ == "__main__":
    main()


