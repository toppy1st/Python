#   PE12_3

import os

#   Building function to append lines to a file
def appending(Fname, lines):
    if os.path.exists(Fname):
        with open(Fname, 'a') as file:  
            for line in lines:
                file.write(line + "\n") 
        print(f"Lines were successfully appended to '{Fname}'.")
    else:
        print(f"File '{Fname}' does not exist. Creating a new file.")
        with open(Fname, 'w') as file:  
            for line in lines:
                file.write(line + '\n')
            print(f"File '{Fname}' was created and lines were written to it.")

    display_file(Fname)

#   Building function to display file contents
def display_file(Fname):
    if os.path.exists(Fname):
        print(f"\nContents of '{Fname}':\n")
        with open(Fname, 'r') as file:
            print(file.read())
    else:
        print(f"File '{Fname}' does not exist.")  
    
    
#   Building a function to list files in a folder
def Lfolder(Folpath):
    files = [f for f in os.listdir(Folpath) if os.path.isfile(os.path.join(Folpath, f))]
    return files

#   Building a function to ask the user to choose a file from the folder
def file_name(Folpath):
    files = Lfolder(Folpath)
    
    if not files:
        print("No files found in the folder.")
        return None

    print("Available files:")
    for idx, file in enumerate(files, 1):
        print(f"{idx}. {file}")
    
#   Asking the user to select a file
    while True:
        try:
            choice = int(input(f"Please select a file number (1-{len(files)}): "))
            if 1 <= choice <= len(files):
                return files[choice - 1]
            else:
                print("Invalid choice, please select a valid file number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#   Building main function
def main():
    Folpath = '/Users/thirihtet/Desktop/QBCC/Python/PE_12(Files_and_Exception)/PE'
    lines = ["James Madison", "James Monroe", "John Quincy Adams"]

    selected_file = file_name(Folpath)

    if selected_file:
        appending(selected_file, lines)

if __name__ == "__main__":
    main()



import random

# Function to generate a multiplication table of random numbers
def gen(n):
    table = []  # Initialize an empty list
    for i in range(1, n+1):  # Rows from 1 to n
        row = []  
        for j in range(1, n+1):  # Columns from 1 to n
            row.append(random.randint(1, 100))  # Generate random numbers between 1 and 100
        table.append(row)  # Add the row to the table
    return table

# Function to save the table to a file
def save(table, filename):
    with open(filename, 'w') as file:
        for row in table:  # Loop through each row
            line = " ".join(map(str, row))  # Convert numbers to strings and join them with spaces
            file.write(line + "\n")  # Write each row to the file with a newline
    print(f"Table saved to '{filename}'.")

# Function to display the table
def display_table(table):
    for row in table:
        print(" ".join(map(str, row)))  # Print rows with numbers separated by spaces

# Main Program
if __name__ == "__main__":
    n = int(input("Enter the size of the table (n x n): "))  # Ask user for table size
    table = gen(n)  # Generate the table
    print("\nGenerated Table:")
    display_table(table)  # Display the table to the user
    
    filename = "table.txt"  # File to save the table
    save(table, filename)  # Save the table to a file
    print("\nTable has been saved successfully.")

