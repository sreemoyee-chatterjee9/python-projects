# Sum of Integers from 1 to 50 Using a Loop
range_number=int(input("Enter the range : "))
i=0
sum=0
for i in range(1,range_number+1):
    sum +=i
    i+= 1
print(f"The sum of numbers from 1 to {range_number} is : {sum}")
