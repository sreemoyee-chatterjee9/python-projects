# Using the Math Module for Calculations
import math

user_input = int(input("Enter a number : "))

square_root=math.sqrt(user_input)
logarithm=math.log(user_input)
number_in_radians=math.radians(user_input)
sine=math.sin(number_in_radians)
sine_in_degrees=math.sin(user_input)

print(
    f"""
    Square Root     : {square_root}\n
    Logarithm       : {logarithm}\n
    sine in radians : {sine}\n
    sine in degrees : {sine_in_degrees}
    """
)
