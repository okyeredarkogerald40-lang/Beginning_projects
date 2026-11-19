info = [
  {
    "year": "First year",
    "semester": [1, 2],
    "number of courses": [8, 6]
    
  },
  {
    "year": "Second year",
    "semester": [1, 2],
    "number of courses": [8, 7]
  },
  {
    "year": "Third year",
    "semester": [1, 2],
    "number of courses": [7, 7]

  },
  {
    "year": "Fourth year",
    "semester": [1, 2],
    "number of courses": [7, 6]
  }
]

all_weighted_marks = []
all_credit_hours = []
while True:
  print("----CWA CALCULATOR----")

  for i in range(len(info)):
    level = info[i]
    print(f"{i + 1}. {level["year"]}")
    
  year = int(input("Enter year: "))
  semester = int(input("Enter semester: "))

  number_of_courses = 0
  for item in info:
    if year == info.index(item) + 1:
      if semester == 1:
        number_of_courses = item["number of courses"][0]
      elif semester == 2:
        number_of_courses = item["number of courses"][1]

  print(f"\nEntering marks for {number_of_courses} courses:")
  for course_num in range(number_of_courses):
    print(f"\nCourse {course_num + 1}:")
    mark = int(input("Enter your mark: "))
    credit_hour = int(input("Enter credit hours: "))
    all_credit_hours.append(credit_hour)
    weighted_mark = mark * credit_hour
  
  Total_weighted_marks = sum(all_weighted_marks)
  Total_credit_hours = sum(all_credit_hours)
  
  cwa = Total_weighted_marks/Total_credit_hours
  print(f"Your cwa is {cwa}")

  if cwa >= 80.00:
    print("First class")
  elif cwa <= 79.99 and cwa >= 70.00:
    print("Second class upper")
  elif cwa <= 69.99 and cwa >= 65.00:
    print("Second class lower")
  elif cwa <= 64.99 and cwa >= 60.00:
    print("Third class")
  elif cwa <= 59.99 and cwa >= 50.00:
    print("Pass")
  else:
    print("Fail")

  

  
  
  

