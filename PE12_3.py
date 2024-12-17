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
