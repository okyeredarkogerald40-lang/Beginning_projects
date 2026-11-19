calculating = False

while not calculating:
  try:
    user_input = input("Enter a number(or 'q' to quit): ")
    if user_input == "q":
       print("Exiting calculator.")
       calculating = True
       break
    first_number = float(user_input)
    operator = input("Operator: ")
    second_number = float((input("Enter a number: ")))
    if operator == "+":
      result = first_number + second_number
      if result.is_integer():
        result = int(result)
      print(f"Ans: {result}")
    elif operator == "-":
        result = first_number - second_number
        if result.is_integer():
          result = int(result)
        print(f"Ans: {result}")
    elif operator == "*":
        result = first_number * second_number
        if result.is_integer():
          result = int(result)
        print(f"Ans: {result}")
    elif operator == "/":
      if second_number == 0:
         print("Error: Division by Zero")
         continue
      result = first_number/second_number
      if result.is_integer():
        result = int(result)
      print(f"Ans: {result}")
  except ValueError:
     print("Enter valid number.")
  
  
 
