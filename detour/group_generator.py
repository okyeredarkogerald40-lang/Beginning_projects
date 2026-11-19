import random
names = ['Gerald', 'Ezra', 'Otis', 'Michelle', 'Francis', 'Bryan', 'Sam', 'Alvin']




def main():
  print("Generating names....")
  random.shuffle(names)

  midpoint = len(names) // 2
  group1 = names[:midpoint]
  group2 = names[midpoint:]

  print("\nGroups generated.")

  print("\nGroup 1:")
  for person in group1:
    print(person)

  print("\nGroup 2:")  
  for student in group2:
    print(student) 

if __name__ == "__main__":
  main()
  
    