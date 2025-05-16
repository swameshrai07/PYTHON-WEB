def write_to_file(filename):
    user_input = input("Enter text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(user_input + '\n')
    print("Data written to file.")

def append_to_file(filename):
    more_input = input("Enter more text to append to the file: ")
    with open(filename, 'a') as file:
        file.write(more_input + '\n')
    print("Data appended to file.")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("\nFinal content of the file:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


filename = 'output.txt'
write_to_file(filename)
append_to_file(filename)
read_file(filename)
