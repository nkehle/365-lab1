# CSC 365
# Lab 1-a test suite

import unittest
import schoolsearch
import sys
from io import StringIO
# from schoolsearch import 
file = open('students.txt', 'r')
lines = [line.strip().split(',') for line in file]

class TestSearch(unittest.TestCase):

# TC - 1
# Tests Requirements: R3 R11
# short form command name, Student Info
# expected output: 0 : 0\n1 : 2\n2 : 13\n3 : 9\n4 : 15\n5 : 0"
# Command: I
    def test_InfoSearch(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        schoolsearch.InfoSearch(lines)
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue().strip()
        self.assertEqual(printed_output, "0 : 0\n1 : 2\n2 : 13\n3 : 9\n4 : 15\n5 : 0")

# TC - 2
# Tests Requirements: R3 R10
# short form command name, Calculate Average GPA 
# expected output: 3 3.048888888888889
# Command: A 3
    def test_AverageSearch(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        schoolsearch.AverageSearch(('A', '3'), lines)
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue().strip()
        self.assertEqual(printed_output, "3 3.048888888888889")


# TC - 3
# Tests Requirements: R3 R7
# short form command name, Find all students in Grade G
# expected output: SAELEE, DANILO\nGARTH, JOHN
# Command: G 1
    def test_GradeSearch(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        schoolsearch.GradeSearch(('G', '1'), lines)
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue().strip()
        self.assertEqual(printed_output, "SAELEE, DANILO\nGARTH, JOHN")

# TC - 4
# Tests Requirements: R3 R9
# short form command name, Highest GPA in Grade
# expected output: SHARRI SWEDLUND
# Command: G 3 H
    def test_GradeSearchHigh(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        schoolsearch.GradeSearchHigh(('G', '3', 'H'),lines)
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue().strip()
        self.assertEqual(printed_output, "SHARRI SWEDLUND")

# TC - 5
# Tests Requirements: R3 R9
# short form command name, Lowest GPA in Grade
# expected output: MANIE CIGANEKN
# Command: G 3 L
    def test_GradeSearchLow(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        schoolsearch.GradeSearchLow(('G', '3', 'L'), lines)
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue().strip()
        self.assertEqual(printed_output, "MANIE CIGANEK")

# TC - 6
# Tests Requirements: R3 R4 
# Long form command name, existing student
# expected output: WOOLERY, NOLAN, 2, 104, STEIB, GALE
# Command: STUDENT WOOLERY
    def test_StudentSearch(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        schoolsearch.StudentSearch(('STUDENT','WOOLERY'), lines)
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue().strip()
        self.assertEqual(printed_output, "WOOLERY, NOLAN, 2, 104, STEIB, GALE")


# TC - 7
# Tests Requirements: R3 R4 R5
# short form command name, existing student Bus
# expected output: WOOLERY, NOLAN, 51
# Command: S WOOLERY B
    def test_StudentSearchBus(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        schoolsearch.StudentSearchBus(('S', 'WOOLERY', 'B'), lines)
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue().strip()
        self.assertEqual(printed_output, "WOOLERY, NOLAN, 51")

# TC - 8
# Tests Requirements: R3 R12
# short form command name, Quit
# expected output: ''
# Command: Q
    def test_Quit(self):
        captured_output = StringIO()
        schoolsearch.main("Q")
        # sys.stdin = sys.__stdin__
        printed_output = captured_output.getvalue().strip()
        self.assertEqual(printed_output, "")

        

if __name__ == '__main__':
    unittest.main()