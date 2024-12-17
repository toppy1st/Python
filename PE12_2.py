import csv
import os  

print()

#   Building function to display the file
def display_file(filename):
    if os.path.exists(filename):
        print(f"\nContents of '{filename}':\n")
        with open(filename, 'r') as file:
            print(file.read())
    else:
        print(f"\nFile '{filename}' does not exists, so no contents to display.\n")


#   With CSV
def csvfile(Pres1, Cdatas):
    if os.path.exists(Pres1): 
        print(f"CSV file '{Pres1}' already exists.")
    else:
        with open(Pres1, 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerows(Cdatas)
            print(f"CSV file '{Pres1}' is created.")
        
        display_file(Pres1)
    
#   Asking if the user wants to delete the file after creation
    delete = input(f"Do you want to delete the file '{Pres1}'? (y/n): ")
    if delete.lower() == 'y' and os.path.exists(Pres1):
        os.remove(Pres1)
        print(f"CSV file '{Pres1}' has been deleted.")
    elif delete.lower() == 'n':
        print(f"CSV file '{Pres1}' was not deleted.")
        display_file(Pres1)
    else:
        print("Invalid input. File not deleted.")

print()

#   Using write() in a loop
def Wwrite(Pres2, Wdatas):
    if os.path.exists(Pres2):
        print(f"\n'{Pres2}' [write()] file already exists.")
    else:
        with open(Pres2, 'w') as file:
            for Wdata in Wdatas:
                file.write(Wdata + '\n')
            print(f"\nFile '{Pres2}' is created using write().")
        
        display_file(Pres2)
    
#   Asking if the user wants to delete the file after creation
    delete = input(f"Do you want to delete the file '{Pres2}'? (y/n): ")
    if delete.lower() == 'y' and os.path.exists(Pres2):
        os.remove(Pres2)
        print(f"The file [write()] '{Pres2}' has been deleted.")
    elif delete.lower() == 'n':
        print(f"The file [write()] '{Pres2}' was not deleted.")
        display_file(Pres2)
    else:
        print("Invalid input. File not deleted.")

print()

#   Building main function
def main():
    csv_data = [["George Washington"], ["John Adams"]]
    csvfile("Pres1.csv", csv_data)
    
    Wdatas = ["George Washington", "John Adams", "Thomas Jefferson"]
    Wwrite("Pres2.txt", Wdatas)

    folder_path = '/Users/thirihtet/Desktop/QBCC/Python/PE_12(Files_and_Exception)/PE'

#   Checking if file already exists before calling the function again with full path
    if not os.path.exists(os.path.join(folder_path, 'Pres1.csv')):
        csvfile(os.path.join(folder_path, 'Pres1.csv'), csv_data)

    if not os.path.exists(os.path.join(folder_path, 'Pres2.txt')):
        Wwrite(os.path.join(folder_path, 'Pres2.txt'), Wdatas)

if __name__ == "__main__":
    main()

print()






import os

# Define the Employee class
class Employee:
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = str(name)
        self.hours_worked = float(hours_worked)
        self.hourly_rate = float(hourly_rate)

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

# Function to create an employee file with sample data
def create_employee_file(filename):
    if not os.path.exists(filename):  # Only create the file if it doesn't exist
        with open(filename, 'w') as file:
            file.write("Alice,40,15\n")
            file.write("Bob,35,20\n")
            file.write("Charlie,45,18\n")
        print(f"File '{filename}' created with sample employee data.\n")
    else:
        print(f"File '{filename}' already exists. Using the existing file.\n")

# Function to read employee data from file
def read_data(filename):
    employees = []  # List to store Employee objects
    if os.path.exists(filename):
        print(f"Reading employee data from {filename}...")
        with open(filename, 'r') as file:
            for line in file:
                name, hours_worked, hourly_rate = line.strip().split(",")
                employees.append(Employee(name, hours_worked, hourly_rate))
    else:
        print(f"Error: File {filename} does not exist.")
    return employees

# Function to write employee salaries to a file
def write_salary(employees, filename):
    with open(filename, 'w') as file:
        for employee in employees:
            salary = employee.calculate_salary()
            file.write(f"{employee.name}: ${salary:.2f}\n")
    print(f"Salary data has been written to '{filename}'.\n")

# Main Program
if __name__ == "__main__":
    input_file = "employees.txt"  # Input file name
    output_file = "salaries.txt"  # Output file name

    # Step 1: Create an employee file if it doesn't exist
    create_employee_file(input_file)

    # Step 2: Read employee data
    employees = read_data(input_file)

    # Step 3: Display and write salaries
    if employees:
        print("Employee Weekly Salaries:")
        for employee in employees:
            print(f"{employee.name}: ${employee.calculate_salary():.2f}")
        
        # Write to output file
        write_salary(employees, output_file)