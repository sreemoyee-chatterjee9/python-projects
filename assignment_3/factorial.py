# Calculate Factorial Using a Function
user_input=int(input("Enter a number : "))

def factorial_output(n):
    factorial = 1
    input_number=n
    while input_number>0:
        factorial=factorial*input_number
        input_number=input_number-1
    return factorial

output_result=factorial_output(user_input)

print(f"Factorial of {user_input} is {output_result}.\n")
