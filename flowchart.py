myVar = input("Does It Move? (yes/no) ")
if myVar == "yes":
  myNextVar = input("Should it? (yes/no) ")
  if myNextVar == "yes":
    print("No Problem")
  elif myNextVar == "no":
    print("Then use the duct tape! ")
  else:
    print("Answer my question! You didn't type yes or no.")
elif myVar == "no":
  print("Then stop it from moving! ")
else:
  print("Answer my question! You didn't type yes or no.")
