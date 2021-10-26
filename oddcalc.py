firstnumber = input("Give me a number, any number...")
secondnumber = input("Wonderful, and give me another number...")
operation = input("And what operation do you want? (mul, div, or mod)")
if operation == "mul":
    print(int(firstnumber) * int(secondnumber))
elif operation == "div":
    print(int(firstnumber) / int(secondnumber))
elif operation == "mod":
    print(int(firstnumber) % int(secondnumber))
else:
    print("***Invalid Operation!!!***")
