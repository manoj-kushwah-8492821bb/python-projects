firstInput = input("Please enter your first value : ")
operator = input("Please tell what you want : ")
secondInput = input("Please enter your first value : ")

# when user wants to sum
if operator=="+":
   print(int(firstInput) + int(secondInput))

# when user wants to difference
elif operator=="-":
   print(int(firstInput) - int(secondInput))

# when user wants to product
elif operator=="*":
    print(int(firstInput) * int(secondInput))

# when user wants to divide
elif operator=="/":
    print(int(firstInput) / int(secondInput))

# when user wants to remainder
elif operator=="%":
    print(int(firstInput) % int(secondInput))

