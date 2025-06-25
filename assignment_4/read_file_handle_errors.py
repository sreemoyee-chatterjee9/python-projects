try:
    with open("sample.txt", "r") as file:
        for line in file:
            print(line)
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
