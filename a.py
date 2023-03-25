file_name = input("Enter file name: ")

try:

    with open(file_name, "r") as file:

        lines = file.readlines()

except FileNotFoundError:

    print("File not found.")

    exit()

unique_lines = list(set(lines))

try:

    with open(file_name, "w") as file:

        file.writelines(unique_lines)

except:

    print("Error writing to file.")

    exit()

print(f"{len(lines) - len(unique_lines)} duplicate line(s) removed.")

