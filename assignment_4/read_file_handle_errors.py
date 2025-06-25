try:
    with open("sample.txt", "r") as file:
        for line in file:
            print(line)  # This automatically adds an extra newline
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
