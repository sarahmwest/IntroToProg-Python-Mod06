# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Working With Functions, Classes, and Separations of Concern
# Desc: This assignment demonstrates using functions, classes, and separations of concern.
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   S.West, 11/18/24, Modified Script
# ------------------------------------------------------------------------------------------ #
import json  # Imports JSON Module

# --------------------DATA------------------------- #
# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str = ''  # Hold the choice made by the user.


# --------------------PROCESSING-------------------- #

class FileProcessor():
    """
    This class contains a collection of functions for processing JSON files.
    ChangeLog:
    S.West, 18Nov24: Created class, added functions that reads data from file, and writes data to file.
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function reads and extracts the JSON data file when the program starts.
        ChangeLog:
        S.West, 18Nov24: Created function.
        Return = student_data (list)
        """
        try:
            file = open(file_name, "r")  # Extract the data from the file
            student_data = json.load(file)  # Loads data stored in the file into the variable student_data
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running the script!", e)
        except Exception as e:
            IO.output_error_messages("There is a non-specific error!", e)
        finally:
            if file.close == False:
                file.close()
        return student_data  # The output of this function is in the loaded variable, student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This function writes the old and user imputed data to the JSON file.
        ChangeLog:
        S.West, 18Nov24: Created function
        Return = None
        """
        try:
            file = open(file_name, "w")  # Opens the file name with write permission
            json.dump(student_data, file)  # Adds all the data stored in student_data to the file.
            file.close()  # Close and save the file.
        except TypeError as e:  # Calls custom error message if exception is raised.
            IO.output_error_messages("The data type is wrong!", e)
        except Exception as e:
            IO.output_error_messages("There is a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()


# --------------------PRESENTATION-------------------- #

class IO:
    """
    A collection of presentation layer functions that manage user I/O.
    Changelog:
    S.West, 18Nov24: Created class, added menu output and input functions,
    added functions to display the data and custom error messages.
    """

    @staticmethod
    def input_menu_choice():
        """
        This function takes the user input to select an option from the menu.
        ChangeLog:
        S.West, 18Nov24: Created function.
        Return = choice (string)
        """
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Please only choose 1-4!")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice

    @staticmethod
    def output_error_messages(message: str,
                              error: Exception = None):  # Custom error messages to be called if exception is raised
        """
        This functions handles errors with custom messages if errors are raised!
        Changelog:
        S.West, 18Nov24: Created function.
        Return: None
        """
        print(message, end="\n\n")  # message is a local variable
        if error is not None:  # If Exceptions = None is NOT TRUE, then this will execute!
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        This function displays the menu choices to the user
        ChangeLog:
        S.West, 18Nov24: Created function.
        Return = None
        """
        print(menu)  # The local variable is assigned to MENU in the function call below
        print()

    @staticmethod
    def output_student_course(student_data: list):
        """
        This function shows the students currently registered for their courses.
        ChangeLog:
        S.West, 18Nov24: Created function.
        Return = None
        """
        print("-" * 50)
        for student in student_data:  # Prints each student's info stored in the variable student_data
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """
        This function takes the student's name and course form the user.
        ChangeLog:
        S.West, 18Nov24: created function
        Return = student_data (list)
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}  # the variable student is defined as a dictionary here
            student_data.append(student)  # Appending the entered data in student to the variable student_data
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("That value is not the correct data type.", e)
        except Exception as e:
            IO.output_error_messages("There was an unspecific error!", e)
        return student_data


# -----------------Beginning of the main body of the script---------------#
# When program runs, the data is read from the JSON file and stored into variable "students".
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

while True:
    IO.output_menu(menu=MENU)  # the variable menu_choice is assigned to the output of the function.
    menu_choice = IO.input_menu_choice()  # variable menu_choice equals the return value (choice) of the function
    # Input user data
    if menu_choice == "1":
        students = IO.input_student_data(student_data=students)
        continue
    # Present the current data:
    elif menu_choice == "2":
        IO.output_student_course(student_data=students)
        continue
    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        IO.output_student_course(student_data=students) # Outputs the student data that was written to the file.
        continue
    # Stop the loop
    elif menu_choice == "4":
        break

print("Program Ended")
