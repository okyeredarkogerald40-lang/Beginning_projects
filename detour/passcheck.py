import string

def check_password_length(password):
  if len(password) < 8:
    print("Password is too short")
  elif len(password) >= 8 and len(password) <= 12:
    print("Length is okay")
  else:
    print("Maximum number of characters is 12")

def check_password_strength(password):
  has_upper = False
  has_digit = False
  has_punct = False
  for char in password:
    if char.isupper():
      has_upper = True
    if char.isdigit():
      has_digit = True
    if char in string.punctuation:
      has_punct = True 

  
  if has_upper == False:
    print("Password is weak")
    print("Password requires at least one uppercase letter")
  elif has_digit == False:
    print("Password is weak")
    print("Password requires at least one digit")
  elif has_punct == False:
    print("Password is weak")
    print("Password requires at least one symbol")
  elif has_upper and has_digit and has_punct:
      print("Password is strong")
      

def main():
  while True:
    print("---- PASSWORD STRENGTH CHECKER ----")
    user_password = input("Enter your password: ")
    if user_password == "Exit":
      print("Exiting...")
      break
    check_password_length(user_password)
    check_password_strength(user_password)

if __name__ == "__main__":
  main()


